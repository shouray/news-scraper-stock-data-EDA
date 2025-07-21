import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/raw/stock_data.csv', parse_dates=['Date'])
df.set_index('Date', inplace=True)

# Sidebar
st.sidebar.title("Yahoo Finance News & Stock Explorer")
tickers = [col.split('_')[0] for col in df.columns if '_Close' in col]
selected_ticker = st.sidebar.selectbox("Select a ticker", list(set(tickers)))

# Show line chart for closing price
st.header(f"Closing Price for {selected_ticker}")
st.line_chart(df[f"{selected_ticker}_Close"])

# Show volume chart
st.header(f"Trading Volume for {selected_ticker}")
st.bar_chart(df[f"{selected_ticker}_Volume"])

# (Optional) Display data
if st.checkbox("Show raw data"):
    st.write(df[[f"{selected_ticker}_Close", f"{selected_ticker}_Volume"]])
