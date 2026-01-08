from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from simulation import SimulationEngine
import asyncio
import json

app = FastAPI(title="MESA - Multi-Agent Exchange Simulator")

# CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global simulation instance
sim = SimulationEngine()
is_running = False

@app.get("/")
async def root():
    return {"status": "MESA Backend Running"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    global is_running
    try:
        while True:
            if is_running:
                state = sim.tick()
                # Use json.dumps with default=str for datetime objects
                await websocket.send_text(state.json())
            else:
                # If not running, still send current state but don't tick
                # Fetching state from sim without ticking
                # (Need a method for that, but tick() is fine for now; 
                # we can just send the last produced state)
                pass
            
            await asyncio.sleep(0.1) # 100ms per simulated step
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"WS Error: {e}")

@app.post("/simulation/start")
async def start_sim():
    global is_running
    is_running = True
    return {"status": "started"}

@app.post("/simulation/stop")
async def stop_sim():
    global is_running
    is_running = False
    return {"status": "stopped"}

@app.post("/simulation/reset")
async def reset_sim():
    global sim, is_running
    sim = SimulationEngine()
    is_running = False
    return {"status": "reset"}

@app.post("/agents/add/{agent_type}")
async def add_agent(agent_type: str):
    sim.coordinator.add_agent(agent_type)
    return {"status": "added", "type": agent_type}

@app.post("/agents/remove/{agent_type}")
async def remove_agent(agent_type: str):
    sim.coordinator.remove_agent(agent_type)
    return {"status": "removed", "type": agent_type}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
