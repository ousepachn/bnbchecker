
import streamlit as st
import pandas as pd
import numpy as np

data = [[-33.71205471, 29.19017682], [-33.81205471, 29.11017682], [-34.71205471, 29.49017682]]
df = pd.DataFrame(data, columns=['latitude', 'longitude'])

st.map(df)