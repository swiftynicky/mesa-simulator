from .base import BaseAgent
from models import Order, OrderSide, OrderBookState
from typing import Optional

class MeanReversionAgent(BaseAgent):
    def __init__(self, window: int = 20):
        super().__init__("MeanReversion")
        self.window = window

    def decide(self, price_history, current_price, orderbook_state) -> Optional[Order]:
        if len(price_history) < self.window:
            return None
            
        long_avg = sum(price_history[-self.window:]) / self.window
        
        # If price is high relative to average, sell (expect fall)
        if current_price > long_avg * 1.02:
            return self._create_order(OrderSide.SELL, current_price * 0.999, 10)
        # If price is low, buy (expect rise)
        elif current_price < long_avg * 0.98:
            return self._create_order(OrderSide.BUY, current_price * 1.001, 10)
            
        return None
