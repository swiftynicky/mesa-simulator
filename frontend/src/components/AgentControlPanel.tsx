"use client";

import React from 'react';
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Plus, Minus, Users } from "lucide-react";

interface AgentControlPanelProps {
  agents: Record<string, number>;
  onAdd: (type: string) => void;
  onRemove: (type: string) => void;
}

export function AgentControlPanel({ agents, onAdd, onRemove }: AgentControlPanelProps) {
  const agentTypes = [
    { id: "NoiseTrader", label: "Noise Traders", color: "bg-ghost", desc: "Random liquidity providers" },
    { id: "TrendFollower", label: "Trend Followers", color: "bg-cyan-500", desc: "Momentum amplifiers" },
    { id: "MeanReversion", label: "Mean Reversion", color: "bg-purple-500", desc: "Price stabilizers" },
    { id: "Fundamental", label: "Fundamentalists", color: "bg-orange-500", desc: "Value anchors" },
  ];

  return (
    <div className="flex flex-col gap-4">
      <div className="flex items-center gap-2 mb-2">
        <Users className="w-5 h-5 text-primary" />
        <h3 className="font-semibold text-sm uppercase tracking-wider">Agent Population</h3>
      </div>
      
      {agentTypes.map((agent) => (
        <div key={agent.id} className="glass-panel p-3 rounded-lg flex items-center justify-between group">
          <div className="flex flex-col">
            <div className="flex items-center gap-2">
              <span className="text-sm font-medium">{agent.label}</span>
              <Badge variant="secondary" className="bg-primary/10 text-primary border-primary/20">
                {agents[agent.id] || 0}
              </Badge>
            </div>
            <span className="text-[10px] text-muted-foreground">{agent.desc}</span>
          </div>
          
          <div className="flex items-center gap-1">
            <Button 
              size="icon" 
              variant="outline" 
              className="h-7 w-7 rounded-md hover:bg-red-500/20 hover:text-red-400 border-white/5"
              onClick={() => onRemove(agent.id)}
            >
              <Minus className="h-3 w-3" />
            </Button>
            <Button 
              size="icon" 
              variant="outline" 
              className="h-7 w-7 rounded-md hover:bg-primary/20 hover:text-primary border-white/5"
              onClick={() => onAdd(agent.id)}
            >
              <Plus className="h-3 w-3" />
            </Button>
          </div>
        </div>
      ))}
    </div>
  );
}
