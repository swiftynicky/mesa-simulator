# MESA: Multi-Agent Exchange Simulation Architecture

A real-time financial market simulator powered by agentic AI.

## 🚀 Quick Start

### 1. Start the Backend (Engine)
```bash
cd backend
venv\Scripts\activate   # On Windows
pip install -r requirements.txt
python main.py
```
*The engine will run at `http://localhost:8000`*

### 2. Start the Frontend (Dashboard)
```bash
cd frontend
npm install
npm run dev
```
*Open `http://localhost:3000` in your browser.*

## 🛠 Features
- **Price Discovery Engine**: Real-time matching engine using price-time priority.
- **Agentic Traders**:
  - **Noise Traders**: Provide random liquidity.
  - **Trend Followers**: Amplify market momentum.
  - **Mean Reversion**: Stabilize price action.
  - **Fundamentalists**: Anchor price to true value.
- **Dynamic Controls**: Add/remove agents on the fly to observe market impact.
- **Visual Analytics**: Professional candlesticks (lightweight-charts), order book depth, and trade feed.

## 🧠 Viva / Talking Points
- **Emergent Behavior**: Explain how random noise traders and trend followers can create "flash crashes" or bubbles.
- **Matching Engine**: Explain the use of sorted lists (bisect) for $O(\log n)$ order placement.
- **WebSocket Sync**: Real-time push of market state for zero-latency UI updates.
- **Zustand Management**: Centralized state for handling high-frequency market updates without React overhead.
