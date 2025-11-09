import pandas as pd

def get_charts_data(df: pd.DataFrame, age_bins: list):
    
    # Prepara los datos necesarios para los graficos
    
    # 1- Distribución por edad
    age_distribution = pd.cut(df['Edad'], bins=age_bins).value_counts().sort_index()
    age_labels = [f"{int(interval.left)}-{int(interval.right)}" for interval in age_distribution.index]
    
    # 2- Distribución por tipo de sangre
    blood_type_distribution = df['RH'].value_counts()
    
    # 3- Datos para scatter
    scatter_data = {
        'estatura': df['Estatura_CM'].values,
        'peso': df['Peso'].values
    }
    
    # 4- Distribución por color de cabello
    hair_color_distribution = df['Color_Cabello'].value_counts()
    
    # 5- Distribución de tallas de zapatos
    shoe_size_distribution = df['Talla_Zapato'].value_counts().sort_index()
    
    # 6- Top 10 de barrios
    top_neighborhoods = df['Barrio_Residencia'].value_counts().head(10)
    
    return {
        'age_distribution': age_distribution,
        'age_labels': age_labels,
        'blood_type_distribution': blood_type_distribution,
        'scatter_data': scatter_data,
        'hair_color_distribution': hair_color_distribution,
        'shoe_size_distribution': shoe_size_distribution,
        'top_neighborhoods': top_neighborhoods
    }