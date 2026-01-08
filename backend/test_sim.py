from simulation import SimulationEngine

def run_test():
    print("Initializing MESA Test...")
    sim = SimulationEngine()
    
    print("\nRunning 10 simulation ticks...")
    for i in range(1, 11):
        state = sim.tick()
        print(f"Tick {i}: Price=${state.last_price}, Bids={len(state.orderbook.bids)}, Asks={len(state.orderbook.asks)}, Trades={len(state.recent_trades)}")
        
    print("\nSimulation test complete.")

if __name__ == "__main__":
    run_test()
