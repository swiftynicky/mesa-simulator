from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from simulation import SimulationEngine
from models import MarketState
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

def get_current_state() -> MarketState:
    """Get current state without advancing the simulation"""
    ob_state = sim.orderbook.get_state()
    return MarketState(
        tick=sim.tick_count,
        last_price=round(sim.matching_engine.last_price, 2),
        orderbook=ob_state,
        recent_trades=[],
        price_history=sim.price_history[-100:],
        agents=sim.coordinator.get_agent_counts(),
        metrics={
            "volatility": 0.0,
            "volume": 0
        }
    )

@app.head("/")
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
                await websocket.send_text(state.json())
            else:
                # When paused, still send current state so UI stays updated
                state = get_current_state()
                await websocket.send_text(state.json())
            
            await asyncio.sleep(0.1)  # 100ms update rate
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
    return {"status": "added", "type": agent_type, "count": sim.coordinator.get_agent_counts()}

@app.post("/agents/remove/{agent_type}")
async def remove_agent(agent_type: str):
    sim.coordinator.remove_agent(agent_type)
    return {"status": "removed", "type": agent_type, "count": sim.coordinator.get_agent_counts()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
