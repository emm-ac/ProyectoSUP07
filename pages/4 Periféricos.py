import streamlit as st
import psycopg2
import sqlite3 as sql
import pandas as pd

st.set_page_config(page_title='TA Tools - Periféricos', 
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


#- cant de alumnos q poseen tanto mic como cam
st.subheader('Uso de cámara y/o micrófono')
sql4 = (run_query("SELECT Cam_Mic, COUNT(Cam_Mic) FROM Alumnos GROUP BY Cam_Mic"))
st.markdown(f'Los alumnos tienen:')
st.dataframe(data=sql4, use_container_width=True)