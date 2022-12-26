import streamlit as st
import psycopg2
import sqlite3 as sql
import pandas as pd

st.set_page_config(page_title='TA Tools - Periféricos', 
                   page_icon='📊', 
                   layout="centered", 
                   initial_sidebar_state="collapsed", 
                   menu_items=None)


# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)


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
sql4 = pd.DataFrame(run_query("SELECT Cam_Mic, COUNT(Cam_Mic) FROM Alumnos GROUP BY Cam_Mic"))
sql4.columns = ['Periférico','Cantidad']
st.table(sql4)


st.subheader(f'La distribución de periféricos es la siguiente:')
sql44 = pd.DataFrame(run_query("SELECT Dispositivo_usado, COUNT(Dispositivo_usado) FROM Alumnos GROUP BY Dispositivo_usado"))
st.bar_chart(data=sql4, x='Periférico', y='Cantidad', use_container_width=True)