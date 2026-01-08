from .base import BaseAgent
from models import Order, OrderSide, OrderBookState
import random
from typing import Optional

class NoiseTraderAgent(BaseAgent):
    def __init__(self, activity_rate: float = 0.5):  # Increased from 0.3
        super().__init__("NoiseTrader")
        self.activity_rate = activity_rate

    def decide(self, price_history, current_price, orderbook_state) -> Optional[Order]:
        if random.random() > self.activity_rate:
            return None
            
        side = random.choice([OrderSide.BUY, OrderSide.SELL])
        # Wider price range for more volatility (1% instead of 0.5%)
        price_offset = random.uniform(-0.01, 0.01)
        target_price = current_price * (1 + price_offset)
        quantity = random.randint(5, 30)
        
        return self._create_order(side, target_price, quantity)
