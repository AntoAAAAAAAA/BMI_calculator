import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

language = st.session_state.language

#set up translations 
# Translations for all four BMI categories (FULL VERSION)
translations = {
    "page_title": {
        "English": "Understand your Results",
        "Spanish": "Comprenda sus resultados",
    },

    # Tab labels
    "underweight_tab": {"English": "Underweight", "Spanish": "Bajo peso"},
    "normal_tab": {"English": "Normal", "Spanish": "Normal"},
    "overweight_tab": {"English": "Overweight", "Spanish": "Sobrepeso"},
    "obese_tab": {"English": "Obese", "Spanish": "Obesidad"},

    # Shared headings
    "what_it_means": {"English": "What It Means:", "Spanish": "Qué significa:"},
    "what_you_can_do": {"English": "What You Can Do:", "Spanish": "Qué puede hacer:"},
    "your_goal": {"English": "Your Goal:", "Spanish": "Su objetivo:"},
    "sources": {"English": "Sources:", "Spanish": "Fuentes:"},

    # Underweight
    "bmi_category_underweight": {
        "English": "BMI Category: Underweight (Less than 18.5)",
        "Spanish": "Categoría de IMC: Bajo peso (menos de 18.5)"
    },
    "underweight_meaning_1": {
        "English": "Your weight is lower than what's considered healthy for your height. This can lead to feeling tired, weaker bones and muscles, and a lower resistance to illness.",
        "Spanish": "Su peso está por debajo de lo considerado saludable para su estatura. Esto puede causar fatiga, debilidad ósea y muscular, y menor resistencia a enfermedades."
    },
    "underweight_meaning_2": {
        "English": "Sometimes people are naturally slim and healthy. But being underweight can also be a sign of other issues. Possible causes include:",
        "Spanish": "Algunas personas son naturalmente delgadas y saludables. Pero tener bajo peso también puede ser señal de otros problemas. Las posibles causas incluyen:"
    },
    "underweight_causes": {
        "English": "- Not eating enough — due to stress, busy life, or lack of food\n- Digestive problems — like celiac disease or Crohn’s disease\n- Thyroid issues — such as hyperthyroidism\n- Mental health concerns — like anxiety, depression, or eating disorders\n- Underlying illnesses — such as cancer or chronic infections",
        "Spanish": "- No comer lo suficiente — por estrés, ritmo de vida agitado o falta de alimentos\n- Problemas digestivos — como enfermedad celíaca o enfermedad de Crohn\n- Problemas de tiroides — como el hipertiroidismo\n- Problemas de salud mental — como ansiedad, depresión o trastornos alimenticios\n- Enfermedades subyacentes — como cáncer o infecciones crónicas"
    },
    "underweight_tips": {
        "English": "- Eat more often. Try 3 meals and 2–3 snacks daily, even if you don’t feel hungry\n- Choose nutritious foods. Add calorie-rich items like nuts, cheese, avocados, whole grains, and smoothies\n- Do light strength exercises. It helps build healthy muscle weight\n- Talk to a doctor. If you’re losing weight without meaning to or can’t gain weight, ask a provider to check for health problems",
        "Spanish": "- Coma con más frecuencia. Intente comer 3 comidas y 2–3 refrigerios al día, incluso si no tiene hambre\n- Elija alimentos nutritivos. Agregue alimentos ricos en calorías como nueces, queso, aguacates, granos integrales y batidos\n- Haga ejercicios de fuerza ligeros. Ayuda a ganar peso muscular saludable\n- Consulte a un médico. Si pierde peso sin intención o no puede aumentar, busque orientación médica"
    },
    "underweight_goal": {
        "English": "Gradually reach a BMI between 18.5 and 24.9, the healthy range. Small, steady steps—eating more, choosing nutrient-rich foods, and exercising—can improve your health, energy, and strength over time.",
        "Spanish": "Alcance gradualmente un IMC entre 18.5 y 24.9, el rango saludable. Pequeños pasos constantes —comer más, elegir alimentos nutritivos y hacer ejercicio— pueden mejorar su salud, energía y fuerza con el tiempo."
    },

    # Normal
    "bmi_category_normal": {
        "English": "BMI Category: Normal (18.5 to 24.9)",
        "Spanish": "Categoría de IMC: Normal (18.5 a 24.9)"
    },
    "normal_meaning": {
        "English": "Your BMI is within the healthy “normal” range for your height. This generally means your risk for weight-related health problems—like high blood pressure, heart disease, and type 2 diabetes—is lower.",
        "Spanish": "Su IMC está dentro del rango \"normal\" saludable para su estatura. Esto significa que tiene menor riesgo de problemas de salud relacionados con el peso como presión alta, enfermedades del corazón y diabetes tipo 2."
    },
    "normal_tips": {
        "English": "- Keep up healthy habits: Continue eating balanced meals with whole grains, fruits, vegetables, lean proteins, and healthy fats.\n- Stay active: Aim for at least 150 minutes of moderate exercise each week (e.g., brisk walking, cycling).\n- Regular check-ups: Continue routine health screenings (like blood pressure, cholesterol) to catch any changes early.",
        "Spanish": "- Mantenga hábitos saludables: Siga comiendo comidas balanceadas con granos integrales, frutas, verduras, proteínas magras y grasas saludables.\n- Manténgase activo: Haga al menos 150 minutos de ejercicio moderado por semana (como caminar o andar en bicicleta).\n- Chequeos regulares: Hágase controles médicos periódicos como presión y colesterol para detectar cambios a tiempo."
    },
    "normal_goal": {
        "English": "Maintain your BMI in the 18.5–24.9 range to support long-term health, energy levels, and well-being.",
        "Spanish": "Mantenga su IMC entre 18.5 y 24.9 para conservar su salud a largo plazo, energía y bienestar."
    },

    # Overweight
    "bmi_category_overweight": {
        "English": "BMI Category: Overweight (25.0 to 29.9)",
        "Spanish": "Categoría de IMC: Sobrepeso (25.0 a 29.9)"
    },
    "overweight_meaning": {
        "English": "Your BMI is higher than the healthy range. This can increase your chances of developing high blood pressure, type 2 diabetes, and heart disease.",
        "Spanish": "Su IMC está por encima del rango saludable. Esto puede aumentar su riesgo de presión alta, diabetes tipo 2 y enfermedades cardíacas."
    },
    "overweight_tips": {
        "English": "- Improve your diet: Focus on whole foods—fruits, vegetables, lean protein, whole grains, and healthy fats. Reduce sugary drinks and processed snacks.\n- Move more: Try a mix of cardio (walking, cycling) and strength exercises. Aim for at least 150 minutes of moderate activity weekly.\n- Talk to a Doctor or Dietitian: They can help create a realistic and safe plan to reach a healthier weight.",
        "Spanish": "- Mejore su dieta: Consuma alimentos integrales — frutas, verduras, proteínas magras, granos enteros y grasas saludables. Reduzca los azúcares y los productos procesados.\n- Muévase más: Combine cardio (caminar, bicicleta) y ejercicios de fuerza. Apunte a al menos 150 minutos por semana.\n- Consulte a un médico o dietista: Ellos pueden ayudarle a crear un plan realista y seguro para alcanzar un peso más saludable."
    },
    "overweight_goal": {
        "English": "Lower your BMI into the normal range (18.5–24.9) to reduce health risks and stay fit.",
        "Spanish": "Reduzca su IMC al rango normal (18.5–24.9) para disminuir riesgos y mejorar su estado físico."
    },

    # Obese
    "bmi_category_obese": {
        "English": "BMI Category: Obese (30.0 and above)",
        "Spanish": "Categoría de IMC: Obesidad (30.0 o más)"
    },
    "obese_meaning": {
        "English": "Your BMI falls into the “obesity” category. This raises your risk for serious health problems like high blood pressure, type 2 diabetes, heart disease, sleep apnea, and some cancers.",
        "Spanish": "Su IMC cae dentro de la categoría de obesidad. Esto aumenta su riesgo de problemas graves como presión alta, diabetes tipo 2, enfermedades cardíacas, apnea del sueño y algunos tipos de cáncer."
    },
    "obese_tips": {
        "English": "- Adopt healthy eating habits: Eat a balanced diet rich in whole foods. Limit high-calorie processed items.\n- Increase physical activity: Add both cardio and strength training. Work toward at least 150 minutes per week—and build up slowly if needed.\n- Talk to a Doctor or Dietitian: They can help you create a personalized plan. Sometimes medication or weight-loss surgery is recommended.\n- Support your overall health: Manage stress, get enough sleep, and monitor your blood pressure, cholesterol, and blood sugar.",
        "Spanish": "- Adopte hábitos saludables: Consuma una dieta equilibrada rica en alimentos naturales. Limite alimentos procesados y altos en calorías.\n- Aumente la actividad física: Incluya cardio y fuerza. Apunte a 150 minutos semanales, aumentando gradualmente.\n- Consulte a un médico o dietista: Pueden ayudarle con un plan personalizado. En algunos casos se recomienda medicación o cirugía.\n- Apoye su salud general: Controle el estrés, duerma bien y vigile su presión, colesterol y azúcar."
    },
    "obese_goal": {
        "English": "Work safely toward lowering your BMI below 30. Even a small weight loss (5–10% of your current weight) can lead to big health improvements.",
        "Spanish": "Trabaje de manera segura para reducir su IMC por debajo de 30. Incluso una pequeña pérdida de peso (5–10%) puede mejorar mucho su salud."
    }
}


