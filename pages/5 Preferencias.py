import streamlit as st
import psycopg2
import sqlite3 as sql
import pandas as pd

st.set_page_config(page_title='TA Tools - Preferencias', 
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


#- metrica con lo que preferirían hacer en el sup
st.subheader('Temas más elegidos para el SUP')
sql5 = pd.DataFrame(run_query("SELECT gustos_sup, COUNT(gustos_sup) FROM alumno GROUP BY gustos_sup"))
sql5.columns = ['Actividad','Cantidad']
st.table(sql5)


st.subheader(f'La distribución de preferencias es la siguiente:')
st.bar_chart(data=sql5, x='Actividad', y='Cantidad', use_container_width=True)