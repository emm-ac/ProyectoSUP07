import streamlit as st
import psycopg2
import sqlite3 as sql
import pandas as pd

st.set_page_config(page_title='TA Tools - Nacionalidad', 
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


#- cant de alumnos por nacionalidad (barras)
st.subheader('Nacionalidades')
st.markdown(f'La distribución de nacionalidades es la siguiente:')
sql2 = pd.DataFrame(run_query("SELECT COUNT(IDAlumno) FROM Alumnos GROUP BY país"))


st.markdown(sql2)
#sql2 = sql2(columns=('País','Cantidad'))
st.write(sql2)
st.dataframe(data=sql2, use_container_width=True)
st.bar_chart(data=sql2, use_container_width=True)


st.subheader('Edades de los alumnos')
sql111 = pd.DataFrame(run_query("SELECT Nombre_apellido, edad FROM Alumnos"))
sql111.columns = ['Nombre','Edad']
sql111.style.hide_index()


# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)
# Display a static table
st.table(sql111)