#make function to pull translation
def get_text(key, language):
    return translations[key][language]

st.title(get_text("page_title", language))
st.markdown('-----')

tab1, tab2, tab3, tab4 = st.tabs(['Underweight', 'Normal', 'Overweight', 'Obese'])

with tab1:
    st.title(get_text("bmi_category_underweight", language))
    st.subheader(get_text("what_it_means", language))
    st.text(get_text("underweight_meaning_1", language))

    st.subheader(get_text("what_you_can_do", language))
    for line in get_text("underweight_tips", language).split("\n"):
        st.markdown(line)

    st.subheader(get_text("your_goal", language))
    st.markdown(get_text("underweight_goal", language))

    st.markdown('------')

    st.subheader(get_text("sources", language))
    st.markdown("CDC. (2024, May 20). Body mass index (BMI): Adult BMI categories. Centers for Disease Control and Prevention. Retrieved June 25, 2025, from https://www.cdc.gov/bmi/index.html")
    st.markdown("Mayo Clinic Staff. (2024). Underweight? See how to add pounds healthfully. Mayo Clinic. Retrieved June 25, 2025, from https://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/expert-answers/underweight/faq-20058429")
    st.markdown("Office on Women’s Health. (2021). Underweight. U.S. Department of Health and Human Services. Retrieved June 25, 2025, from https://www.womenshealth.gov/healthy-weight/underweight")
    st.markdown("Mayo Clinic Staff. (2023). Unexplained weight loss—Causes. Mayo Clinic. Retrieved June 25, 2025, from https://www.mayoclinic.org/symptoms/unexplained-weight-loss/basics/causes/sym-20050700")

