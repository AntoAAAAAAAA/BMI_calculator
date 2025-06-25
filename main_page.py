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
        "Spanish": "Bienvenido a la Calculadora de IMC (BMI) y Métricas de Salud. Seleccione sus métricas de salud.",
    },
    "weight_input_label": {
        "English": "Weight",
        "Spanish": "Peso",
    },
    "weight_invalid_range": {
        "English": "Please input a real weight",
        "Spanish": "Por favor ingrese un peso real",
    },
    "weight_invalid_format": {
        "English": "Please enter a valid number",
        "Spanish": "Por favor ingrese un número válido",
    },
    "height_input_label": {
        "English": "Height",
        "Spanish": "Altura",
    },
    "height_invalid_units": {
        "English": "Please make sure units are matching",
        "Spanish": "Por favor asegúrese de que las unidades coincidan",
    },
    "height_invalid_values": {
        "English": "Please input a valid height (Please also check if units match)",
        "Spanish": "Por favor ingrese una altura válida (Verifique también que las unidades coincidan)",
    },
    "height_waiting": {
        "English": "Waiting for valid height input...",
        "Spanish": "Por favor, ingresa una altura válida...",
    },
    "results_subheader": {
        "English": "Results:",
        "Spanish": "Resultados:",
    },
    "not_valid_weight": {
        "English": "Not valid weight",
        "Spanish": "Peso no válido",
    },
    "not_valid_height": {
        "English": "No valid height",
        "Spanish": "Altura no válida",
    },
    "final_weight_kg": {
        "English": "Final weight in kilograms",
        "Spanish": "Peso final en kilogramos",
    },
    "final_height_m": {
        "English": "Final height in meters",
        "Spanish": "Altura final en metros",
    },
    "bmi_result": {
        "English": "Your BMI is",
        "Spanish": "Su IMC es",
    },
    "bmi_warning": {
        "English": "BMI cannot be calculated until both weight and height are valid.",
        "Spanish": "El IMC no se puede calcular hasta que el peso y la altura sean validos.",
    },
    "underweight": {
        "English": "Underweight",
        "Spanish": "Bajo peso",
    },
    "normal": {
        "English": "Normal",
        "Spanish": "Normal",
    },
    "overweight": {
        "English": "Overweight",
        "Spanish": "Sobrepeso",
    },
    "obese": {
        "English": "Obese",
        "Spanish": "Obeso",
    }
}

# Function to get the translated text
def get_text(key, language):
    return translations[key][language]

# Display the content based on the selected language
st.title(get_text('page_title', language))
st.markdown('-----')
st.write(get_text('intro_text', language))


valid_weight = None
weight_valid = False
valid_unit3 = None
# Two columns for weight
col1, col2 = st.columns([2, 1])
with col1:
    weight = st.text_input(get_text('weight_input_label', language))
    try:
        weight = float(weight)
        if weight > 0 and weight < 2000:
            valid_weight = weight
            weight_valid = True
        else:
            st.error(get_text('weight_invalid_range', language))
            weight_valid = False
    except ValueError:
        weight_valid = False
        st.write(get_text('weight_invalid_format', language))
with col2:
    unit = st.selectbox('', ['lb', 'kg'])
valid_unit3 = unit
st.write(f'{get_text("weight_input_label", language)}: {weight} {unit}')

# Two columns for height
col1, col2, col3, col4 = st.columns([4, 2, 4, 2])
with col1:
    height1 = st.text_input(get_text('height_input_label', language), key='height1')
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
    unit2 = st.selectbox('', ['in', 'cm'])

valid_height1 = None
valid_height2 = None
valid_unit1 = None
valid_unit2 = None
height_valid = False
if height1 and height2:
    if ((unit1 == 'ft' and unit2 == 'in') or (unit1 == 'm' and unit2 == 'cm')):
        if (height1 < 8) and (height2 < 12):
            st.write(f"{get_text('height_input_label', language)}: {height1} {unit1} {height2} {unit2}")
            valid_height1 = int(height1)
            valid_unit1 = unit1
            valid_height2 = int(height2)
            valid_unit2 = unit2
            height_valid = True
        else:
            st.error(get_text('height_invalid_values', language))
    else:
        st.error(get_text('height_invalid_units', language))
else:
    st.info(get_text('height_waiting', language))

st.write('')
# Results
st.subheader(get_text('results_subheader', language))

bmi=None
valid_bmi = False
if not valid_height1:
    st.write(get_text('not_valid_weight', language))

if not valid_height1 or not valid_height2 or not valid_unit1 or not valid_unit2:
    st.write(get_text('not_valid_height', language))

if height_valid and weight_valid:
    if valid_unit3 == 'lb':
        final_weight = round(valid_weight / 2.205, 2)
    else:
        final_weight = valid_weight

    if valid_unit1 == 'ft' and valid_unit2 == 'in':
        total_inches = (valid_height1 * 12) + valid_height2
        final_height_meter = round(total_inches / 39.37, 2)
    else:
        final_height_meter = round(((valid_height1 * 100) + valid_height2) / 100, 2)

    bmi = round((final_weight / (final_height_meter)**2), 2)

    valid_bmi = True
else:
    st.warning(get_text('bmi_warning', language))

if valid_bmi:
    if bmi < 18.5:
        #st.warning(f"{get_text('bmi_result', language)} {bmi}")
        st.metric(label="BMI", value=round(bmi, 2), border=True)
        st.warning(get_text('underweight', language))
    elif bmi < 25:
        st.metric(label="BMI", value=round(bmi, 2), border=True)
        st.success(get_text('normal', language))
    elif bmi < 30:
        st.metric(label="BMI", value=round(bmi, 2), border=True)
        st.warning(get_text('overweight', language))
    else:
        st.metric(label="BMI", value=round(bmi, 2), border=True)
        st.error(get_text('obese', language))