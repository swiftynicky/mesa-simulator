from abc import ABC, abstractmethod
from typing import Optional
from models import Order, OrderSide, OrderBookState
import uuid
from datetime import datetime

class BaseAgent(ABC):
    def __init__(self, agent_type: str, cash: float = 10000.0):
        self.id = f"{agent_type}_{uuid.uuid4().hex[:6]}"
        self.agent_type = agent_type
        self.cash = cash
        self.holdings = 0

    @abstractmethod
    def decide(self, 
               price_history: list[float], 
               current_price: float, 
               orderbook_state: OrderBookState) -> Optional[Order]:
        pass

    def _create_order(self, side: OrderSide, price: float, quantity: int) -> Order:
        return Order(
            id=f"O-{uuid.uuid4().hex[:6]}",
            agent_id=self.id,
            side=side,
            price=round(price, 2),
            quantity=quantity,
            timestamp=datetime.now()
        )
