import pandas as pd
import streamlit as st
from datetime import datetime, date, timedelta
from yahoo_fin import stock_info 
import yahoo_fin as yf

st.set_page_config(
    page_title="Investorama",
    page_icon="📈",
)


st.sidebar.success('Navigation')

yesterday = date.today() - timedelta(days=1)
yesterday.strftime('%m%d%y')


spx = stock_info.get_live_price('^gspc')
dow = stock_info.get_live_price('^dji')
qqq = stock_info.get_live_price('^ixic')

spx_yst = stock_info.get_data('^gspc',start_date=yesterday.strftime('%m%d%y'), end_date=None,interval='1d')
spx_yesterday = pd.DataFrame(spx_yst).reset_index()
spx_yst_final = spx_yesterday['open'][0]
spx_pct = str(round((spx/spx_yst_final-1)*100,2))+'%'

dow_yst = stock_info.get_data('^dji',start_date=yesterday.strftime('%m%d%y'), end_date=None,interval='1d')
dow_yesterday = pd.DataFrame(dow_yst).reset_index()
dow_yst_final = dow_yesterday['open'][0]
dow_pct = str(round((dow/dow_yst_final-1)*100,2))+'%'

qqq_yst = stock_info.get_data('^ixic',start_date=yesterday.strftime('%m%d%y'), end_date=None,interval='1d')
qqq_yesterday = pd.DataFrame(qqq_yst).reset_index()
qqq_yst_final = qqq_yesterday['open'][0]
qqq_pct = str(round((qqq/qqq_yst_final-1)*100,2))+'%'

futures = stock_info.get_futures()
futures.reset_index()
futures = futures[0:8]
# futures.rename(columns={'Unnamed: 7':'Volume'})
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
    ### Major Quotes
    """
    )
col_1,col_2,col_3 = st.columns(3)
col_1.subheader('**S&P 500**')
col_2.subheader('**DOW**')
col_3.subheader('**Nasdaq**')

col4,col5,col6 = st.columns(3)
col4.metric(label='',value=round(spx,2),delta=spx_pct)
col5.metric(label='',value=round(dow,2),delta=dow_pct)
col6.metric(label='',value=round(qqq,2),delta=qqq_pct)
st.subheader('Futures')
st.dataframe(futures)

