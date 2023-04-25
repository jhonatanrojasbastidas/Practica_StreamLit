import pandas as pd
import streamlit as st

# 
st.title("Ventas de videojuegos")

# Invocamos el dataframe
data = pd.read_csv('vgsales.csv')
df = pd.DataFrame(data)
df

# Método para seleccionar el mes y el día.
Genre = st.selectbox('Genre',(df["Genre"].sort_values(ascending=True).unique()))  
Platform = st.selectbox('Platform',(df["Platform"].sort_values(ascending=True).unique()))   
Year = st.selectbox('Year',(df["Year"].sort_values(ascending=True).unique()))   

filtro = (df['Genre'] == Genre) & (df['Platform'] ==Platform) & (df['Year'] ==Year)

# 
df_filtrado = df.loc[filtro] 

df = pd.DataFrame(
    df_filtrado)

df