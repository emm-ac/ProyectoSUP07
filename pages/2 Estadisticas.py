import streamlit as st
import psycopg2

st.set_page_config(page_title='Estadísticas', 
                   page_icon='📊', 
                   layout="centered", 
                   initial_sidebar_state="collapsed", 
                   menu_items=None)


st.title('Estadísticas TA Tools')
st.text('Indicadores de tu grupo')
    

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()


## Perform query.
## Uses st.experimental_memo to only rerun when the query changes or after 10 min.
#@st.experimental_memo(ttl=600)
#def run_query(query):
#    with conn.cursor() as cur:
#        cur.execute(query)
#        return cur.fetchall()
#
#rows = run_query("SELECT * FROM Alumnos")                 
#
## Print results.
#for row in rows:
#    st.write(f"{row[0]} has a :{row[1]}:")
    



@st.experimental_memo(ttl=300)
def run_query2(query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


sql = run_query2('''SELECT * FROM Alumnos''')                 

# Print results.
for row in sql:
    st.write(f"{row[0]} has a :{row[1]}:")
  



#- edad promedio de alumnos, c la min y max
#- cant de alumnos por nacionalidad (barras)
#- dispositivo q ussn para conectarse al sup (ver porcentaje de cada c resp al total)
#- cant de alumnos q poseen tanto mic como cam
#- metrica con lo que preferirían hacer en el sup
#- relacionar la edad c que prefieren hacer en el sup
#- relacionar nacionalidad c pais de residencia
#- relacionar disp q usan con si tienen mic y cam o solo alguna de las dos