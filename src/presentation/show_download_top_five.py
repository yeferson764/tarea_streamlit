import streamlit as st
import pandas as pd
from io import BytesIO

def show_download_top_five(df: pd.DataFrame):
    st.subheader("Top 5 Estudiantes por Estatura y Peso")

    # Generar los top 5 dinámicamente
    top_estatura = df.nlargest(5, "Estatura_CM")[["Código", "Nombre_Estudiante", "Apellido_Estudiante", "Estatura_CM", "Peso", "IMC"]]
    top_peso = df.nlargest(5, "Peso")[["Código", "Nombre_Estudiante", "Apellido_Estudiante", "Peso", "Estatura_CM", "IMC"]]

    # Mostrar tablas previas
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**🏆 Top 5 por Estatura (cm)**")
        st.dataframe(top_estatura, width="content")

    with col2:
        st.markdown("**🏋️‍♂️ Top 5 por Peso (kg)**")
        st.dataframe(top_peso, width="content")

    st.markdown("### Descargar Archivos Excel")

    # Convertir a Excel en memoria
    def to_excel_bytes(dataframe):
        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            dataframe.to_excel(writer, index=False)
        return buffer.getvalue()

    # Crear los botones de descarga
    col3, col4 = st.columns(2)
    with col3:
        st.download_button(
            label="⬇️ Descargar Top 5 por Estatura",
            data=to_excel_bytes(top_estatura),
            file_name="top_5_estatura.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    with col4:
        st.download_button(
            label="⬇️ Descargar Top 5 por Peso",
            data=to_excel_bytes(top_peso),
            file_name="top_5_peso.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
