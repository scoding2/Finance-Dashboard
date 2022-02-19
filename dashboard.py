import pandas as pd
import streamlit as st
import yfinance as yf


st.title('Stock & Crypto Dashboard')

# Stock and Crypto Signs
tickers = ('TSLA', 'GOOG', 'AAPL', 'MSFT', 'LCID', 'BB', 'FB', 'WMT', 'AMZN')
crypto = ('BTC-USD', 'ETH-USD', 'DOGE-USD', 'SHIB-USD', 'ADAUSD')

# Dropdown Menu
dropdown = st.multiselect('Pick your Stock Asset', tickers)
dropdown_crypto = st.multiselect('Pick your Crypto Asset', crypto)

# Dropdown Menu(Dates)
start = st.date_input('Start Date', value = pd.to_datetime('2021-01-01'))
end = st.date_input('End Date', value = pd.to_datetime('today'))


if len(dropdown_crypto) > 0:
    df = yf.download(dropdown_crypto,start,end)['Adj Close']
    st.header('Return of {}'.format(dropdown_crypto))
    st.line_chart(df)

if len(dropdown) > 0:
    df = yf.download(dropdown,start,end)['Adj Close']
    st.header('Return of {}'.format(dropdown))
    st.line_chart(df)
