import streamlit as st

def show_statistical_summary(statistical_summary: dict):

    st.markdown("---")
    st.subheader("Resumen Estadístico")
    
    # Crear 3 columnas
    col1, col2, col3 = st.columns(3)
    
    # col estatura
    with col1:
        st.markdown("Estatura (cm)")
        st.metric(label="Media", value=f"{statistical_summary['Estatura_CM']['media']:.2f}")
        st.metric(label="Mediana", value=f"{statistical_summary['Estatura_CM']['mediana']:.2f}")
        st.metric(label="Mínimo", value=f"{statistical_summary['Estatura_CM']['minimo']:.2f}")
        st.metric(label="Máximo", value=f"{statistical_summary['Estatura_CM']['maximo']:.2f}")
        st.metric(label="Rango", value=f"{statistical_summary['Estatura_CM']['rango']:.2f}")
    
    # col peso
    with col2:
        st.markdown("Peso (kg)")
        st.metric(label="Media", value=f"{statistical_summary['Peso']['media']:.2f}")
        st.metric(label="Mediana", value=f"{statistical_summary['Peso']['mediana']:.2f}")
        st.metric(label="Mínimo", value=f"{statistical_summary['Peso']['minimo']:.2f}")
        st.metric(label="Máximo", value=f"{statistical_summary['Peso']['maximo']:.2f}")
        st.metric(label="Rango", value=f"{statistical_summary['Peso']['rango']:.2f}")
    
    # col imc
    with col3:
        st.markdown("   IMC")
        st.metric(label="Media", value=f"{statistical_summary['IMC']['media']:.2f}")
        st.metric(label="Mediana", value=f"{statistical_summary['IMC']['mediana']:.2f}")
        st.metric(label="Mínimo", value=f"{statistical_summary['IMC']['minimo']:.2f}")
        st.metric(label="Máximo", value=f"{statistical_summary['IMC']['maximo']:.2f}")
        st.metric(label="Rango", value=f"{statistical_summary['IMC']['rango']:.2f}")