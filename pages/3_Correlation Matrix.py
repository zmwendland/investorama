# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 20:40:57 2022

@author: Zach
"""

import pandas as pd
import numpy as np
import pandas_datareader as web
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn
import streamlit as st

start = datetime(2021,1,1)
stocks = [stonk,'SPY','QQQ','^RUT','GC=F','CL=F','^TNX', 'DX=F',
          'BTC-USD','EURUSD=X','USDJPY=X']

stocks_data = []
s2_price = []

for stock in stocks:
    r = web.DataReader(stock,'yahoo',start)
    r['stock'] = stock
    stocks_data.append(r)
    
df = pd.concat(stocks_data)
df = df.reset_index()
df = df[['Date','stock','Close']]

df_piv = df.pivot('Date','stock','Close').reset_index()
corr_df = df_piv.corr(method='pearson')
corr_df.head().reset_index()

mask = np.zeros_like(corr_df)
mask[np.triu_indices_from(mask)] = True

#generate plot
def heatmaps():
    x = seaborn.heatmap(corr_df, cmap='RdYlGn', vmax=1.0, vmin=-1.0 , mask = mask, linewidths=2.5)
    x.plt.title('Correlation 2021-Present')
    x.plt.yticks(rotation=0) 
    x.plt.xticks(rotation=90) 
    return x
stonksForm = st.form('Enter Ticker Symbol to Correlate')
stonk = stonksForm.text_input('Symbol','AAPL')
submit_button = stonksForm.form_submit_button('Correlate!')
if submit_button:
    st.write(heatmaps())
    