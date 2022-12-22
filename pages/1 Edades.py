import streamlit as st
import psycopg2
import sqlite3 as sql
import pandas as pd

st.set_page_config(page_title='TA Tools - Edades', 
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


#- edad promedio de alumnos, c la min y max
st.subheader('Edades de los alumnos') 
sql1 = run_query("SELECT ROUND(AVG(edad),0) FROM Alumnos")            
st.markdown(f'La edad promedio de los alumnos es: {sql1[0][0]}')
sql11 = run_query("SELECT MIN(edad) , MAX(edad) FROM Alumnos")  
st.markdown(f'Siendo {sql11[0][0]} la menor y {sql11[0][1]} la mayor')