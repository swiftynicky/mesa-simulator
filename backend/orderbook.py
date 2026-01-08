from typing import List, Optional, Dict
from models import Order, OrderSide, OrderBookState
import bisect

class OrderBook:
    def __init__(self):
        self.bids: List[Order] = []  # Sorted descending by price
        self.asks: List[Order] = []  # Sorted ascending by price
        self.order_map: Dict[str, Order] = {}

    def add_order(self, order: Order):
        self.order_map[order.id] = order
        if order.side == OrderSide.BUY:
            # Insert maintaining descending order
            # We negate price to use bisect on descending list if we wanted, 
            # but simpler to just use a custom sort or binary search.
            # However, for simulation scale, bisect + insert is fine.
            # Using negative price for bids makes them sortable with bisect.
            prices = [-o.price for o in self.bids]
            idx = bisect.bisect_right(prices, -order.price)
            self.bids.insert(idx, order)
        else:
            # Insert maintaining ascending order
            prices = [o.price for o in self.asks]
            idx = bisect.bisect_right(prices, order.price)
            self.asks.insert(idx, order)

    def remove_order(self, order_id: str) -> Optional[Order]:
        if order_id not in self.order_map:
            return None
        
        order = self.order_map.pop(order_id)
        if order.side == OrderSide.BUY:
            self.bids = [o for o in self.bids if o.id != order_id]
        else:
            self.asks = [o for o in self.asks if o.id != order_id]
        return order

    def get_best_bid(self) -> Optional[Order]:
        return self.bids[0] if self.bids else None

    def get_best_ask(self) -> Optional[Order]:
        return self.asks[0] if self.asks else None

    def get_state(self, depth: int = 10) -> OrderBookState:
        # Aggregate bids
        bid_levels = {}
        for o in self.bids:
            bid_levels[o.price] = bid_levels.get(o.price, 0) + o.quantity
        
        sorted_bids = sorted([[p, q] for p, q in bid_levels.items()], reverse=True)[:depth]
        
        # Aggregate asks
        ask_levels = {}
        for o in self.asks:
            ask_levels[o.price] = ask_levels.get(o.price, 0) + o.quantity
            
        sorted_asks = sorted([[p, q] for p, q in ask_levels.items()])[:depth]
        
        best_bid = sorted_bids[0][0] if sorted_bids else 0.0
        best_ask = sorted_asks[0][0] if sorted_asks else 0.0
        
        spread = best_ask - best_bid if best_ask and best_bid else 0.0
        mid = (best_ask + best_bid) / 2 if best_ask and best_bid else (best_ask or best_bid or 0.0)
        
        return OrderBookState(
            bids=sorted_bids,
            asks=sorted_asks,
            spread=round(spread, 4),
            mid_price=round(mid, 4)
        )
