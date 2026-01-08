"use client";

import React from 'react';
import { ScrollArea } from "@/components/ui/scroll-area";
import { Badge } from "@/components/ui/badge";
import { Trade } from '@/store/useSimulationStore';
import { AnimatePresence, motion } from 'framer-motion';

interface TradeFeedProps {
  trades: Trade[];
}

export function TradeFeed({ trades }: TradeFeedProps) {
  return (
    <div className="flex flex-col h-full overflow-hidden">
      <div className="flex items-center justify-between mb-4 px-2">
        <h3 className="font-semibold text-sm uppercase tracking-wider">Live Trades</h3>
        <Badge variant="outline" className="text-[10px] opacity-50 border-white/10 uppercase">
          Real-time
        </Badge>
      </div>

      <ScrollArea className="flex-1 -mx-2 px-2">
        <div className="flex flex-col gap-2">
          <AnimatePresence initial={false}>
            {trades.slice().reverse().map((trade) => (
              <motion.div
                key={trade.id}
                initial={{ opacity: 0, x: -10, height: 0 }}
                animate={{ opacity: 1, x: 0, height: 'auto' }}
                exit={{ opacity: 0 }}
                className="flex items-center justify-between p-2 rounded-md bg-white/[0.02] border border-white/[0.05] hover:bg-white/[0.04] transition-colors"
              >
                <div className="flex flex-col">
                  <span className="text-[10px] text-muted-foreground font-mono">
                    {trade.id.slice(-4).toUpperCase()}
                  </span>
                  <div className="flex items-center gap-1">
                     <span className="text-xs font-bold text-cyan-400">${trade.price.toFixed(2)}</span>
                  </div>
                </div>
                
                <div className="flex flex-col items-end">
                   <span className="text-[10px] text-white/50">{trade.quantity} SH</span>
                   <span className="text-[8px] text-muted-foreground uppercase">
                     {new Date(trade.timestamp).toLocaleTimeString([], { hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' })}
                   </span>
                </div>
              </motion.div>
            ))}
          </AnimatePresence>
          {trades.length === 0 && (
            <div className="text-center py-10 text-muted-foreground text-xs italic">
              Waiting for trades...
            </div>
          )}
        </div>
      </ScrollArea>
    </div>
  );
}
