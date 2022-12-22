import streamlit as st
import psycopg2
import sqlite3 as sql
import pandas as pd

st.set_page_config(page_title='TA Tools - Dipositivos', 
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


#- dispositivo q ussn para conectarse al sup (ver porcentaje de cada c resp al total)
st.subheader('Dispositivos utilizados')
sql3 = (run_query("SELECT Nombre_apellido, Dispositivo_usado FROM Alumnos"))
st.markdown(f'Los alumnos se conectan utilizando:')
st.dataframe(data=sql3, use_container_width=True)
sql33 = (run_query("SELECT Dispositivo_usado, COUNT(Dispositivo_usado) as Total FROM Alumnos GROUP BY Dispositivo_usado"))
st.markdown(f'Y hay un total de:')
st.dataframe(sql33, use_container_width=True)