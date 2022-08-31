import pandas as pd
import streamlit as st
from datetime import  date, timedelta
from yahoo_fin import stock_info 
import streamlit.components.v1 as components

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
ten_yr = round(stock_info.get_live_price('^tnx'),2)
gold = stock_info.get_live_price('GC=F')
oil = stock_info.get_live_price('CL=F')

spx_yst = stock_info.get_data('^gspc',start_date=yesterday.strftime('%m%d%y'), end_date=None,interval='1d')
spx_yesterday = pd.DataFrame(spx_yst).reset_index()
spx_yst_final = spx_yesterday['close'][0]
spx_pct = str(round((spx/spx_yst_final-1)*100,2))+'%'

dow_yst = stock_info.get_data('^dji',start_date=yesterday.strftime('%m%d%y'), end_date=None,interval='1d')
dow_yesterday = pd.DataFrame(dow_yst).reset_index()
dow_yst_final = dow_yesterday['close'][0]
dow_pct = str(round((dow/dow_yst_final-1)*100,2))+'%'

qqq_yst = stock_info.get_data('^ixic',start_date=yesterday.strftime('%m%d%y'), end_date=None,interval='1d')
qqq_yesterday = pd.DataFrame(qqq_yst).reset_index()
qqq_yst_final = qqq_yesterday['close'][0]
qqq_pct = str(round((qqq/qqq_yst_final-1)*100,2))+'%'

ten_yr_yst = stock_info.get_data('^tnx',start_date=yesterday.strftime('%m%d%y'), end_date=None,interval='1d')
ten_yesterday = pd.DataFrame(ten_yr_yst).reset_index()
ten_yst_final = ten_yesterday['close'][0]
ten_yst_price = str(ten_yr)+'%'
ten_pct = str(round((ten_yr/ten_yst_final-1)*100,2))+'%'

gold_yst = stock_info.get_data('GC=F',start_date=yesterday.strftime('%m%d%y'), end_date=None,interval='1d')
gold_yesterday = pd.DataFrame(gold_yst).reset_index()
gold_yst_final = gold_yesterday['close'][0]
gold_pct = str(round((gold/gold_yst_final-1)*100,2))+'%'

oil_yst = stock_info.get_data('CL=F',start_date=yesterday.strftime('%m%d%y'), end_date=None,interval='1d')
oil_yesterday = pd.DataFrame(oil_yst).reset_index()
oil_yst_final = oil_yesterday['close'][0]
oil_pct = str(round((oil/oil_yst_final-1)*100,2))+'%'

futures = stock_info.get_futures()
futures.reset_index()
futures = futures[0:8]

mkt_time = str(futures['Market Time'][0])
# mkt_time = mkt_time.replace('AM','')
# mkt_time = mkt_time.replace('PM', '')
mkt_time = mkt_time.replace('EDT', '')
# futures.rename(columns={'Unnamed: 7':'Volume'})
st.title('Welcome to Investorama!')

st.markdown(
    """
    Investorama is a personal project designed to provide
    stock market data & information. The home page includes daily
    live US index quotes as well as futures quotes. The sidebar 
    contains a stock screener, correlation matrix tool, and a
    company specific data analysis tool.
    ### Key Quotes
    """
    )

col4,col5,col6 = st.columns(3)
col4.subheader('**S&P 500**')
col4.metric(label='',value=round(spx,2),delta=spx_pct)
col5.subheader('**DOW**')
col5.metric(label='',value=round(dow,2),delta=dow_pct)
col6.subheader('**Nasdaq**')
col6.metric(label='',value=round(qqq,2),delta=qqq_pct)

col7,col8,col9 = st.columns(3)
col7.subheader('**US 10-Year Bond**')
col7.metric(label='',value=ten_yst_price,delta=ten_pct)
col8.subheader('**Gold**')
col8.metric(label='',value=round(gold,2),delta=gold_pct)
col9.subheader('**WTI Crude Oil**')
col9.metric(label='',value=round(oil,2),delta=oil_pct)

st.subheader('Futures')
st.table(futures)
st.subheader('Top 20 Gainers')
st.table(stock_info.get_day_gainers(20))
st.subheader('Top 20 losers')
st.table(stock_info.get_day_losers(20))
# st.subheader('Top 20 Most Active')
# st.dataframe(stock_info.get_day_most_active(20))
