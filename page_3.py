import streamlit as st
import matplotlib.pyplot as plt

# Ensure session state is loaded
if "language" not in st.session_state:
    st.session_state["language"] = "English"
language = st.session_state.language

# Import values
valid_bmi = st.session_state.get("valid_bmi") is True
bmi = st.session_state.get("bmi")

# Translations
translations = {
    "bmi_above_average": {
        "English": "📈 Your BMI is above the national average",
        "Spanish": "📈 Su IMC está por encima del promedio nacional",
    },
    "bmi_below_average": {
        "English": "📉 Your BMI is below the national average",
        "Spanish": "📉 Su IMC está por debajo del promedio nacional",
    },
    "bmi_equal_average": {
        "English": "⚖️ Your BMI is equal to the national average",
        "Spanish": "⚖️ Su IMC es igual al promedio nacional",
    },
    "bmi_points_higher": {
        "English": "points higher",
        "Spanish": "puntos más alto",
    },
    "bmi_points_lower": {
        "English": "points lower",
        "Spanish": "puntos más bajo",
    },
    "comparison_header": {
        "English": "Comparison to National Average",
        "Spanish": "Comparación con el promedio nacional",
    }
}

def get_text(key, language):
    return translations[key][language]

# Page layout
st.subheader(get_text("comparison_header", language))

# National average BMI
average_bmi = 29.0

# If valid BMI exists
if valid_bmi and bmi is not None:
    # Comparison message
    difference = round(bmi - average_bmi, 1)
    if difference > 0:
        comparison_text = get_text("bmi_above_average", language) + f" ({difference} {get_text('bmi_points_higher', language)})"
    elif difference < 0:
        comparison_text = get_text("bmi_below_average", language) + f" ({abs(difference)} {get_text('bmi_points_lower', language)})"
    else:
        comparison_text = get_text("bmi_equal_average", language)
    
    st.success(comparison_text)

    # Nicer graph
    fig, ax = plt.subplots(figsize=(6, 4))

    bars = ax.bar(["You", "U.S. Avg"], [bmi, average_bmi], color=["#1f77b4", "#ff7f0e"], width=0.5)
    ax.set_ylim(0, max(bmi, average_bmi) + 10)
    ax.set_ylabel("BMI", fontsize=12)
    ax.set_title("BMI Comparison", fontsize=14, fontweight='bold')

    # Add value labels above bars
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5),  # vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=11, fontweight='bold')

    # Clean axes
    ax.spines[['top', 'right']].set_visible(False)
    ax.yaxis.grid(True, linestyle='--', linewidth=0.5)
    ax.set_axisbelow(True)

    st.pyplot(fig)

    if bmi > 25:
        st.info("🔗 [Tips for Healthy Weight Management](https://www.cdc.gov/healthyweight/index.html)")
    elif bmi < 18.5:
        st.info("🔗 [Understanding Underweight Risks](https://www.cdc.gov/nutrition/index.html)")

else:
    st.info("⏳ Waiting on BMI input...")    