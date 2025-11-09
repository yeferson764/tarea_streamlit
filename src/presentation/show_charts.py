import streamlit as st
import matplotlib.pyplot as plt

def show_charts(charts_data: dict):

    #Muestra los graficos en la interfaz de streamlit
    
    st.markdown("---")
    st.subheader("📊 Gráficos Estadísticos")
    
    # FILA1: barras (edad) --- torta (tipo de sangre)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Distribución por Edad")
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(range(len(charts_data['age_distribution'])), 
               charts_data['age_distribution'].values, 
               color='steelblue', edgecolor='black')
        ax.set_xlabel('Rango de Edad', fontsize=12, fontweight='bold')
        ax.set_ylabel('Cantidad de Estudiantes', fontsize=12, fontweight='bold')
        ax.set_xticks(range(len(charts_data['age_labels'])))
        ax.set_xticklabels(charts_data['age_labels'], rotation=45, ha='right')
        plt.tight_layout()
        st.pyplot(fig)
    
    with col2:
        st.markdown("#### Distribución por Tipo de Sangre")
        fig, ax = plt.subplots(figsize=(8, 5))
        colors = plt.cm.Set3(range(len(charts_data['blood_type_distribution'])))
        ax.pie(charts_data['blood_type_distribution'].values,
               labels=charts_data['blood_type_distribution'].index,
               autopct='%1.1f%%',
               colors=colors,
               startangle=90)
        ax.set_title('Porcentaje por Tipo de Sangre', fontsize=12, fontweight='bold', pad=20)
        plt.tight_layout()
        st.pyplot(fig)
    
    # FILA2: scatter (estatura vs peso) --- barras (color de cabello)
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("#### Relación Estatura vs Peso")
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.scatter(charts_data['scatter_data']['estatura'], 
                   charts_data['scatter_data']['peso'],
                   alpha=0.6, s=100, color='coral', edgecolors='black')
        ax.set_xlabel('Estatura (cm)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Peso (kg)', fontsize=12, fontweight='bold')
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        st.pyplot(fig)
    
    with col4:
        st.markdown("#### Distribución por Color de Cabello")
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.barh(range(len(charts_data['hair_color_distribution'])), 
                charts_data['hair_color_distribution'].values,
                color='mediumseagreen', edgecolor='black')
        ax.set_yticks(range(len(charts_data['hair_color_distribution'])))
        ax.set_yticklabels(charts_data['hair_color_distribution'].index)
        ax.set_xlabel('Cantidad de Estudiantes', fontsize=12, fontweight='bold')
        ax.set_title('Color de Cabello', fontsize=12, fontweight='bold')
        plt.tight_layout()
        st.pyplot(fig)
    
    # FILA3: linea (tallas de zapatos) --- barras (top 10 barrios)
    col5, col6 = st.columns(2)
    
    with col5:
        st.markdown("#### Distribución de Tallas de Zapatos")
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(range(len(charts_data['shoe_size_distribution'])), 
                charts_data['shoe_size_distribution'].values,
                marker='o', linewidth=2, markersize=8, color='purple', alpha=0.7)
        ax.fill_between(range(len(charts_data['shoe_size_distribution'])), 
                        charts_data['shoe_size_distribution'].values,
                        alpha=0.3, color='purple')
        ax.set_xlabel('Talla de Zapatos', fontsize=12, fontweight='bold')
        ax.set_ylabel('Cantidad de Estudiantes', fontsize=12, fontweight='bold')
        ax.set_xticks(range(len(charts_data['shoe_size_distribution'])))
        ax.set_xticklabels(charts_data['shoe_size_distribution'].index, rotation=45, ha='right')
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        st.pyplot(fig)
    
    with col6:
        st.markdown("#### Top 10 Barrios de Residencia")
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.barh(range(len(charts_data['top_neighborhoods'])), 
                charts_data['top_neighborhoods'].values,
                color='darkorange', edgecolor='black')
        ax.set_yticks(range(len(charts_data['top_neighborhoods'])))
        ax.set_yticklabels(charts_data['top_neighborhoods'].index)
        ax.set_xlabel('Cantidad de Estudiantes', fontsize=12, fontweight='bold')
        ax.set_title('Top 10 Barrios', fontsize=12, fontweight='bold')
        plt.tight_layout()
        st.pyplot(fig)