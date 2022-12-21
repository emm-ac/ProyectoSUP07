import streamlit as st
import psycopg2
import sqlite3 as sql
import pandas as pd

st.set_page_config(page_title='Estadísticas', 
                   page_icon='📊', 
                   layout="centered", 
                   initial_sidebar_state="collapsed", 
                   menu_items=None)


st.title('Estadísticas TA Tools')
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


#- edad promedio de alumnos, c la min y max
sql1 = run_query("SELECT ROUND(AVG(edad),0) FROM Alumnos")
st.subheader('Edades de los alumnos')             
st.markdown(f'La edad promedio de los alumnos es: {sql1[0][0]}')
sql11 = run_query("SELECT MIN(edad) , MAX(edad) FROM Alumnos")  
st.markdown(f'Siendo {sql11[0][0]} la menor y {sql11[0][1]} la mayor')



#- cant de alumnos por nacionalidad (barras)
st.subheader('Nacionalidad de los alumnos')
sql2 = pd.DataFrame(run_query("SELECT país,COUNT(IDAlumno) FROM Alumnos GROUP BY país"))
st.dataframe(sql2)
st.bar_chart(data=sql2, x=None, y=None, width=600, height=200, use_container_width=False)





#- dispositivo q ussn para conectarse al sup (ver porcentaje de cada c resp al total)
#- cant de alumnos q poseen tanto mic como cam
#- metrica con lo que preferirían hacer en el sup
#- relacionar la edad c que prefieren hacer en el sup
#- relacionar nacionalidad c pais de residencia
#- relacionar disp q usan con si tienen mic y cam o solo alguna de las dos