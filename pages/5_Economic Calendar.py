
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


countries = list(df.zone.unique())
countries = [x.title() for x in countries]
countries.sort()

countryForm = st.form('Choose Country')
box = st.selectbox('Choose Country',options=countries)
submit = countryForm.form_submit_button("Go")

if submit:
    new_df = df[df['zone']==box]
    st.write(df.head(14))
