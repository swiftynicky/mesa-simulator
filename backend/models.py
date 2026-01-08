from pydantic import BaseModel
from enum import Enum
from datetime import datetime
from typing import Optional, List, Dict

class OrderSide(str, Enum):
    BUY = "BUY"
    SELL = "SELL"

class Order(BaseModel):
    id: str
    agent_id: str
    side: OrderSide
    price: float
    quantity: int
    timestamp: datetime = datetime.now()

class Trade(BaseModel):
    id: str
    buyer_id: str
    seller_id: str
    price: float
    quantity: int
    timestamp: datetime = datetime.now()

class OrderBookState(BaseModel):
    bids: List[List[float]]  # [[price, qty], ...]
    asks: List[List[float]]  # [[price, qty], ...]
    spread: float
    mid_price: float

class MarketState(BaseModel):
    tick: int
    last_price: float
    orderbook: OrderBookState
    recent_trades: List[Trade]
    price_history: List[float]
    agents: Dict[str, int]  # {agent_type: count}
    metrics: Dict[str, float]  # volatility, volume, etc.
