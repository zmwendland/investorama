import pandas as pd
import streamlit as st
from datetime import  date, timedelta
from yahoo_fin import stock_info 


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
ten_yr = stock_info.get_live_price('^tnx')

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

ten_yr_yst = stock_info.get_data('^tnx',start_date=yesterday.strftime('%m%d%y'), end_date=None,interval='1d')
ten_yesterday = pd.DataFrame(ten_yr_yst).reset_index()
ten_yst_final = ten_yesterday['open'][0]
ten_pct = str(round((ten_yr/ten_yst_final-1)*100,2))+'%'




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
    news related to global macroeconomic issues, as well as links
    to important financial websites and learning resourdes. The sidebar 
    contains a stock screener, correlation matrix tool, live major
    commodity quotes and stock quotes, and a stock specific data 
    tool.
    ### Key Quotes
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

col7,col8,col9 = st.columns(3)
col6.metric(label='',value=round(ten_yr,2),delta=ten_pct)

if mkt_time < '9:30AM' or mkt_time > '4:00PM':
    st.subheader('Futures')
    st.dataframe(futures)
else:
    st.dataframe(stock_info.get_day_gainers(20))

