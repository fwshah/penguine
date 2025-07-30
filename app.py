import pandas as pd

import streamlit as st

import numpy as np

from sklearn.ensemble import RandomForestClassifier

import matplotlib.pyplot as plt

import seaborn as sns

st.title("Penguine Speicy Prediction ML app")

st.info("This is end-to-end Machine Learning App")

with st.expander("Data"):

  st.write("*Raw Data*")

  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")

  df
  st.write("Input Vriables")
  X_raw = df.drop("species", axis = 1)
  X_raw
 
  st.write("Target Variable")
  y_raw = df.species
  y_raw
 
  st.write("Descriptive Statistics")
  des = df.describe()
  des  

with st.expander("Data Visualization"):
  st.write("Count of Penguin Species")
  fig, ax = plt.subplots()
  sns.countplot(data=df, x='species', ax=ax)
  st.pyplot(fig)

  st.write("Bill Length vs Bill Depth")
  fig, ax = plt.subplots()
  sns.scatterplot(data=df, x='bill_length_mm', y='bill_depth_mm', hue='species', ax=ax)
  st.pyplot(fig)
 
  st.write("Bill Length vs Body Mass")
  fig, ax = plt.subplots()
  sns.scatterplot(data=df, x='bill_length_mm', y='body_mass_g', hue='species', ax=ax)
  st.pyplot(fig)
  
#####################################################################################################
# Boxplot visualization  
  st.write("Boxplot of Body Mass by Species")
  fig, ax = plt.subplots()
  sns.boxplot(data=df, x='species', y='body_mass_g', ax=ax)
  st.pyplot(fig)
#####################################################################################################
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
 
  data = {

    'island': island,

    'bill_length_mm': bill_length_mm,

    'bill_depth_mm': bill_depth_mm,

    'flipper_length_mm': flipper_length_mm,

    'body_mass_g': body_mass_g,

    'gender': gender

}

input_df = pd.DataFrame(data, index = [0])

input_penguins = pd.concat([input_df, X_raw], axis = 0)
 
with st.expander("Input data"):

  st.write("*Input data*")

  input_df

  st.write("*Combineed data*")

  input_penguins
 
#One hot encoding for X

encode_ = ['island', 'sex']

df_penguins = pd.get_dummies(input_penguins, columns = encode_)

input_row = df_penguins.iloc[0:1]  # User input

X = df_penguins[1:]
 
#one hot encoding for y

target_mapper = {

'Adelie' : 0,

'Gentoo' : 1,

'Chinstrap' : 2

}
 
def target_encode(val):
  return target_mapper[val]
 
y = y_raw.apply(target_encode)
