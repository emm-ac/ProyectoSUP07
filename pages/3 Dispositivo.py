import streamlit as st
import psycopg2
import sqlite3 as sql
import pandas as pd

st.set_page_config(page_title='TA Tools - Dipositivos', 
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


#- dispositivo q ussn para conectarse al sup (ver porcentaje de cada c resp al total)
st.subheader('Dispositivos utilizados')
sql3 = pd.DataFrame(run_query("SELECT Nombre_apellido, Dispositivo_usado FROM Alumnos"))
sql3.columns = ['Alumno','Dispositivo']
st.table(sql3)


st.subheader(f'La distribución de dispositivos es la siguiente:')
#sql33 = pd.DataFrame(run_query("SELECT Dispositivo_usado, COUNT(Dispositivo_usado) FROM Alumnos GROUP BY Dispositivo_usado"))
#st.write(sql33)

#sql33.columns = ['Dispositivo','Cantidad']
#st.table(sql33)



#st.bar_chart(data=sql33, x='Dispositivo', y='Total', use_container_width=True)