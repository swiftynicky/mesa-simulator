from typing import List
from models import Order, Trade, OrderSide
from orderbook import OrderBook
import uuid
from datetime import datetime

class MatchingEngine:
    def __init__(self, orderbook: OrderBook):
        self.orderbook = orderbook
        self.last_price: float = 100.0

    def process_order(self, order: Order) -> List[Trade]:
        trades = []
        
        if order.side == OrderSide.BUY:
            trades = self._match_buy(order)
        else:
            trades = self._match_sell(order)
            
        return trades

    def _match_buy(self, order: Order) -> List[Trade]:
        trades = []
        while order.quantity > 0 and self.orderbook.asks:
            best_ask = self.orderbook.asks[0]
            if order.price >= best_ask.price:
                # Match found
                qty = min(order.quantity, best_ask.quantity)
                
                trade = Trade(
                    id=f"T-{uuid.uuid4().hex[:6]}",
                    buyer_id=order.agent_id,
                    seller_id=best_ask.agent_id,
                    price=best_ask.price,
                    quantity=qty,
                    timestamp=datetime.now()
                )
                trades.append(trade)
                self.last_price = trade.price
                
                # Update quantities
                order.quantity -= qty
                best_ask.quantity -= qty
                
                if best_ask.quantity == 0:
                    self.orderbook.remove_order(best_ask.id)
            else:
                break
        
        if order.quantity > 0:
            self.orderbook.add_order(order)
            
        return trades

    def _match_sell(self, order: Order) -> List[Trade]:
        trades = []
        while order.quantity > 0 and self.orderbook.bids:
            best_bid = self.orderbook.bids[0]
            if order.price <= best_bid.price:
                # Match found
                qty = min(order.quantity, best_bid.quantity)
                
                trade = Trade(
                    id=f"T-{uuid.uuid4().hex[:6]}",
                    buyer_id=best_bid.agent_id,
                    seller_id=order.agent_id,
                    price=best_bid.price,
                    quantity=qty,
                    timestamp=datetime.now()
                )
                trades.append(trade)
                self.last_price = trade.price
                
                # Update quantities
                order.quantity -= qty
                best_bid.quantity -= qty
                
                if best_bid.quantity == 0:
                    self.orderbook.remove_order(best_bid.id)
            else:
                break
                
        if order.quantity > 0:
            self.orderbook.add_order(order)
            
        return trades
