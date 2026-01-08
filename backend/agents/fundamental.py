from .base import BaseAgent
from models import Order, OrderSide, OrderBookState
from typing import Optional

class FundamentalAgent(BaseAgent):
    def __init__(self, true_value: float = 100.0):
        super().__init__("Fundamental")
        self.true_value = true_value

    def decide(self, price_history, current_price, orderbook_state) -> Optional[Order]:
        # Calculate how far price is from true value
        deviation = (current_price - self.true_value) / self.true_value
        
        # MORE AGGRESSIVE: 1% threshold instead of 5%
        if deviation < -0.01:  # Undervalued by 1%
            # Buy aggressively - price is below fair value!
            return self._create_order(OrderSide.BUY, current_price * 1.002, 25)
        elif deviation > 0.01:  # Overvalued by 1%
            # Sell aggressively - price is above fair value!
            return self._create_order(OrderSide.SELL, current_price * 0.998, 25)
            
        return None
