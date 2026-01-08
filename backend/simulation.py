from typing import List
from models import MarketState, Trade
from orderbook import OrderBook
from matching import MatchingEngine
from coordinator import AgentCoordinator
import numpy as np

class SimulationEngine:
    def __init__(self):
        self.orderbook = OrderBook()
        self.matching_engine = MatchingEngine(self.orderbook)
        self.coordinator = AgentCoordinator()
        
        self.tick_count = 0
        self.price_history = [100.0]
        self.all_trades: List[Trade] = []
        
        # NO DEFAULT AGENTS - user controls everything via UI

    def tick(self) -> MarketState:
        self.tick_count += 1
        
        # 1. Get current state
        current_price = self.matching_engine.last_price
        ob_state = self.orderbook.get_state()
        
        # 2. Get orders from agents
        new_orders = self.coordinator.get_orders(self.price_history, current_price, ob_state)
        
        # 3. Process orders through matching engine
        tick_trades = []
        for order in new_orders:
            trades = self.matching_engine.process_order(order)
            tick_trades.extend(trades)
            
        self.all_trades.extend(tick_trades)
        
        # Update price history if trades occurred
        if tick_trades:
            self.price_history.append(self.matching_engine.last_price)
        else:
            self.price_history.append(self.price_history[-1])
            
        # Keep history manageable
        if len(self.price_history) > 1000:
            self.price_history.pop(0)

        # 4. Calculate metrics
        volatility = float(np.std(self.price_history[-20:])) if len(self.price_history) >= 20 else 0.0
        volume = sum(t.quantity for t in tick_trades)
        
        return MarketState(
            tick=self.tick_count,
            last_price=round(self.matching_engine.last_price, 2),
            orderbook=ob_state,
            recent_trades=tick_trades,
            price_history=self.price_history[-100:], # Send last 100 points
            agents=self.coordinator.get_agent_counts(),
            metrics={
                "volatility": round(volatility, 4),
                "volume": volume
            }
        )

    def reset(self):
        self.__init__()
