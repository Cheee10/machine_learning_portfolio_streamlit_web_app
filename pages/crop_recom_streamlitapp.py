import streamlit as st
import pandas as pd
import joblib

# Load the trained model with error handling
filename = 'pages/laptops.csv'
try:
    loaded_model = joblib.load(filename)
except FileNotFoundError:
    st.error(f"Model file not found: {filename}")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")
    st.stop()

# Function to predict laptop brand
def predict_brand(features):
    if loaded_model is not None:
        brand_name = loaded_model.predict([features])[0]
        st.success(f"The predicted brand is {brand_name}")
    else:
        st.warning("Model is not loaded.")

# Streamlit app
st.title("Laptop Brand Predictor")
st.subheader("Enter features to predict the laptop brand:")

# Slider inputs for features
price_input = st.slider("Price:", 0.0, 20000.0)
rating_input = st.slider("Rating:", 0.0, 20.0)
ram_input = st.slider("RAM (GB):", 0, 32)

# Button to trigger prediction
if st.button("Predict Brand"):
    features = [price_input, rating_input, ram_input]
    predict_brand(features)

st.text("The predicted brand will be displayed above.")
