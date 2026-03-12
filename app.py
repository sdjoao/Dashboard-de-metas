from servicos.uploadData import carregar_arquivo
from servicos.calculos import calcular_percentual, calcular_metricas
import streamlit as st

dataFrame = carregar_arquivo("dados/metas.csv")
dataFrame= calcular_percentual(dataFrame)

metricas = calcular_metricas(dataFrame)

st.title("Dashboard de Metas")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Meta total", value=str(metricas['meta_total']))

with col2:
    st.metric(label="Realizado total", value=str(metricas['realizado_total']))

with col3:
    metrica_str = f"{metricas['percentual_final']:.2f}"
    st.metric(label="Percentual final", value=metrica_str)

st.dataframe(dataFrame)


