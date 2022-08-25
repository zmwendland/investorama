# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 02:50:02 2022

@author: Zach
"""

import investpy as ip
from datetime import timedelta
from datetime import datetime as dt
import pandas as pd
import streamlit as st

st.subheader('USA Economic Calendar')
st.markdown('Dates are dd/mm/yyyy.')

start = dt.now()
start2 = start.strftime('%d/%m/%Y')
end = dt.now() + timedelta(days=14)
end2 = end.strftime('%d/%m/%Y')

data = ip.economic_calendar(from_date=start2,to_date=end2)

df = pd.DataFrame(data)
df = df.drop(columns=['id'])
df['zone'] = [x.title() for x in df['zone']]
df['date'] = end.strftime('%m-%d-%Y')
df = df.loc[df['zone']=='United States']
df = df.sort_values(by=['zone','date'])
st.write(df)


