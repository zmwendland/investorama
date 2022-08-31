# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:52:16 2022

@author: Zach
"""

import pandas as pd
import yfinance as yf
import datetime as dt
from datetime import  date, timedelta,time
from pandas_datareader import data as pdr
import matplotlib as mpl
from yahoo_fin import stock_info as si
import streamlit as st 

ticker = ''
    
yesterday = date.today() - timedelta(days=1)
yesterday.strftime('%m%d%y')


start = dt.datetime.now()


st.subheader('Single Stock Daily Performance')
stonkForm = st.form("Enter Ticker")
inputTicker = stonkForm.text_input('Ticker Symbol',value=ticker)
submit_button = stonkForm.form_submit_button("GO")
if submit_button:
    ticker = ticker
    name = stock_info.get_data(ticker)
    name = list(name['ticker'])
    name = name[0]
    stock = stock_info.get_live_price(ticker)
    stock = round(stock,2)
    last = stock_info.get_data(ticker,start_date=start)
    last = list(last['open'])
    change = stock/round(last[0],2)-1

else:
    st.subheader('Press GO')
