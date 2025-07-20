
import streamlit as st
import pandas as pd
import numpy as np

# Título de la aplicación
st.title("📈 Análisis de Acciones Más Activas")
st.markdown("Esta aplicación muestra las 100 acciones con mayor movimiento del último día y recomendaciones automáticas.")

# Botón para actualizar datos
if st.button("🔄 Actualizar datos"):
    st.success("Datos actualizados correctamente (simulados).")

# Simulación de datos de acciones más activas
np.random.seed(42)
tickers = [f"ACC{i:03d}" for i in range(1, 101)]
data = {
    "Ticker": tickers,
    "Precio Actual": np.round(np.random.uniform(10, 500, 100), 2),
    "Variación (%)": np.round(np.random.uniform(-5, 5, 100), 2),
    "Volumen": np.random.randint(100000, 5000000, 100)
}
df = pd.DataFrame(data)

# Mostrar tabla de acciones
st.subheader("📊 Top 100 Acciones Más Activas")
st.dataframe(df)

# Recomendaciones: acciones con variación positiva mayor al 2%
recomendadas = df[df["Variación (%)"] > 2].sort_values(by="Variación (%)", ascending=False).head(10)

st.subheader("✅ Recomendaciones Destacadas")
if not recomendadas.empty:
    st.dataframe(recomendadas)
else:
    st.info("No hay recomendaciones destacadas en este momento.")
