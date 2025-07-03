import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# -------------------------------------
# CONFIG
# -------------------------------------

API_KEY = ""
BASE_URL = "https://www.alphavantage.co/query"

# Define available currency pairs
available_pairs = [
    ("EUR", "USD"),
    ("GBP", "USD"),
    ("AUD", "USD"),
    ("USD", "JPY"),
    ("USD", "CAD"),
    ("USD", "CHF"),
]

# -------------------------------------
# PAGE SETTINGS
# -------------------------------------

st.set_page_config(page_title="Forex Trading Dashboard", layout="wide")

st.title("💹 Forex Trading Dashboard")

# -------------------------------------
# SIDEBAR - Controls
# -------------------------------------

st.sidebar.header("Select Options")

# Currency pair dropdown
pair = st.sidebar.selectbox(
    "Choose Currency Pair:",
    available_pairs,
    format_func=lambda x: f"{x[0]}/{x[1]}"
)

# Chart type dropdown
chart_type = st.sidebar.radio(
    "Chart Type:",
    ["Candlestick", "Line Chart"]
)

# Refresh interval
refresh_interval = st.sidebar.number_input(
    "Refresh interval (seconds):",
    min_value=0,
    max_value=3600,
    value=0,
    help="Set to 0 to disable auto-refresh."
)

# -------------------------------------
# DATA FETCH
# -------------------------------------

from_currency, to_currency = pair

params = {
    "function": "FX_DAILY",
    "from_symbol": from_currency,
    "to_symbol": to_currency,
    "apikey": API_KEY,
    "outputsize": "compact"
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    time_series = data.get("Time Series FX (Daily)", {})

    if time_series:
        df = pd.DataFrame.from_dict(time_series, orient="index")
        df = df.rename(columns={
            "1. open": "Open",
            "2. high": "High",
            "3. low": "Low",
            "4. close": "Close"
        })
        df.index = pd.to_datetime(df.index)
        df = df.sort_index()
        df = df.astype(float)

        # -------------------------------------
        # CHART RENDERING
        # -------------------------------------

        st.subheader(f"{from_currency}/{to_currency} Chart")

        if chart_type == "Candlestick":
            fig = go.Figure(data=[
                go.Candlestick(
                    x=df.index,
                    open=df["Open"],
                    high=df["High"],
                    low=df["Low"],
                    close=df["Close"],
                    increasing_line_color='green',
                    decreasing_line_color='red'
                )
            ])
            fig.update_layout(
                title=f"Candlestick Chart - {from_currency}/{to_currency}",
                xaxis_rangeslider_visible=False,
                height=600
            )
        else:
            fig = px.line(
                df,
                x=df.index,
                y="Close",
                title=f"Line Chart - {from_currency}/{to_currency}"
            )
            fig.update_traces(line=dict(width=2))
            fig.update_layout(height=600)

        st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("No data returned from API.")
else:
    st.error("API request failed.")

# -------------------------------------
# AUTO REFRESH
# -------------------------------------

if refresh_interval > 0:
    st.experimental_autorefresh(interval=refresh_interval * 1000, key="refresh")
