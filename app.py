import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Encabezado
st.title('Anlisis de autos en el lote')

# 2. Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# 3. Checkbox: filtro de autos 4WD

build_4wd_filter = st.checkbox('Mostrar solo autos 4WD')

if build_4wd_filter:
    filtered_data = car_data[car_data['is_4wd'] == 1.0]
else:
    filtered_data = car_data

# 4. Histograma: precios

st.subheader('Distribucin de Precios de Autos')
fig_hist = px.histogram(filtered_data, x='price',
                        nbins=30, title='Distribucin de Precios')
st.plotly_chart(fig_hist)

# 5. Dispersion: precio vs odometro

st.subheader('Precio vs Kilometraje')
fig_scatter = px.scatter(filtered_data, x='odometer', y='price',
                         title='Precio vs Kilometraje',
                         labels={'odometer': 'Kilometraje', 'price': 'Precio'})
st.plotly_chart(fig_scatter)

# 6. Barras: condicion del vehiculo
st.subheader('Condicin del Vehculo')
cond_counts = filtered_data['condition'].value_counts().reset_index()
cond_counts.columns = ['condition', 'count']  # renombrar las columnas

fig_bar = px.bar(
    cond_counts,
    x='condition',
    y='count',
    labels={'condition': 'Condicion', 'count': 'Nmero de Autos'},
    title='Nmero de Autos por Condicin'
)
st.plotly_chart(fig_bar)
