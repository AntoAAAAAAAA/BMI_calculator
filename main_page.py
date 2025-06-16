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

# Two columns for weight
col1, col2 = st.columns([2, 1])  # Adjust the width ratio as needed
# Input for weight and dropdown for unit
with col1:
    weight = st.text_input('Weight')
with col2:
    unit = st.selectbox('Unit', ['lb', 'kg'])
# Display the selected weight and unit
if weight:
    st.write(f'Weight: {weight} {unit}')

st.subheader('Height')
# Two columns for height
col1, col2, col3, col4 = st.columns([4,2,4,2])  # Adjust the width ratio as needed
# Input for weight and dropdown for unit
with col1:
    height1 = st.text_input('', key='height1')
with col2:
    unit1 = st.selectbox('Unit', ['ft', 'm'])
with col3:
    height2 = st.text_input('', key='height2')
with col4:
    unit2 = st.selectbox('Unit', ['in','cm'])
# Display the selected weight and unit
if (unit1 == 'ft' and unit2 == 'in') or (unit1 == 'm' and unit2 == 'cm'):
    st.write(f"Height: {height1} {unit1} {height2} {unit2}")
else:
    st.write('Error: Units not matching. Please choose either imperial or metric system for input')
#Results 
st.subheader('Results:')