with tab2:
    st.title(get_text("bmi_category_normal", language))
    st.subheader(get_text("what_it_means", language))
    st.text(get_text("normal_meaning", language))

    st.subheader(get_text("what_you_can_do", language))
    for line in get_text("normal_tips", language).split("\n"):
        st.markdown(line)

    st.subheader(get_text("your_goal", language))
    st.markdown(get_text("normal_goal", language))

    st.markdown('------')

    st.subheader(get_text("sources", language))
    st.markdown("CDC. (2024, May 20). Body mass index (BMI): Adult BMI categories. Centers for Disease Control and Prevention. Retrieved June 25, 2025, from https://www.cdc.gov/bmi/adult-calculator/bmi-categories.html")
    st.markdown("CDC. (2024). About BMI. Centers for Disease Control and Prevention. Retrieved June 25, 2025, from https://www.cdc.gov/bmi/about/index.html")

with tab3:
    st.title(get_text("bmi_category_overweight", language))
    st.subheader(get_text("what_it_means", language))
    st.text(get_text("overweight_meaning", language))

    st.subheader(get_text("what_you_can_do", language))
    for line in get_text("overweight_tips", language).split("\n"):
        st.markdown(line)

    st.subheader(get_text("your_goal", language))
    st.markdown(get_text("overweight_goal", language))

    st.markdown('------')

    st.subheader(get_text("sources", language))
    st.markdown("CDC. (2024, May 20). Body mass index (BMI): Adult BMI categories. Centers for Disease Control and Prevention. Retrieved June 25, 2025, from https://www.cdc.gov/bmi/adult-calculator/bmi-categories.html")
    st.markdown("Health.com. (2025, May). The difference between being overweight and obese. Health. Retrieved June 25, 2025, from https://www.health.com/overweight-vs-obese-11708497")
    st.markdown("Wikipedia contributors. (2025, June). Overweight. In Wikipedia, The Free Encyclopedia. Retrieved June 25, 2025, from https://en.wikipedia.org/wiki/Overweight")

with tab4:
    st.title(get_text("bmi_category_obese", language))
    st.subheader(get_text("what_it_means", language))
    st.text(get_text("obese_meaning", language))

    st.subheader(get_text("what_you_can_do", language))
    for line in get_text("obese_tips", language).split("\n"):
        st.markdown(line)

    st.subheader(get_text("your_goal", language))
    st.markdown(get_text("obese_goal", language))

    st.markdown('------')

    st.subheader(get_text("sources", language))
    st.markdown("Mayo Clinic. (2023). Obesity – symptoms and causes. Mayo Clinic. Retrieved June 25, 2025, from https://www.mayoclinic.org/diseases-conditions/obesity/symptoms-causes/syc-20375742")
    st.markdown("CDC. (2024). BMI Frequently Asked Questions. Centers for Disease Control and Prevention. Retrieved June 25, 2025, from https://www.cdc.gov/bmi/faq/index.html")
    st.markdown("Wikipedia contributors. (2025, June). Obesity. In Wikipedia, The Free Encyclopedia. Retrieved June 25, 2025, from https://en.wikipedia.org/wiki/Obesity")
    st.markdown("Health.com. (2025, May). The difference between being overweight and obese. Health. Retrieved June 25, 2025, from https://www.health.com/overweight-vs-obese-11708497")
