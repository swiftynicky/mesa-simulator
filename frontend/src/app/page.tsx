"use client";

import React, { useState } from 'react';
import { useWebSocket } from '@/hooks/useWebSocket';
import { useSimulationStore } from '@/store/useSimulationStore';
import { PriceChart } from '@/components/PriceChart';
import { OrderBookDepth } from '@/components/OrderBookDepth';
import { AgentControlPanel } from '@/components/AgentControlPanel';
import { TradeFeed } from '@/components/TradeFeed';
import { MarketMetrics } from '@/components/MarketMetrics';
import { Button } from '@/components/ui/button';
import { Play, Pause, RotateCcw, Activity } from 'lucide-react';

// Use environment variable for API URL, fallback to localhost for development
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
const WS_URL = process.env.NEXT_PUBLIC_WS_URL || 'ws://localhost:8000/ws';

export default function Dashboard() {
  const { state, isRunning, setRunning, reset } = useSimulationStore();
  
  // Initialize WebSocket connection
  useWebSocket(WS_URL);

  const handeStartStop = async () => {
    const endpoint = isRunning ? 'stop' : 'start';
    try {
      await fetch(`${API_URL}/simulation/${endpoint}`, { method: 'POST' });
      setRunning(!isRunning);
    } catch (error) {
      console.error("Failed to toggle simulation:", error);
    }
  };

  const handleReset = async () => {
    try {
      await fetch(`${API_URL}/simulation/reset`, { method: 'POST' });
      reset();
    } catch (error) {
      console.error("Failed to reset simulation:", error);
    }
  };

  const addAgent = async (type: string) => {
    try {
      await fetch(`${API_URL}/agents/add/${type}`, { method: 'POST' });
    } catch (error) {
      console.error("Failed to add agent:", error);
    }
  };

  const removeAgent = async (type: string) => {
    try {
      await fetch(`${API_URL}/agents/remove/${type}`, { method: 'POST' });
    } catch (error) {
      console.error("Failed to remove agent:", error);
    }
  };

  if (!state) return (
    <div className="min-h-screen bg-background flex flex-col items-center justify-center gap-4 text-cyan-400">
      <Activity className="w-12 h-12 animate-pulse" />
      <span className="font-mono text-xs uppercase tracking-[0.3em]">Connecting to MESA Engine...</span>
    </div>
  );

  return (
    <div className="min-h-screen bg-background text-foreground p-6 selection:bg-cyan-500/20">
      {/* Header */}
      <div className="max-w-[1600px] mx-auto mb-8 flex flex-col md:flex-row md:items-center justify-between gap-6">
        <div className="flex flex-col">
          <h1 className="text-3xl font-black tracking-tighter flex items-center gap-2">
            MESA <span className="text-primary text-sm font-light tracking-[0.5em] mt-2">SYSTEM</span>
          </h1>
          <p className="text-xs text-muted-foreground font-medium uppercase tracking-wider mt-1 opacity-60">
            Multi-Agent Exchange Simulation Architecture • Sol-1 Engine
          </p>
        </div>

        <div className="flex items-center gap-3">
          <Button 
            variant={isRunning ? "destructive" : "default"}
            className={`min-w-[140px] font-bold uppercase tracking-wider ${!isRunning && "bg-cyan-600 hover:bg-cyan-500 cyan-glow"}`}
            onClick={handeStartStop}
          >
            {isRunning ? (
              <><Pause className="mr-2 h-4 w-4" /> Pause Simulation</>
            ) : (
              <><Play className="mr-2 h-4 w-4" /> Start Market</>
            )}
          </Button>
          <Button 
            variant="outline" 
            size="icon" 
            className="border-white/5 hover:bg-background/80"
            onClick={handleReset}
          >
            <RotateCcw className="h-4 w-4" />
          </Button>
        </div>
      </div>

      <div className="max-w-[1600px] mx-auto grid grid-cols-12 gap-6">
        {/* TopRow: Metrics */}
        <div className="col-span-12">
          <MarketMetrics metrics={state.metrics} lastPrice={state.last_price} tick={state.tick} />
        </div>

        {/* Main Column: Chart & Depth */}
        <div className="col-span-12 lg:col-span-8 flex flex-col gap-6">
          <div className="glass-panel p-6 rounded-2xl border-white/5 bg-black/20">
             <div className="flex items-center justify-between mb-6">
                <h3 className="text-sm font-bold uppercase tracking-widest text-white/40">Market Discovery Chart</h3>
                <div className="flex items-center gap-4 text-[10px] font-mono opacity-50">
                   <div className="flex items-center gap-2">
                     <div className="w-2 h-2 rounded-full bg-cyan-500" />
                     <span>PRICE DISCOVERY</span>
                   </div>
                </div>
             </div>
             <PriceChart data={state.price_history} />
          </div>

          <div className="glass-panel p-6 rounded-2xl border-white/5 bg-black/20">
             <h3 className="text-sm font-bold uppercase tracking-widest text-white/40 mb-6">Order Book Depth</h3>
             <OrderBookDepth bids={state.orderbook.bids} asks={state.orderbook.asks} />
          </div>
        </div>

        {/* Sidebar: Agents & Feed */}
        <div className="col-span-12 lg:col-span-4 flex flex-col gap-6">
          <div className="glass-panel p-6 rounded-2xl border-white/5 flex-none h-fit">
            <AgentControlPanel 
              agents={state.agents} 
              onAdd={addAgent} 
              onRemove={removeAgent} 
            />
          </div>

          <div className="glass-panel p-6 rounded-2xl border-white/5 flex-grow overflow-hidden h-[500px]">
            <TradeFeed trades={state.recent_trades} />
          </div>
        </div>
      </div>
      
      {/* Footer Decoration */}
      <div className="mt-12 text-center opacity-20 text-[10px] font-mono uppercase tracking-[1em] max-w-[1600px] mx-auto">
        Distributed Agentic Intelligence • Institutional Architecture • 2026.01.07
      </div>
    </div>
  );
}
