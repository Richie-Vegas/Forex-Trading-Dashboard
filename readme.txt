Forex Trading Dashboard
A Streamlit web app replicating core functionality of platforms like TradingView, tailored for Forex trading.

✅ Interactive charts (candlestick + line)
✅ Dropdown selection for currency pairs
✅ Auto-refresh option for live updates
✅ Clean, responsive UI
✅ Built entirely in Python

🚀 Demo
Here’s what it looks like:

Interactive candlestick or line charts

Zoom, pan, hover tooltips

Easy switching between different currency pairs

Automatic refresh for near-live dashboards

⚠️ Note: The free Alpha Vantage API provides daily forex data only. For real-time streaming candles, use a premium API or different data provider.

💻 Features
✅ Currency Pair Selection
Easily choose among major forex pairs like:

EUR/USD

GBP/USD

AUD/USD

USD/JPY

USD/CAD

USD/CHF

✅ Chart Type
Candlestick chart (OHLC)

Line chart (close prices)

Switch instantly between chart types via the sidebar.

✅ TradingView-Like Tools
Interactive Plotly graphs:

Zoom

Pan

Reset view

Save chart as PNG

Hover over candles or lines to view:

Open

High

Low

Close

Dates

✅ Auto-Refresh
Optional auto-refresh interval

Simulates live updating charts for active monitoring

🛠️ How It Works
🔗 Data Source
We use the Alpha Vantage API with:

Endpoint: FX_DAILY

Returns daily OHLC forex data

Free plan limited to ~5 requests/minute

🐍 Python Stack
Streamlit → UI + Web Server

Plotly → Charts (candlestick, line)

Pandas → Data cleaning + manipulation

Requests → API calls