import streamlit as st
import psycopg2
import sqlite3 as sql
import pandas as pd

st.set_page_config(page_title='TA Tools - Edad c/ Preferencia', 
                   page_icon='📊', 
                   layout="centered", 
                   initial_sidebar_state="collapsed", 
                   menu_items=None)


st.header('Indicadores de tu grupo')
    

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()


@st.experimental_memo(ttl=600)
def run_query(query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


#- relacionar la edad c que prefieren hacer en el sup
st.subheader('Edad y preferencias')
sql6 = (run_query("SELECT Nombre_apellido,Edad,Actividad_preferida FROM Alumnos ORDER BY Edad"))
st.markdown(f'En función de la edad, los alumnos prefieren:')
st.dataframe(data=sql6, use_container_width=True)