import streamlit as st
import psycopg2
import sqlite3 as sql
import pandas as pd

st.set_page_config(page_title='TA Tools - Dispositivos c/ periféricos', 
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


#- relacionar disp q usan con si tienen mic y cam o solo alguna de las dos
st.subheader('Dispositivos y conexión')
sql7 = (run_query("SELECT Nombre_apellido,Dispositivo_usado,Cam_Mic FROM Alumnos"))
st.markdown(f'En función del dispositivo, los alumnos se conectan usando:')
st.dataframe(data=sql7, use_container_width=True)