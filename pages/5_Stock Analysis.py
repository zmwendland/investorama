import cufflinks as cf
import yfinance as yf
import warnings
from datetime import datetime as dt

warnings.filterwarnings("ignore")

cf.set_config_file(theme='pearl', world_readable=False)
cf.go_offline()

start = '2021-01-01'
end = dt.today()

stockForm = st.form('Input Ticker')
inputTicker = stockForm.text_input(label='Enter Ticker',value='aapl')
submitbutton = stockForm.form_submit_button('Go')
if submitbutton:
    stock = yf.download(inputTicker, start,end)
    close = stock['Close']

    stock['Close'].iplot(title='Stock Price Chart',colors=['red'])

    stock['Close'].iplot(title='Returns',bestfit=True, bestfit_colors=['blue'])

    qf=cf.QuantFig(stock,title='First Quant Figure',legend='top',name='GS')
    qf.add_sma([10,20],width=2,color=['green','lightgreen'],legendgroup=True)
    qf.add_bollinger_bands()
    qf.add_volume()
    qf.iplot()
