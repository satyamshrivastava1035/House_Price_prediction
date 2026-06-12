import pickle
import streamlit as st
import pandas as pd

with open("Housing_price_pipeline.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🏠 House Price Prediction")

area = st.number_input(
    "Area (sq ft)",
    min_value=100,
    value=1000
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    value=2
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=1,
    value=2
)

stories = st.number_input(
    "Stories",
    min_value=1,
    value=2
)

parking = st.number_input(
    "parking",
    min_value=1,
    value=2
)

mainroad = st.selectbox(
    "mainroad",
    ['yes','no']
)

guestroom = st.selectbox(
    "guestroom",
    ['yes','no']
)

basement = st.selectbox(
    "basement",
    ['yes','no']
)

hotwaterheating = st.selectbox(
    "hotwaterheating",
    ['yes','no']
)

airconditioning = st.selectbox(
    "airconditioning",
    ['yes','no']
)

prefarea = st.selectbox(
    "prefarea",
    ['yes','no']
)

furnishingstatus = st.selectbox(
    "furnishingstatus",
    ['yes','no']
)

features = pd.DataFrame({
    "area": [area],
    "bedrooms": [bedrooms],
    "bathrooms": [bathrooms],
    "stories": [stories],
    "parking": [parking],
    "mainroad": [mainroad],
    "guestroom": [guestroom],
    "basement": [basement],
    "hotwaterheating": [hotwaterheating],
    "airconditioning": [airconditioning],
    "prefarea": [prefarea],
    "furnishingstatus": [furnishingstatus]})

if st.button("Predict Price"):


    prediction = model.predict(features)

    st.success(
        f"Predicted House Price: ₹ {prediction[0]:,.2f}"
    )

    st.balloons()