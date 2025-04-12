import streamlit as st
from prediction_helper import predict

st.title("CodeX Beverage: Price Prediction")

# Create rows of three columns each
row1 = st.columns(4)
row2 = st.columns(4)
row3 = st.columns(4)
row4 = st.columns(4)

# Assign inputs to the first row with default values
with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100, value=30)
with row1[1]:
    gender = st.selectbox('Gender', ['M', 'F'])
with row1[2]:
    zone = st.selectbox('Zone', ['Urban', 'Metro', 'Rural', 'Semi-Urban'])
with row1[3]:
    occupation = st.selectbox('Occupation', ['Entrepreneur', 'Working Professional', 'Student', 'Retired'])

with row2[0]:
    income_level = st.selectbox('Income Level (In L)', ['<10L', '10L - 15L',  '16L - 25L', '26L - 35L', '> 35L', 'Not Reported'])
with row2[1]:
    consume_frequency = st.selectbox('Consume Frequency(Weekly)', ['0-2 times', '3-4 times', '5-7 times'])
with row2[2]:
    current_brand = st.selectbox('Current Brand', ['Newcomer', 'Established'])
with row2[3]:
    preferable_consumption_size = st.selectbox('Preferable Consumption Size', ['Small (250 ml)', 'Medium (500 ml)', 'Large (1 L)'])

with row3[0]:
    awareness_of_other_brands = st.selectbox('Awareness of other brands', ['0 to 1', '2 to 4', 'above 4'])
with row3[1]:
    reasons_for_choosing_brands = st.selectbox('Reasons for choosing brands', ['Price', 'Quality', 'Availability', 'Brand Reputation'])
with row3[2]:
    flavor_preference = st.selectbox('Flavor Preference', ['Traditional', 'Exotic'])
with row3[3]:
    purchase_channel = st.selectbox('Purchase Channel', ['Online', 'Retail Store'])

with row4[0]:
    packaging_preference = st.selectbox('Packaging Preference', ['Simple', 'Premium', 'Eco-Friendly'])
with row4[1]:
    health_concerns = st.selectbox('Health Concerns', ['Medium (Moderately health-conscious)', 'Low (Not very concerned)',
       'High (Very health-conscious)'])
with row4[2]:
    typical_consumption_situations = st.selectbox('Typical Consumption Situations', ['Active (eg. Sports, gym)', 'Social (eg. Parties)',
       'Casual (eg. At home)'])

# Create a dictionary for input values
input_dict = {
    'Age': age,
    'Gender': gender,
    'Zone': zone,
    'Occupation': occupation,
    'Income Level': income_level,
    'Consume Frequency': consume_frequency,
    'Current Brand': current_brand,
    'Preferable Consumption Size': preferable_consumption_size,
    'Awareness of other brands': awareness_of_other_brands,
    'Reasons for choosing brands': reasons_for_choosing_brands,
    'Flavor Preference': flavor_preference,
    'Purchase Channel': purchase_channel,
    'Packaging Preference': packaging_preference,
    'Health Concerns': health_concerns,
    'Typical Consumption Situations': typical_consumption_situations
}

# Button to make prediction
if st.button('Predict'):
    prediction = predict(input_dict)
    st.success(f'Predicted price: {prediction}')