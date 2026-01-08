from .base import BaseAgent
from models import Order, OrderSide, OrderBookState
from typing import Optional

class TrendFollowerAgent(BaseAgent):
    def __init__(self, window: int = 10):
        super().__init__("TrendFollower")
        self.window = window

    def decide(self, price_history, current_price, orderbook_state) -> Optional[Order]:
        if len(price_history) < self.window:
            return None
            
        recent_avg = sum(price_history[-self.window:]) / self.window
        
        # If current price is significantly above moving average, buy (follow the trend)
        if current_price > recent_avg * 1.005:
            return self._create_order(OrderSide.BUY, current_price * 1.001, 10)
        # If significantly below, sell
        elif current_price < recent_avg * 0.995:
            return self._create_order(OrderSide.SELL, current_price * 0.999, 10)
            
        return None
