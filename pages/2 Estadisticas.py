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
st.subheader('Edades de los alumnos') 
sql1 = run_query("SELECT ROUND(AVG(edad),0) FROM Alumnos")            
st.markdown(f'La edad promedio de los alumnos es: {sql1[0][0]}')
sql11 = run_query("SELECT MIN(edad) , MAX(edad) FROM Alumnos")  
st.markdown(f'Siendo {sql11[0][0]} la menor y {sql11[0][1]} la mayor')



#- cant de alumnos por nacionalidad (barras)
st.subheader('Nacionalidades')
sql2 = pd.DataFrame(run_query("SELECT COUNT(IDAlumno) FROM Alumnos GROUP BY país"))
st.dataframe(data=sql2, use_container_width=True)
st.bar_chart(data=sql2, use_container_width=True)



#- dispositivo q ussn para conectarse al sup (ver porcentaje de cada c resp al total)
st.subheader('Dispositivos utilizados')
sql3 = (run_query("SELECT Nombre_apellido, Dispositivo_usado FROM Alumnos"))
st.markdown(f'Los alumnos se conectan utilizando:')
st.dataframe(data=sql3, use_container_width=True)
sql33 = (run_query("SELECT Dispositivo_usado, COUNT(Dispositivo_usado) as Total FROM Alumnos GROUP BY Dispositivo_usado"))
st.markdown(f'Y hay un total de:')
st.dataframe(sql33, use_container_width=True)



#- cant de alumnos q poseen tanto mic como cam
st.subheader('Uso de cámara y/o micrófono')
sql4 = (run_query("SELECT Cam_Mic, COUNT(Cam_Mic) FROM Alumnos GROUP BY Cam_Mic"))
st.markdown(f'Los alumnos tienen:')
st.dataframe(data=sql4, use_container_width=True)



#- metrica con lo que preferirían hacer en el sup
st.subheader('Temas más elegidos para el SUP')
sql5 = (run_query("SELECT Actividad_preferida, COUNT(Actividad_preferida) FROM Alumnos GROUP BY Actividad_preferida"))
st.markdown(f'Los alumnos prefieren:')
st.dataframe(data=sql5, use_container_width=True)
sql55 = pd.DataFrame(run_query("SELECT Actividad_preferida FROM Alumnos"))
st.bar_chart(data=sql55, use_container_width=True)



#- relacionar la edad c que prefieren hacer en el sup
st.subheader('Edad y preferencias')
sql6 = (run_query("SELECT Nombre_apellido,Edad,Actividad_preferida FROM Alumnos ORDER BY Edad"))
st.markdown(f'En función de la edad, los alumnos prefieren:')
st.dataframe(data=sql6, use_container_width=True)



#- relacionar nacionalidad c pais de residencia



#- relacionar disp q usan con si tienen mic y cam o solo alguna de las dos
st.subheader('Dispositivos y conexión')
sql7 = (run_query("SELECT Nombre_apellido,Dispositivo_usado,Cam_Mic FROM Alumnos"))
st.markdown(f'En función del dispositivo, los alumnos se conectan usando:')
st.dataframe(data=sql7, use_container_width=True)
