import streamlit as st
import sqlite3 as sql
import os 

st.set_page_config(page_title='Juegos', 
                   page_icon='🕹️', 
                   layout="centered", 
                   initial_sidebar_state="collapsed", 
                   menu_items=None)


# Initialize connection.
# Uses st.experimental_singleton to only run once.


@st.experimental_memo(ttl=300)
def run_query2(query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


sql = run_query2('''SELECT * FROM Alumnos''')                 

# Print results.
for row in sql:
    st.write(f"{row[0]} has a :{row[1]}:")