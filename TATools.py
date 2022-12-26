import streamlit as st

st.set_page_config(page_title='Inicio', 
                   page_icon='🚀', 
                   layout="centered", 
                   initial_sidebar_state="collapsed", 
                   menu_items=None)

st.title('TA Tools :rocket:')

st.header('Esta app proporciona herramientas e información útil para TAs.')

st.markdown('En el menú a tu izquierda puedes acceder a distintas métricas de tu grupo:')


st.markdown("""
    Saber qué distribución de edades tienen, sus nacionalidades,
    dispositivo con el que se conectan y los periféricos que disponen.
    También conocer qué temas prefieren hablar durante el SUP y algunos
    datos extra que pueden servirte. 
""")