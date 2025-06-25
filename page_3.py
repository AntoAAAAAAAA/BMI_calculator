import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#importation of values from main_page
valid_bmi = st.session_state.get("valid_bmi", False)
bmi = st.session_state.get("bmi", None)
weight = st.session_state.get("weight", None)
unit = st.session_state.get("unit", None)
height1 = st.session_state.get("height1", None)
height2 = st.session_state.get("height2", None)
unit1 = st.session_state.get("unit1", None)
unit2 = st.session_state.get("unit2", None)

language = st.session_state.language

#set up translations 
translations = {
    "bmi_above_average": {
    "English": "Your BMI is above the national average",
    "Spanish": "Su IMC está por encima del promedio nacional",
    },
    "bmi_below_average": {
        "English": "Your BMI is below the national average",
        "Spanish": "Su IMC está por debajo del promedio nacional",
    },
    "bmi_equal_average": {
        "English": "Your BMI is equal to the national average",
        "Spanish": "Su IMC es igual al promedio nacional",
    },
    "bmi_points_higher": {
        "English": "points higher",
        "Spanish": "puntos más alto",
    },
    "bmi_points_lower": {
        "English": "points lower",
        "Spanish": "puntos más bajo",
}
}

def get_text(key, language):
    return translations[key][language]


average_bmi = 29.0
if valid_bmi and bmi is not None:
    difference = round(bmi - average_bmi, 1)
    if difference > 0:
        comparison_text = get_text("bmi_above_average", language) + f" ({difference} {get_text('bmi_points_higher', language)})"
    elif difference < 0:
        comparison_text = get_text("bmi_below_average", language) + f" ({abs(difference)} {get_text('bmi_points_lower', language)})"
    else:
        comparison_text = get_text("bmi_equal_average", language)

    st.info(comparison_text)
else:
    st.info('Waiting on BMI input...')
