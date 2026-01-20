#Tratamiento de datos
import pandas as pd

def eda_preliminar(df):

    """
    Realiza un análisis exploratorio preliminar sobre un DataFrame dado.

    Este análisis incluye:
    - Muestra aleatoriamente 5 filas del DataFrame.
    - Información general del DataFrame (tipo datos, nulos, etc).
    - Porcentaje de valores nulos por columna.
    - Conteo de filas duplicadas.
    - Distribución de valores para cada columna categóorica.

    Parameters:
    df(pd.DataFrame): DataFrame a analizar.

    Returns:
    None

    """

    display(df.sample(5))

    print('--------')

    print('RESUMEN DE DATOS')
    print(f"Nuestro conjunto de datos presenta un total de {df.shape[0]} filas y {df.shape[1]} columnas")

    print('--------')

    print('INFO')
    columnas_por_tipo = {
    str(dtype): df.select_dtypes(include=[dtype]).columns.tolist()
    for dtype in df.dtypes.unique()}

    print("Los tipos de las columnas son:")
    display(df.dtypes.to_frame(name="tipo_dato"))

    print("\nColumnas agrupadas por tipo de dato:")
    for tipo, columnas in columnas_por_tipo.items():
        print(f"- {tipo}: {columnas}")

    print("\n-----------------\n")

    print('NULOS')
    df_nulos = pd.DataFrame({"count":df.isnull().sum(),
                             "% nulos": ((df.isnull().sum() / df.shape[0])*100).round(3)}).sort_values(by="% nulos", ascending=False)
    df_nulos = df_nulos[df_nulos["count"] > 0]
    df_nulos_sorted = df_nulos.sort_values(by="% nulos", ascending=False)
    print("Los nulos que tenemos en el conjunto de datos son:")
    display(df_nulos_sorted)
    
    print('--------')
    print('DUPLICADOS')
    print(f"Tenemos un total de {df.duplicated().sum()} duplicados")

    print('--------')
    print('FRECUENCIA CATEGORICAS')
    for col in df.select_dtypes(include='O').columns:
        print(col.upper())
        print(df[col].value_counts())
        print('-------')
    
    print('--------')
    print('ESTADISTICOS NUMERICOS')
    display(df.describe().T)
