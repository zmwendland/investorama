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

st.subheader('Economic Calendar')
st.markdown('Dates are dd/mm/yyyy.')

countries = list(['United States','Germany','Canada','Japan','Taiwan',
                  'Euro Zone','United Kingdom','France','South Korea'])

start = dt.now()
start2 = start.strftime('%d/%m/%Y')
end = dt.now() + timedelta(days=14)
end2 = end.strftime('%d/%m/%Y')

data = ip.economic_calendar(from_date=start2,to_date=end2)

df = pd.DataFrame(data)
df = df.drop(columns=['id'])
df['zone'] = [x.title() for x in df['zone']]
df = df.loc[df['zone'].isin(['United States','Germany','Canada','Japan','Taiwan',
                              'Euro Zone','United Kingdom','France','South Korea'])]
df = df.sort_values(by=['zone','date'])

choice = st.radio('Choose an Info Type',
         ('All','USA','Specific Country'))


if (choice=='All'):
    st.write(df)
elif (choice=='USA'):
    countries = [x.title() for x in countries]
    countries.sort()    
    if submit:
        start = dt.now()
        start2 = start.strftime('%d/%m/%Y')
        end = dt.now() + timedelta(days=14)
        end2 = end.strftime('%d/%m/%Y')
        
        data = ip.economic_calendar(from_date=str(start2),to_date=str(end2))
        
        df = pd.DataFrame(data)
        df = df.drop(columns=['id'])
        df['zone'] = [x.title() for x in df['zone']]
        df = df.loc[df['zone'].isin(['United States'])]
        df['date'] = [x.strftime('%m/%d/%Y') for x in df['date']]
        df = df.loc[df['zone'].isin([box])]
        df = df.sort_values(by=['zone','date'])
        st.write(df)

else:
    countries = [x.title() for x in countries]
    countries.sort()    
    box = st.selectbox('Choose Country',options=countries)
    countryForm = st.form('Choose Country')
    submit = countryForm.form_submit_button("Go")
    if submit:
        
        start = dt.now()
        start2 = start.strftime('%d/%m/%Y')
        end = dt.now() + timedelta(days=14)
        end2 = end.strftime('%d/%m/%Y')
        
        data = ip.economic_calendar(from_date=str(start2),to_date=str(end2))
        
        df = pd.DataFrame(data)
        df = df.drop(columns=['id'])
        df['zone'] = [x.title() for x in df['zone']]
        df['date'] = [x.strftime('%m/%d/%Y') for x in df['date']]
        df = df.loc[df['zone'].isin([box])]
        df = df.sort_values(by=['zone','date'])
        
        st.write(df)


