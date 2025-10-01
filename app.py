import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
# boton para construir el histograma
hist_button = st.button('Construir Histograma')
if hist_button:  # al hacer click en el boton
    # escribir un mensaje
    st.write(
        'Creacion de histograma para el conjunto de datos de anuncios de venta de coches')

    # crear el histograma
    fig = px.histogram(car_data, x='odometer')

    # mostrar un grafico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
