import pandas as pd
import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.title("Penguine Specy Prediction ML app")
st.info("This is end-t-end MAchine Learning App")
with st.expander("Data"):
  pass
with st.expander("Data Visulization"):
    pass
with st.expander("input data"):
    pass
with st.expander("Data Preperation"):
    pass
with st.sidebar:
    pass
island = st.selectbox('Island',('Biscoe','Dream','Torgersen'))
bill_length_mm = st.slider('Bill length (mm)',42.1,59.6,43.9)
bill_depth = st.slider('Bill length (mm)',13.1,21.5,17.2)
flipper_length_mm = st.slider('flipper length (mm)',172.0,231.0,201.0)
body_mass_g = st.slider('body mass (mm)',2700.0,6300.0,4207.0)
gender = st.selecter("Gender,('Male','Female'))
