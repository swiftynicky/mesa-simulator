"use client";

import React from 'react';
import { Card } from "@/components/ui/card";
import { Activity, BarChart3, TrendingUp, Zap } from "lucide-react";

interface MarketMetricsProps {
  metrics: {
    volatility: number;
    volume: number;
  };
  lastPrice: number;
  tick: number;
}

export function MarketMetrics({ metrics, lastPrice, tick }: MarketMetricsProps) {
  const items = [
    { label: "Price", value: `$${lastPrice.toFixed(2)}`, icon: TrendingUp, color: "text-cyan-400" },
    { label: "Volatility", value: `${(metrics.volatility * 100).toFixed(2)}%`, icon: Activity, color: "text-purple-400" },
    { label: "Volume (Tick)", value: metrics.volume.toLocaleString(), icon: BarChart3, color: "text-emerald-400" },
    { label: "Current Tick", value: tick.toString(), icon: Zap, color: "text-amber-400" },
  ];

  return (
    <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
      {items.map((item) => (
        <Card key={item.label} className="glass-panel p-4 rounded-xl flex items-center gap-4 transition-all duration-300 hover:cyan-glow border-white/5">
          <div className={`p-2 rounded-lg bg-background/50 ${item.color}`}>
            <item.icon className="w-5 h-5" />
          </div>
          <div className="flex flex-col">
            <span className="text-[10px] text-muted-foreground uppercase tracking-wider font-bold">{item.label}</span>
            <span className="text-lg font-bold font-mono tracking-tight">{item.value}</span>
          </div>
        </Card>
      ))}
    </div>
  );
}
