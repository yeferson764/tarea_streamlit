import pandas as pd
import os

def save_top_five(df: pd.DataFrame):
    # Crear carpeta outputs si no existe
    output_dir = "./outputs"
    os.makedirs(output_dir, exist_ok=True)

    # Validar que existan las columnas necesarias
    if "Estatura_CM" not in df.columns or "Peso" not in df.columns:
        print("No se encontraron las columnas 'Estatura_CM' o 'Peso' en el DataFrame.")
        return

    # Obtener los Top 5
    top_estatura = df.nlargest(5, "Estatura_CM")
    top_peso = df.nlargest(5, "Peso")

    # Rutas de guardado
    path_estatura = os.path.join(output_dir, "top_5_estatura.xlsx")
    path_peso = os.path.join(output_dir, "top_5_peso.xlsx")

    # Guardar en archivos Excel
    try:
        top_estatura.to_excel(path_estatura, index=False)
        top_peso.to_excel(path_peso, index=False)
        print(f"Archivos generados correctamente en {output_dir}")
    except Exception as e:
        print(f"Error al guardar los archivos Excel: {e}")
