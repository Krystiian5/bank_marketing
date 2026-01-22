import pandas as pd

def minus(df):

    """
    Convierte a minúsculas los valores de todas las columnas categóricas de un DataFrame.

    Recorre cada columna de tipo objeto en el DataFrame y convierte sus valores a minúsculas, 
    facilitando el análisis de datos sin distinción de mayúsculas y minúsculas.

    Parameters:
    df (pd.DataFrame): DataFrame en el cual se procesarán las columnas categóricas.

    Returns:
    None
    """
    for col in df.select_dtypes(include='O').columns:
        df[col] = df[col].str.lower()

def comas (df):

    """
    Reemplaza comas con puntos en columnas específicas de un DataFrame.

    Para cada columna en la lista proporcionada, convierte las comas (',') a puntos ('.'), 
    facilitando el análisis de datos numéricos en sistemas que utilizan el punto como separador decimal.

    Parameters:
    df (pd.DataFrame): DataFrame que contiene las columnas a procesar.
    lista_col (list of str): Lista con los nombres de las columnas en las que se deben reemplazar comas por puntos.

    Returns:
    None
    """
    for col in df.select_dtypes(include='O'):
        df[col] = df[col].str.replace(',','.')
        try:
            df[col] = df[col].astype('float64')
        except:
            pass

def transformar_booleanos(df, columnas):
    """
    Transforma columnas con valores 0/1 en variables categóricas 'Yes'/'No'
    y reemplaza los valores nulos por 'unknown'.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame a modificar.
    columnas : list
        Lista de columnas a transformar.

    Returns
    -------
    pd.DataFrame
        DataFrame con las columnas transformadas.
    """

    map_bool = {
        1.0: 'Yes',
        0.0: 'No'
    }

    for col in columnas:
        df[col] = (
            df[col]
            .map(map_bool)
            .fillna('unknown')
            .astype('object')
        )

    return df

def limpiar_fecha(df, columna):
    """
    Traduce los meses en español a inglés y convierte una columna a tipo datetime.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame que contiene la columna de fecha.
    columna : str
        Nombre de la columna de fecha.

    Returns
    -------
    pd.DataFrame
        DataFrame con la columna transformada a datetime.
    """

    meses_es_en = {
        'enero': 'january',
        'febrero': 'february',
        'marzo': 'march',
        'abril': 'april',
        'mayo': 'may',
        'junio': 'june',
        'julio': 'july',
        'agosto': 'august',
        'septiembre': 'september',
        'octubre': 'october',
        'noviembre': 'november',
        'diciembre': 'december'
    }

    df[columna] = (
        df[columna]
        .astype(str)
        .str.lower()
        .replace(meses_es_en, regex=True)
    )

    df[columna] = pd.to_datetime(df[columna], format='%d-%B-%Y', errors='coerce')

    return df