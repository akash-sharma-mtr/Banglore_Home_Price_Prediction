import streamlit as st
import numpy as np
import pickle
import json

st.title("Home Price Prediction in Bengluru")

locations = None
data_columns = None
model = None

with open('columns.json','r') as f:
    data_columns = json.load(f)['data_columns']
    locations = data_columns[3:]

if model is None:
    with open('banglore_home_prices_model.pickle','rb') as f:
        model = pickle.load(f)



area = st.number_input("Enter the area in Squeare feet :", step = 10)
bhk = st.slider("Enter the BHK :", 1, 5)
bath = st.slider("Enter the number of bathrooms :", 1, 5)
location = st.selectbox("Select the location :", locations)

loc_inddex = loc_index = data_columns.index(location.lower())

x = np.zeros(len(data_columns))
x[0] = area
x[1] = bath
x[2] = bhk
if loc_index>=0:
    x[loc_index] = 1

if st.button("Predict"):
    st.write("The predicted price is ", round(model.predict([x])[0],2)," Lacs")
else:
    st.write("Please click the button to predict")

