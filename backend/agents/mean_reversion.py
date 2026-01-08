from .base import BaseAgent
from models import Order, OrderSide, OrderBookState
from typing import Optional

class MeanReversionAgent(BaseAgent):
    def __init__(self, window: int = 10):  # Shorter window
        super().__init__("MeanReversion")
        self.window = window

    def decide(self, price_history, current_price, orderbook_state) -> Optional[Order]:
        if len(price_history) < self.window:
            return None
            
        long_avg = sum(price_history[-self.window:]) / self.window
        
        # MORE AGGRESSIVE: 0.5% threshold instead of 2%
        # If price is high relative to average, SELL (expect it to fall back)
        if current_price > long_avg * 1.005:
            return self._create_order(OrderSide.SELL, current_price * 0.998, 20)
        # If price is low, BUY (expect it to rise back)
        elif current_price < long_avg * 0.995:
            return self._create_order(OrderSide.BUY, current_price * 1.002, 20)
            
        return None
