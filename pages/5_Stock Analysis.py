# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:52:16 2022

@author: Zach
"""

import pandas as pd
# import yfinance as yf
import datetime as dt
from datetime import  date, timedelta
# import matplotlib as mpl
from yahoo_fin import stock_info
import streamlit as st

symbols = pd.read_csv('pages/Datasets/symbols.csv')
tickers = symbols['Ticker'].sort_values().tolist() 
ticker = st.sidebar.selectbox('Choose a stock',tickers)
    
yesterday = date.today() - timedelta(days=1)
yesterday.strftime('%m%d%y')

st.subheader('Single Stock Daily Performance')

while stock_info.get_market_status() == 'REGULAR':
    if ticker:
        start = dt.datetime.now()
        name = stock_info.get_data(ticker)
        name = list(name['ticker'])
        name = name[0]
        stock = stock_info.get_live_price(ticker)
        stock = round(stock,2)
        last = stock_info.get_data(ticker,start_date=start)
        last = list(last['open'])
        change = stock/round(last[0],2)-1
        change = round(change,2)
        change = str(change)+'%'
        st.subheader(name)
        st.metric(label='',value=stock,delta=change)
else:
        start = dt.datetime.now()
        name = stock_info.get_data(ticker)
        name = list(name['ticker'])
        name = name[0]
        stock = stock_info.get_postmarket_price(ticker)
        stock = round(stock,2)
        last = stock_info.get_data(ticker,start_date=start)
        last = list(last['close'])
        last = last[0]
        last = round(last,2)
        change = stock/last-1
        change = round(change,2)
        change = str(change)+'%'
        st.subheader(name+' **Market Closed**')
        st.metric(label='',value=stock,delta=change)
