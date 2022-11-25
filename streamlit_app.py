
# streamlit_app.py

import streamlit as st
import psycopg2

# Initialize connection.
# Uses st.experimental_singleton to only run once.
#@st.experimental_singleton
#def init_connection():
#    return psycopg2.connect(**st.secrets["postgres"])
#
#conn = init_connection()


# create database connection
@st.cache(allow_output_mutation=True)
def get_database_connection():
    conn = sqlite3.connect('sup_db')
    c = conn.cursor()   
    return c

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from Usuario;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")