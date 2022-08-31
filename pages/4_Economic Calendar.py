import requests as r 
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

url = 'https://www.marketwatch.com/economy-politics/calendar'
file = r.get(url)
soup = BeautifulSoup(file.text,'lxml')
cont = soup.find('tbody')
cont2 = soup.find('table')

header = []
for x in cont2.find_all('th'):
    y = x.text.strip()
    header.append(y)
    

days = []
for i in cont.find_all('b'):
    z = i.text.strip()
    days.append(z)

cal = pd.DataFrame(columns=header) 


for x in cont.find_all('tr'):
    data = x.find_all('td')
    row = [y.text for y in data]
    length = len(cal)
    cal.loc[length] = row

st.dataframe(cal)
