import { useEffect, useRef } from 'react';
import { useSimulationStore, MarketState } from '@/store/useSimulationStore';

export function useWebSocket(url: string) {
  const socketRef = useRef<WebSocket | null>(null);
  const setMarketState = useSimulationStore((state) => state.setMarketState);
  
  useEffect(() => {
    const socket = new WebSocket(url);
    socketRef.current = socket;

    socket.onmessage = (event) => {
      try {
        const data: MarketState = JSON.parse(event.data);
        setMarketState(data);
      } catch (error) {
        console.error("Failed to parse market state:", error);
      }
    };

    socket.onopen = () => {
      console.log("WebSocket Connected");
    };

    socket.onclose = () => {
      console.log("WebSocket Disconnected");
    };

    return () => {
      socket.close();
    };
  }, [url, setMarketState]);

  return socketRef.current;
}
