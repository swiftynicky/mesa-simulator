# MESA: Multi-Agent Exchange Simulation Architecture

[![Live Demo](https://img.shields.io/badge/Live-Demo-00C7B7?style=for-the-badge&logo=vercel)](https://mesa-simulator.vercel.app)
[![Backend API](https://img.shields.io/badge/API-Render-46E3B7?style=for-the-badge&logo=render)](https://mesa-simulator.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python)](https://python.org)
[![Next.js](https://img.shields.io/badge/Next.js-16-000000?style=flat-square&logo=next.js)](https://nextjs.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.128-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com)

> A real-time stock exchange simulator demonstrating emergent market dynamics through autonomous AI trading agents.

---

## Project Overview

MESA simulates a financial exchange where **four types of autonomous AI agents** compete and interact through a real order book and matching engine. The resulting price movements emerge naturally from the collective behavior of these agents—demonstrating key concepts in:

- **Multi-Agent Systems (MAS)**
- **Behavioral Finance**
- **Emergent Market Dynamics**
- **Real-Time Distributed Systems**

---

## Agent Types

| Agent | Strategy | Market Effect |
|-------|----------|---------------|
| **Noise Traders** | Random buy/sell decisions | Creates base liquidity and unpredictability |
| **Trend Followers** | Buy uptrends, sell downtrends | Amplifies momentum, creates bubbles/crashes |
| **Mean Reversion** | Sell highs, buy lows | Stabilizes price, fights extreme movements |
| **Fundamentalists** | Trade toward "true value" ($100) | Anchors price to fair value |

---

## Architecture

```
+------------------------------------------------------------------+
|                        FRONTEND (Next.js)                        |
|   +----------+  +----------+  +----------+  +----------+         |
|   |  Price   |  |  Order   |  |  Agent   |  |  Trade   |         |
|   |  Chart   |  |  Book    |  | Controls |  |  Feed    |         |
|   +----+-----+  +----+-----+  +----+-----+  +----+-----+         |
|        +-------------+-------------+-------------+                |
|                           | WebSocket                             |
+---------------------------+---------------------------------------+
                            |
+---------------------------+---------------------------------------+
|                        BACKEND (FastAPI)                          |
|   +----------------------------------------------------------+   |
|   |              Simulation Engine                            |   |
|   |  +-------------+  +-------------+  +-------------+        |   |
|   |  |  Matching   |  |   Order     |  |   Agent     |        |   |
|   |  |   Engine    |<-|    Book     |<-| Coordinator |        |   |
|   |  +-------------+  +-------------+  +-------------+        |   |
|   +----------------------------------------------------------+   |
+------------------------------------------------------------------+
```

---

## Live Demo

**Try it now:** [https://mesa-simulator.vercel.app](https://mesa-simulator.vercel.app)

---

## Local Development

### Prerequisites
- Python 3.9+
- Node.js 18+
- npm or yarn

### Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac
pip install -r requirements.txt
python main.py
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### One-Click Start (Windows)
```bash
START_MESA.bat
```

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | Next.js 16, React 19, TailwindCSS, Zustand |
| **Charting** | TradingView Lightweight Charts |
| **Backend** | FastAPI, Uvicorn, Python 3.11 |
| **Real-Time** | WebSockets (100ms tick rate) |
| **Deployment** | Vercel (Frontend), Render (Backend) |

---

## Key Features

- **Real Matching Engine**: Price-time priority order matching (same algorithm used by NYSE/NASDAQ)
- **Live Order Book**: Visualizes bid/ask depth in real-time
- **Dynamic Agent Control**: Add/remove agents mid-simulation
- **WebSocket Streaming**: Zero-latency UI updates at 100ms intervals
- **Emergent Behavior**: Complex market patterns arise from simple agent rules

---

## Academic Context

**Project Type:** B.Tech Minor Project  
**Domain:** Multi-Agent Systems, Computational Finance  

**Key Concepts Demonstrated:**
- Emergent behavior from heterogeneous agents
- Order book mechanics and price discovery
- Real-time event-driven architecture
- WebSocket-based state synchronization

---

## Project Structure

```
mesa-simulator/
├── backend/
│   ├── agents/           # Agent implementations
│   │   ├── noise_trader.py
│   │   ├── trend_follower.py
│   │   ├── mean_reversion.py
│   │   └── fundamental.py
│   ├── main.py           # FastAPI application
│   ├── simulation.py     # Core simulation engine
│   ├── matching.py       # Order matching engine
│   ├── orderbook.py      # Order book data structure
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── app/          # Next.js app router
│   │   ├── components/   # React components
│   │   ├── hooks/        # Custom hooks (WebSocket)
│   │   └── store/        # Zustand state management
│   └── package.json
├── START_MESA.bat        # Windows launcher
└── README.md
```

---

## Author

**Benson Muttath Benni**  
B.Tech Student  

---

## License

MIT License - Feel free to use for educational purposes.
