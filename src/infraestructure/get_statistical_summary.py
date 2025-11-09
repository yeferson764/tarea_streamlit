import pandas as pd

def get_statistical_summary(df: pd.DataFrame):
    
    # Obtiene el resumen estadístico
    
    statistical_summary = {
        'Estatura_CM': {
            'media': df['Estatura_CM'].mean(),
            'mediana': df['Estatura_CM'].median(),
            'minimo': df['Estatura_CM'].min(),
            'maximo': df['Estatura_CM'].max(),
            'rango': df['Estatura_CM'].max() - df['Estatura_CM'].min()
        },
        'Peso': {
            'media': df['Peso'].mean(),
            'mediana': df['Peso'].median(),
            'minimo': df['Peso'].min(),
            'maximo': df['Peso'].max(),
            'rango': df['Peso'].max() - df['Peso'].min()
        },
        'IMC': {
            'media': df['IMC'].mean(),
            'mediana': df['IMC'].median(),
            'minimo': df['IMC'].min(),
            'maximo': df['IMC'].max(),
            'rango': df['IMC'].max() - df['IMC'].min()
        }
    }
    
    return statistical_summary