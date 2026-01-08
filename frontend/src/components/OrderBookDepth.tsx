"use client";

import React from 'react';

interface OrderBookDepthProps {
  bids: [number, number][];
  asks: [number, number][];
}

export function OrderBookDepth({ bids, asks }: OrderBookDepthProps) {
  const maxQty = Math.max(
    ...bids.map(b => b[1]),
    ...asks.map(a => a[1]),
    1
  );

  return (
    <div className="grid grid-cols-2 gap-4 font-mono text-xs">
      {/* Bids Column */}
      <div className="flex flex-col gap-1">
        <div className="flex justify-between text-muted-foreground px-2">
          <span>QTY</span>
          <span>BID</span>
        </div>
        {bids.map(([price, qty], i) => (
          <div key={`bid-${i}`} className="relative h-6 flex items-center justify-end px-2 group">
            <div 
              className="absolute right-0 top-0 bottom-0 bg-green-500/10 transition-all duration-300"
              style={{ width: `${(qty / maxQty) * 100}%` }}
            />
            <span className="z-10 text-muted-foreground mr-auto">{qty}</span>
            <span className="z-10 text-green-400 font-bold group-hover:scale-110 transition-transform cursor-default">
              {price.toFixed(2)}
            </span>
          </div>
        ))}
      </div>

      {/* Asks Column */}
      <div className="flex flex-col gap-1">
        <div className="flex justify-between text-muted-foreground px-2">
          <span>ASK</span>
          <span>QTY</span>
        </div>
        {asks.map(([price, qty], i) => (
          <div key={`ask-${i}`} className="relative h-6 flex items-center justify-start px-2 group">
            <div 
              className="absolute left-0 top-0 bottom-0 bg-red-500/10 transition-all duration-300"
              style={{ width: `${(qty / maxQty) * 100}%` }}
            />
            <span className="z-10 text-red-400 font-bold group-hover:scale-110 transition-transform cursor-default">
              {price.toFixed(2)}
            </span>
            <span className="z-10 text-muted-foreground ml-auto">{qty}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
