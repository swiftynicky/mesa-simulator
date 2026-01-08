from typing import List, Dict, Type
from agents.base import BaseAgent
from agents.noise_trader import NoiseTraderAgent
from agents.trend_follower import TrendFollowerAgent
from agents.mean_reversion import MeanReversionAgent
from agents.fundamental import FundamentalAgent
from models import Order, OrderBookState

class AgentCoordinator:
    def __init__(self):
        self.agents: List[BaseAgent] = []
        self.agent_map: Dict[str, Type[BaseAgent]] = {
            "NoiseTrader": NoiseTraderAgent,
            "TrendFollower": TrendFollowerAgent,
            "MeanReversion": MeanReversionAgent,
            "Fundamental": FundamentalAgent
        }

    def add_agent(self, agent_type: str):
        if agent_type in self.agent_map:
            agent_class = self.agent_map[agent_type]
            self.agents.append(agent_class())

    def remove_agent(self, agent_type: str):
        for i, agent in enumerate(self.agents):
            if agent.agent_type == agent_type:
                self.agents.pop(i)
                break

    def get_orders(self, price_history: List[float], current_price: float, orderbook_state: OrderBookState) -> List[Order]:
        orders = []
        # Shuffle agents to prevent bias
        import random
        shuffled_agents = list(self.agents)
        random.shuffle(shuffled_agents)
        
        for agent in shuffled_agents:
            order = agent.decide(price_history, current_price, orderbook_state)
            if order:
                orders.append(order)
        return orders

    def get_agent_counts(self) -> Dict[str, int]:
        counts = {atype: 0 for atype in self.agent_map.keys()}
        for agent in self.agents:
            counts[agent.agent_type] += 1
        return counts
