import streamlit as st
import psycopg2


st.title('Estadísticas TA Tools')
st.text('Indicadores de tu grupo')
    

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("CREATE TABLE 'Prueba;")
                 

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")

#st.set_page_config(page_title='Estadísticas', 
#                   page_icon='📊', 
#                   layout="centered", 
#                   initial_sidebar_state="collapsed", 
#                   menu_items=None)
#
#
## Initialize connection.
#st.experimental_singleton#(allow_outup_mutation=True)
#def connect_db():
#   try:
#      con = pyodbc.connect(
#      driver = 'ODBC DRIVER 17 FOR SQL SERVER',
#      Server = 'babar.db.elephantsql.com',
#      Port = 5432,
#      DATABASE='xtoaygsy',
#      UID = 'xtoaygsy',
#      PWD ='DRLk6LMdY9G5qH_72fYzLI4-GGkrG0rd',
#      )
#      cursor = con.cursor()
#      df = pd.read_sql_query('select * from test_db',con)
#      data = df
#   except Exception as e:
#      st.write("error is :{}".format(e))
#   return data

#def main():
  # call connect_db in order to use it parameters in latter queries

    

#  connect_db()
## Uses st.experimental_singleton to only run once.
#@st.experimental_singleton
#def init_connection():
#    return psycopg2.connect(**st.secrets["postgres"])
#
#conn = init_connection()
#
## Perform query.
## Uses st.experimental_memo to only rerun when the query changes or after 10 min.
#@st.experimental_memo(ttl=600)
#def run_query(query):
#    with conn.cursor() as cur:
#        cur.execute(query)
#        return cur.fetchall()
#
#rows = run_query("SELECT * from mytable;")
#
## Print results.
#for row in rows:
#    st.write(f"{row[0]} has a :{row[1]}:")