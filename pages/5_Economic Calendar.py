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

start = dt.now()
start = start.strftime('%d/%m/%Y')
end = dt.now() + timedelta(days=365)
end = end.strftime('%d/%m/%Y')

data = ip.economic_calendar(from_date=str(start),to_date=str(end))

df = pd.DataFrame(data)
df.drop(columns=['id'])

choice = st.radio('Choose an Info Type',
         ('All','Specific Country'))

if (choice=='All'):
    st.dataframe(df.head(14))
else:
    st.subheader('Under Construction')
    countries = list(df.zone.unique())
    countries = [x.title() for x in countries]
    countries.sort()    
    box = st.selectbox('Choose Country',options=countries)
    countryForm = st.form('Choose Country')
    submit = countryForm.form_submit_button("Go")
