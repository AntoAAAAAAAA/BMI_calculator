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
    },
    "disclaimer": {
        "English": "⚠️ **Disclaimer:** This tool is for general educational purposes only and does not provide medical advice. Please consult a healthcare provider for personalized health guidance.",
        "Spanish": "⚠️ **Descargo de responsabilidad:** Esta herramienta es solo para fines educativos generales y no proporciona asesoramiento médico. Consulte a un proveedor de atención médica para obtener orientación personalizada.",
    },
    "bmi_info_header": {
        "English": "Click to See BMI Ranges",
        "Spanish": "Haga clic para ver los rangos de IMC",
    }
}

def get_text(key, language):
    return translations[key][language]

st.title(get_text('page_title', language))
st.markdown('-----')
st.write(get_text('intro_text', language))

# Initialize defaults if needed
for key in ["weight", "unit", "height1", "height2", "unit1", "unit2"]:
    if key not in st.session_state:
        st.session_state[key] = ""

# --- Weight Input ---
col1, col2 = st.columns([2, 1])
with col1:
    weight = st.text_input(get_text('weight_input_label', language), value=st.session_state["weight"], key="weight")
with col2:
    unit = st.selectbox('', ['lb', 'kg'], index=['lb', 'kg'].index(st.session_state.get("unit", 'lb')))
st.session_state["unit"] = unit

# Validate weight
weight_valid = False
try:
    weight_val = float(weight)
    if 0 < weight_val < 2000:
        weight_valid = True
    else:
        st.error(get_text('weight_invalid_range', language))
except ValueError:
    st.write(get_text('weight_invalid_format', language))

st.write(f'{get_text("weight_input_label", language)}: {weight} {unit}')

# --- Height Input ---
col1, col2, col3, col4 = st.columns([4, 2, 4, 2])
with col1:
    st.text_input(get_text('height_input_label', language), value=st.session_state["height1"], key='height1')
with col2:
    st.selectbox('', ['ft', 'm'], index=['ft', 'm'].index(st.session_state.get("unit1", 'ft')), key='unit1')
with col3:
    st.text_input('', value=st.session_state["height2"], key='height2')
with col4:
    st.selectbox('', ['in', 'cm'], index=['in', 'cm'].index(st.session_state.get("unit2", 'in')), key='unit2')

# Retrieve values from session_state
try:
    height1 = int(st.session_state["height1"])
except ValueError:
    height1 = None

try:
    height2 = int(st.session_state["height2"])
except ValueError:
    height2 = None

unit1 = st.session_state["unit1"]
unit2 = st.session_state["unit2"]

# Validate height
height_valid = False
if height1 and height2:
    if ((unit1 == 'ft' and unit2 == 'in') or (unit1 == 'm' and unit2 == 'cm')):
        if (height1 < 8) and (height2 < 12):
            height_valid = True
            st.write(f"{get_text('height_input_label', language)}: {height1} {unit1} {height2} {unit2}")
        else:
            st.error(get_text('height_invalid_values', language))
    else:
        st.error(get_text('height_invalid_units', language))
else:
    st.info(get_text('height_waiting', language))

# --- BMI Calculation ---
st.subheader(get_text('results_subheader', language))

bmi = None
valid_bmi = False
if height_valid and weight_valid:
    final_weight = float(weight_val / 2.205) if unit == 'lb' else float(weight_val)
    if unit1 == 'ft' and unit2 == 'in':
        final_height_m = ((height1 * 12) + height2) / 39.37
    else:
        final_height_m = ((height1 * 100) + height2) / 100
    bmi = round(final_weight / (final_height_m ** 2), 2)
    valid_bmi = True
    st.session_state["bmi"] = bmi
    st.session_state["valid_bmi"] = True
else:
    st.session_state["bmi"] = None
    st.session_state["valid_bmi"] = False
    st.warning(get_text('bmi_warning', language))

# --- Display BMI ---
if valid_bmi:
    st.metric(label="BMI", value=round(bmi, 2), border=True)
    if bmi < 18.5:
        st.warning(get_text('underweight', language))
    elif bmi < 25:
        st.success(get_text('normal', language))
    elif bmi < 30:
        st.warning(get_text('overweight', language))
    else:
        st.error(get_text('obese', language))

with st.expander(get_text("bmi_info_header", language)):
    if language == "English":
        st.markdown("""
        - **Underweight**: BMI < 18.5  
        - **Normal weight**: 18.5 – 24.9  
        - **Overweight**: 25 – 29.9  
        - **Obese**: 30+
        """)
    else:
        st.markdown("""
        - **Bajo peso**: IMC < 18.5  
        - **Normal**: 18.5 – 24.9  
        - **Sobrepeso**: 25 – 29.9  
        - **Obeso**: 30+
        """)

# --- Disclaimer ---
st.markdown(f"""
<div style="
    background-color: #f9f9f9;
    padding: 1rem;
    border-left: 5px solid #888888;
    border-radius: 8px;
    font-size: 0.9rem;
    font-style: italic;
    color: #333;
">
    {get_text("disclaimer", language)}
</div>
""", unsafe_allow_html=True)