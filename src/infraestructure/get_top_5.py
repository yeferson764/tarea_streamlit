import pandas as pd

def get_top_5(df: pd.DataFrame):
    
    # Top 5 mayor estatura
    top_5_height = df.nlargest(5, 'Estatura_CM')[['Código', 'Nombre_Estudiante', 'Apellido_Estudiante', 'Estatura_CM', 'Peso', 'Edad']]
    
    # Top 5 mayor peso
    top_5_weight = df.nlargest(5, 'Peso')[['Código', 'Nombre_Estudiante', 'Apellido_Estudiante', 'Peso', 'Estatura_CM', 'Edad']]
    
    return {
        'top_5_height': top_5_height,
        'top_5_weight': top_5_weight
    }