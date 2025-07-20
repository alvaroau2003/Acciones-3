
import streamlit as st
import pandas as pd

# Simulación de datos de acciones más activas
acciones = pd.DataFrame({
    'Ticker': ['AAPL', 'TSLA', 'AMZN', 'NVDA', 'MSFT'],
    'Nombre': ['Apple Inc.', 'Tesla Inc.', 'Amazon.com Inc.', 'NVIDIA Corporation', 'Microsoft Corporation'],
    'Precio': [189.5, 245.3, 132.7, 456.2, 310.8],
    'Variación %': [1.2, -0.5, 2.1, 3.4, -1.0],
    'Volumen': [120_000_000, 98_000_000, 87_000_000, 76_000_000, 65_000_000]
})

# Filtrar recomendaciones (por ejemplo, variación positiva)
recomendadas = acciones[acciones['Variación %'] > 0].sort_values(by='Variación %', ascending=False)

# Interfaz de Streamlit
st.set_page_config(page_title="Análisis de Acciones", layout="wide")
st.title("📈 Análisis de Acciones Más Activas")
st.markdown("Esta aplicación muestra las acciones más activas y recomendaciones basadas en su variación diaria.")

# Botón para actualizar (simulado)
if st.button("🔄 Actualizar datos"):
    st.success("Datos actualizados correctamente (simulados).")

# Mostrar tabla de acciones más activas
st.subheader("🔥 Top Acciones Más Activas")
st.dataframe(acciones, use_container_width=True)

# Mostrar recomendaciones
st.subheader("✅ Recomendaciones (Variación positiva)")
st.dataframe(recomendadas, use_container_width=True)
