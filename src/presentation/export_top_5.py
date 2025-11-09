import streamlit as st
import pandas as pd
from io import BytesIO

def export_top_5(top_5_data: dict):

    #Exporta los top 5 de mayor estatura y mayor peso
    
    st.markdown("---")
    st.subheader("Top 5 - Exportación de Datos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("Top 5 Mayor Estatura")
        st.dataframe(top_5_data['top_5_height'], width='stretch')
        
        # Generar archivo excel
        excel_buffer = BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
            top_5_data['top_5_height'].to_excel(writer, index=False, sheet_name='Top 5 Estatura')
        excel_buffer.seek(0)
        
        st.download_button(
            label="📊 Descargar Excel",
            data=excel_buffer,
            file_name="Top5_MayorEstatura.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    
    with col2:
        st.markdown("Top 5 Mayor Peso")
        st.dataframe(top_5_data['top_5_weight'], width='stretch')
        
        # Generar archivo excel
        excel_buffer = BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
            top_5_data['top_5_weight'].to_excel(writer, index=False, sheet_name='Top 5 Peso')
        excel_buffer.seek(0)
        
        st.download_button(
            label="📊 Descargar Excel",
            data=excel_buffer,
            file_name="Top5_MayorPeso.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )