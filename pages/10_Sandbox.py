import pandas as pd
import streamlit as st
from datetime import  date, timedelta
import datetime as dt 
from yahoo_fin import stock_info 
import streamlit.components.v1 as components
from PIL import Image
import urllib.request as ur


ur.urlretrieve('https://imageio.forbes.com/specials-images/imageserve/627d3f18f0d6a392185ca2de/Stock-Market-Crash-2020/0x0.jpg?crop=3386,1905,x0,y82,safe&height=400&width=711&fit=bounds'
               ,"inv.png")
img_1 = Image.open('inv.png')
st.image(img_1)
