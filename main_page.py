import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Access the language from session_state
language = st.session_state.language

# Define the translations
translations = {
    "page_title": {
        "English": "BMI + Health Metric Calculator",
        "Spanish": "Calculadora de Índice de Masa Corporal y Métricas de Salud",
    },
    "intro_text": {
        "English": "Welcome to the BMI + Health Metric Calculator. Please select your health metrics.",
        "Spanish": "Bienvenido a la Calculadora de IMC y Métricas de Salud. Seleccione sus métricas de salud.",
    },
    ###More should be added here
}

# Function to get the translated text
def get_text(key, language):
    return translations[key][language]

# Display the content based on the selected language
st.title(get_text('page_title', language))
st.write(get_text('intro_text', language))

valid_weight = None
weight_valid = False
valid_unit3 = None
# Two columns for weight
col1, col2 = st.columns([2, 1])  # Adjust the width ratio as needed
# Input for weight and dropdown for unit
with col1:
    weight = st.text_input('Weight')
    try:
        weight = float(weight)
        if weight > 0 and weight < 2000:
            valid_weight = weight
            weight_valid = True
        else:
            st.error('Please input a real weight')
            weight_valid = False
    except ValueError:
        weight_valid = False
        st.write('Please enter a valid number')
with col2:
    unit = st.selectbox('', ['lb', 'kg'])
# Display the selected weight and unit
valid_unit3 = unit
st.write(f'Weight: {weight} {unit}')

# Two columns for height
col1, col2, col3, col4 = st.columns([4,2,4,2])  # Adjust the width ratio as needed
# Input for weight and dropdown for unit
with col1:
    height1 = st.text_input('Height', key='height1')
    try:
        height1 = int(height1)
    except ValueError:
        height1 = None
with col2:
    unit1 = st.selectbox('', ['ft', 'm'])
with col3:
    height2 = st.text_input('', key='height2')
    try:
        height2 = int(height2)
    except ValueError:
        height2 = None
with col4:
    unit2 = st.selectbox('', ['in','cm'])

valid_height1 = None
valid_height2 = None
valid_unit1 = None
valid_unit2 = None
# Display the selected weight and unit
height_valid = False
if height1 and height2: 
    if ((unit1 == 'ft' and unit2 == 'in') or (unit1 == 'm' and unit2 == 'cm')):
        if (height1 < 8 ) and (height2 < 12):
            st.write(f"Height: {height1} {unit1} {height2} {unit2}")
            valid_height1 = int(height1)
            valid_unit1 = unit1
            valid_height2 = int(height2)
            valid_unit2 = unit2
            height_valid = True
        else:
            st.error(f"Please input a valid height (Please also check if units match)")
    else:
        st.error('Please make sure units are matching')
else:
    st.info("Waiting for valid height input...")

st.write('')
#Results 
#This section of code does calculation 
st.subheader('Results:')

if not valid_height1:
    st.write('Not valid weight')

if not valid_height1 or not valid_height2 or not valid_unit1 or not valid_unit2:
    st.write('No valid height')


#calculations for BMI
if height_valid and weight_valid:
    if valid_unit3 == 'lb':
        final_weight = round(valid_weight / 2.205, 2)
    else:
        final_weight = valid_weight


    if valid_unit1 == 'ft' and valid_unit2 == 'in':
        total_inches = (valid_height1*12) + valid_height2
        final_height_meter = round(total_inches/39.37,2)
    else:
        final_height_meter = round(((valid_height1*100) + valid_height2 )/100, 2)
    
    bmi = round((final_weight/(final_height_meter)**2), 2)

    st.write(f'Final weight in kilograms: {final_weight} kg')
    st.write(f'Final height in meters: {final_height_meter} m')

    st.success(f'Your BMI is: {bmi}')

else:
    st.warning("BMI cannot be calculated until both weight and height are valid.")