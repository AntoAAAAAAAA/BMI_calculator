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