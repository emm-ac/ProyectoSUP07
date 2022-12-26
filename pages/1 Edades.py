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
sql1 = run_query("SELECT ROUND(AVG(edad),0) FROM Alumnos")
sql11 = run_query("SELECT MIN(edad) , MAX(edad) FROM Alumnos")  

col1, col2, col3 = st.columns(3)
col1.metric(label="Menor", value=int(sql11[0][0]), delta=None)
col2.metric(label="Edad promedio", value=int(sql1[0][0]), delta=None)
col3.metric(label="Mayor", value=int(sql11[0][1]), delta=None)


st.subheader('Edades de los alumnos')
sql111 = pd.DataFrame(run_query("SELECT Nombre_apellido, edad FROM Alumnos"))
sql111.columns = ['Nombre','Edad']
#sql111 = sql111.set_index(None)
st.dataframe(data=sql111, use_container_width=True)


