import { create } from 'zustand';

export interface Trade {
  id: string;
  buyer_id: string;
  seller_id: string;
  price: number;
  quantity: number;
  timestamp: string;
}

export interface OrderBookState {
  bids: [number, number][];
  asks: [number, number][];
  spread: number;
  mid_price: number;
}

export interface MarketState {
  tick: number;
  last_price: number;
  orderbook: OrderBookState;
  recent_trades: Trade[];
  price_history: number[];
  agents: Record<string, number>;
  metrics: {
    volatility: number;
    volume: number;
  };
}

interface SimulationStore {
  state: MarketState | null;
  isRunning: boolean;
  setMarketState: (state: MarketState) => void;
  setRunning: (running: boolean) => void;
  reset: () => void;
}

const initialMarketState: MarketState = {
  tick: 0,
  last_price: 100.0,
  orderbook: { bids: [], asks: [], spread: 0, mid_price: 100.0 },
  recent_trades: [],
  price_history: [100.0],
  agents: {},
  metrics: { volatility: 0, volume: 0 }
};

export const useSimulationStore = create<SimulationStore>((set) => ({
  state: initialMarketState,
  isRunning: false,
  setMarketState: (state) => set({ state }),
  setRunning: (running) => set({ isRunning: running }),
  reset: () => set({ state: initialMarketState, isRunning: false }),
}));
