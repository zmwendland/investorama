import yfinance as yf
import pandas as pd
import streamlit as st
import pandas_datareader as web 
from datetime import datetime
from yahoo_fin import stock_info 

st.set_page_config(
    page_title="Investorama",
    page_icon="📈",
)


st.sidebar.success('Navigation')

starts = datetime.today()
spx = stock_info.get_live_price('^gspc')
dow = stock_info.get_live_price



st.title('Welcome to Investorama!')

st.markdown(
    """
    Investorama is a personal project designed to provide
    stock market data & information. The home page includes daily
    news related to global macroeconomic issues, as well as links
    to important financial websites and learning resourdes. The sidebar 
    contains a stock screener, correlation matrix tool, live major
    commodity quotes and stock quotes, and a stock specific data 
    tool.
    ### Global Financial News
    """
    )
st.caption(spx)
st.markdown(
    """
    ### Financial Websites
    """
    )

st.markdown(
    """
    ### Learning Resources
    """
    )
