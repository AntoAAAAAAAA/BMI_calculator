import streamlit as st

# Set up language selector globally
if 'language' not in st.session_state:
    st.session_state.language = 'English'

language = st.sidebar.selectbox('Select a Language', ['English', 'Spanish'], index=0 if st.session_state.language == 'English' else 1)

# Store the selected language in session_state to be accessed in other pages
st.session_state.language = language

# Define the pages
main_page = st.Page("main_page.py", title="BMI Calculator")
page_2 = st.Page("page_2.py", title="Understand Your Results")
page_3 = st.Page('page_3.py', title='Compare your Results')
# Navigation
pg = st.navigation([main_page, page_2, page_3])

pg.run()
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
