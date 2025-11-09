import streamlit as st
import pandas as pd

def show_summary_stats(df: pd.DataFrame):
    st.subheader("Resumen Estadístico")

    # Seleccionamos solo las columnas relevantes
    cols = ['Estatura_CM', 'Peso', 'IMC']

    # Verificamos que existan las columnas necesarias
    existing_cols = [col for col in cols if col in df.columns]
    if not existing_cols:
        st.warning("No se encontraron las columnas necesarias para el resumen estadístico.")
        return

    # Obtenemos la tabla descriptiva
    summary = df[existing_cols].describe().T

    # Redondeamos los valores a dos decimales
    summary = summary.round(2)

    # Mostramos cada columna de resumen en tres partes
    c1, c2, c3 = st.columns(3)
    columns_list = [c1, c2, c3]

    # Ajustamos para que muestre una tabla por columna disponible
    for i, col in enumerate(existing_cols):
        with columns_list[i]:
            st.markdown(f"**{col}**")
            st.dataframe(summary.loc[[col]])
