from .base import BaseAgent
from models import Order, OrderSide, OrderBookState
from typing import Optional

class FundamentalAgent(BaseAgent):
    def __init__(self, true_value: float = 100.0):
        super().__init__("Fundamental")
        self.true_value = true_value

    def decide(self, price_history, current_price, orderbook_state) -> Optional[Order]:
        # Simple fundamental agent: buy if cheap, sell if expensive
        deviation = (current_price - self.true_value) / self.true_value
        
        if deviation < -0.05:  # Undervalued by 5%
            return self._create_order(OrderSide.BUY, current_price * 1.001, 15)
        elif deviation > 0.05:  # Overvalued by 5%
            return self._create_order(OrderSide.SELL, current_price * 0.999, 15)
            
        return None
