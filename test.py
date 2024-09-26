import streamlit as st
import pandas as pd
import pickle

# Load the trained model
filename = 'ensemble_model.pkl'
loaded_model = pickle.load(open(filename, 'rb'))

st.title('Monthly Revenue Prediction')

# Input features from user
st.header('Enter Store Details:')
website_visits = st.number_input('Website Visits', min_value=0, value=0)
average_order_value = st.number_input('Average Order Value', min_value=0.0, value=0.0)
customer_acquisition_cost = st.number_input('Customer Acquisition Cost', min_value=0.0, value=0.0)
marketing_spend = st.number_input('Marketing Spend', min_value=0.0, value=0.0)
operating_costs = st.number_input('Operating Costs', min_value=0.0, value=0.0)
customer_lifetime_value = st.number_input('Customer Lifetime Value', min_value=0.0, value=0.0)


# Create a DataFrame with the input values
input_data = pd.DataFrame({
    'website_visits': [website_visits],
    'average_order_value': [average_order_value],
    'customer_acquisition_cost': [customer_acquisition_cost],
    'marketing_spend': [marketing_spend],
    'operating_costs': [operating_costs],
    'customer_lifetime_value': [customer_lifetime_value]
})


# Make prediction
if st.button('Predict Monthly Revenue'):
    prediction = loaded_model.predict(input_data)
    st.write(f'Predicted Monthly Revenue: {prediction[0]:.2f}')
