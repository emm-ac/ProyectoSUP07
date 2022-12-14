import streamlit as st
import psycopg2
import sqlite3 as sql
import pandas as pd
import altair as alt

st.set_page_config(page_title='TA Tools - Perif茅ricos', 
                   page_icon='馃搳', 
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


header_style = '''
    <style>
        th{
            background-color: yellow;
        }
    </style>
'''
st.markdown(header_style, unsafe_allow_html=True)


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
st.subheader('Uso de c谩mara y/o micr贸fono')
sql4 = pd.DataFrame(run_query("SELECT mic, COUNT(mic) as Tot FROM alumno GROUP BY mic ORDER BY Tot DESC"))
sql4.columns = ['Micr贸fono','Cantidad']
st.table(sql4)


st.subheader(f'La distribuci贸n de perif茅ricos es la siguiente:')
graf = alt.Chart(sql4).mark_bar().encode(
    x='Micr贸fono', y='Cantidad', color= 'Micr贸fono', tooltip=['Micr贸fono', 'Cantidad']).properties(width=450).interactive()
st.altair_chart(graf, use_container_width=True)


st.subheader('Uso de c谩mara y/o micr贸fono')
sql44 = pd.DataFrame(run_query("SELECT cam, COUNT(cam) as Tot FROM alumno GROUP BY cam ORDER BY Tot DESC"))
sql44.columns = ['C谩mara','Cantidad']
st.table(sql44)


st.subheader(f'La distribuci贸n de perif茅ricos es la siguiente:')
graf = alt.Chart(sql44).mark_bar().encode(
    x='C谩mara', y='Cantidad', color= 'C谩mara', tooltip=['C谩mara', 'Cantidad']).properties(width=450).interactive()
st.altair_chart(graf, use_container_width=True)