from .base import BaseAgent
from models import Order, OrderSide, OrderBookState
from typing import Optional

class TrendFollowerAgent(BaseAgent):
    def __init__(self, window: int = 5):  # Shorter window = faster reaction
        super().__init__("TrendFollower")
        self.window = window

    def decide(self, price_history, current_price, orderbook_state) -> Optional[Order]:
        if len(price_history) < self.window:
            return None
            
        recent_avg = sum(price_history[-self.window:]) / self.window
        
        # MORE AGGRESSIVE: 0.1% threshold instead of 0.5%
        # If current price is above moving average, BUY (chase the trend!)
        if current_price > recent_avg * 1.001:
            # Buy aggressively above current price to ensure execution
            return self._create_order(OrderSide.BUY, current_price * 1.002, 15)
        # If below average, SELL (follow the downtrend)
        elif current_price < recent_avg * 0.999:
            return self._create_order(OrderSide.SELL, current_price * 0.998, 15)
            
        return None
