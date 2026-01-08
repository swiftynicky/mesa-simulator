from .base import BaseAgent
from models import Order, OrderSide, OrderBookState
import random
from typing import Optional

class NoiseTraderAgent(BaseAgent):
    def __init__(self, activity_rate: float = 0.3):
        super().__init__("NoiseTrader")
        self.activity_rate = activity_rate

    def decide(self, price_history, current_price, orderbook_state) -> Optional[Order]:
        if random.random() > self.activity_rate:
            return None
            
        side = random.choice([OrderSide.BUY, OrderSide.SELL])
        # Unpredictable price within 0.5% of current price
        price_offset = random.uniform(-0.005, 0.005)
        target_price = current_price * (1 + price_offset)
        quantity = random.randint(1, 20)
        
        return self._create_order(side, target_price, quantity)
