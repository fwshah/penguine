import pandas as pd
import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier
 
st.title("Penguine Speicy Prediction ML app")
st.info("This is end-to-end Machine Learning App")
 
with st.expander("Data"):
 st.write("**Raw data**")
 df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
 df
 st.write("Input variables")
 x_raw = df.drop('species',axis=1)
 y_raw = df.species 
 y_raw

 st.write("Descriptive Statistics")
 des = df.describe()
 des
with st.expander("Data Visualization"):
  st.scatter_chart(data=df , x='bill_length_mm',y='body_mass_g',color='species')
  # fig = px.box(df, x='species', y='body_mass_g', color='species')
  # st.plotly_chart(fig)

 
with st.expander("Input data"):
  pass
 
with st.expander("Data Preperation"):
  pass
 
with st.sidebar:
  st.header("Input Variables")
  island = st.selectbox('Island',('Biscoe','Dream','Torgersen'))
  bill_length_mm = st.slider('Bill length (mm)',32.1,59.6,43.9)
  bill_depth_mm = st.slider('Bill depth (mm)',13.1,21.5,17.2)
  flipper_length_mm = st.slider('Flipper length (mm)',172.0,231.0,201.0)
  body_mass_g = st.slider('Body mass (g)',2700.0,6300.0,4207.0)
  gender = st.selectbox('Gender',('male','female'))
  data = {'island':island,
          'bill_depth_mm':bill_dpth_mm,
          'flipper_length_mm': flipper_length_mm,
          'gender': gender
  }
 input_off = pd.DataFrame(data, index[0])
input_penguins = pd.concat([input_df], x_raw], axis=0)
