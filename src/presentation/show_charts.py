import streamlit as st
import plotly.express as px
import pandas as pd

def show_all_charts(df: pd.DataFrame):
    st.subheader("Visualizaciones del Dashboard")

    # Fila 1 
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Distribución por Edad**")
        fig_age = px.histogram(df, x="Edad", nbins=10, color_discrete_sequence=["#5A31B5"])
        fig_age.update_layout(xaxis_title="Edad", yaxis_title="Cantidad de Estudiantes")
        #st.plotly_chart(fig_age, use_container_width=True)
        st.plotly_chart(fig_age, width="stretch")


    with col2:
        st.markdown("**Distribución por Tipo de Sangre (RH)**")
        fig_blood = px.pie(df, names="RH", title="Tipo de Sangre", color_discrete_sequence=px.colors.qualitative.Set3)
        #st.plotly_chart(fig_blood, use_container_width=True)
        st.plotly_chart(fig_blood, width="stretch")


    # Fila 2
    col3, col4 = st.columns(2)

    with col3:
        st.markdown("**Relación Estatura vs Peso**")
        fig_scatter = px.scatter(df, x="Estatura_CM", y="Peso", color="Sexo" if "Sexo" in df.columns else None,
                                 trendline="ols", color_discrete_sequence=["#4B72BF", "#FFD252"])
        fig_scatter.update_layout(xaxis_title="Estatura (cm)", yaxis_title="Peso (kg)")
        #st.plotly_chart(fig_scatter, use_container_width=True)
        st.plotly_chart(fig_scatter, width="stretch")

    with col4:
        st.markdown("**Distribución por Color de Cabello**")
        color_counts = df["Color_Cabello"].value_counts().reset_index()
        color_counts.columns = ["Color_Cabello", "Cantidad"]
        fig_hair = px.bar(color_counts, x="Color_Cabello", y="Cantidad", color="Color_Cabello",
                          color_discrete_sequence=px.colors.qualitative.Bold)
        fig_hair.update_layout(xaxis_title="Color de Cabello", yaxis_title="Cantidad de Estudiantes", showlegend=False)
        #st.plotly_chart(fig_hair, use_container_width=True)
        st.plotly_chart(fig_hair, width="stretch")

    # Fila 3
    col5, col6 = st.columns(2)

    with col5:
        st.markdown("**Distribución de Tallas de Zapatos**")
        if "Talla_Zapato" in df.columns:
            size_counts = df["Talla_Zapato"].value_counts().sort_index().reset_index()
            size_counts.columns = ["Talla_Zapato", "Cantidad"]
            fig_size = px.line(size_counts, x="Talla_Zapato", y="Cantidad", markers=True,
                               color_discrete_sequence=["#013A51"])
            fig_size.update_layout(xaxis_title="Talla de Zapato", yaxis_title="Cantidad de Estudiantes")
            #st.plotly_chart(fig_size, use_container_width=True)
            st.plotly_chart(fig_size, width="stretch")
        else:
            st.info("No se encontró la columna 'Talla_Zapato' en el archivo.")

    with col6:
        st.markdown("**Top 10 Barrios de Residencia**")
        barrio_counts = df["Barrio_Residencia"].value_counts().head(10).reset_index()
        barrio_counts.columns = ["Barrio_Residencia", "Cantidad"]
        fig_barrio = px.bar(barrio_counts, x="Barrio_Residencia", y="Cantidad", color="Barrio_Residencia",
                            color_discrete_sequence=px.colors.qualitative.Pastel)
        fig_barrio.update_layout(xaxis_title="Barrio", yaxis_title="Cantidad de Estudiantes", showlegend=False)
        #st.plotly_chart(fig_barrio, use_container_width=True)
        st.plotly_chart(fig_barrio, width="stretch")
