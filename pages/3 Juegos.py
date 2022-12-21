import streamlit as st

st.set_page_config(page_title='Juegos', 
                   page_icon='🕹️', 
                   layout="centered", 
                   initial_sidebar_state="collapsed", 
                   menu_items=None)


# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()