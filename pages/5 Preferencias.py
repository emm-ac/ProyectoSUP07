import streamlit as st
import psycopg2
import sqlite3 as sql
import pandas as pd

st.set_page_config(page_title='TA Tools - Preferencias', 
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


#- metrica con lo que preferirían hacer en el sup
st.subheader('Temas más elegidos para el SUP')
sql5 = (run_query("SELECT Actividad_preferida, COUNT(Actividad_preferida) FROM Alumnos GROUP BY Actividad_preferida"))
st.markdown(f'Los alumnos prefieren:')
st.dataframe(data=sql5, use_container_width=True)
sql55 = pd.DataFrame(run_query("SELECT Actividad_preferida FROM Alumnos"))
st.bar_chart(data=sql55, use_container_width=True)