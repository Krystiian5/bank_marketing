#Visualizaciones
import matplotlib.pyplot as plt
import seaborn as sns



def visualizar_numericas_nulos(df):
    """
    Genera visualizaciones solo para columnas numéricas que tienen valores nulos.
    
    Para cada columna seleccionada se muestran:
    - Un histograma para analizar la distribución de los valores.
    - Un boxplot para detectar posibles outliers.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame que contiene las variables numéricas a analizar.

    Returns
    -------
    None
    """

    # Selecciona columnas numéricas
    col_nums = df.select_dtypes(include='number').columns
    # Filtra solo las que tienen nulos
    col_nums_nulos = [col for col in col_nums if df[col].isna().sum() > 0]

    # Si no hay columnas con nulos, imprimir mensaje y salir
    if len(col_nums_nulos) == 0:
        print("No hay columnas numéricas con nulos.")
        return

    n_rows = len(col_nums_nulos)

    fig, axes = plt.subplots(n_rows, 2, figsize=(15, 5 * n_rows))

    # Controlar el caso de una sola variable numérica
    if n_rows == 1:
        axes = [axes]

    for i, col in enumerate(col_nums_nulos):
        sns.histplot(df[col].dropna(), bins=200, ax=axes[i][0])
        axes[i][0].set_title(f'Distribución de {col}')
        axes[i][0].set_xlabel(col)
        axes[i][0].set_ylabel('Frecuencia')

        sns.boxplot(x=df[col].dropna(), ax=axes[i][1])
        axes[i][1].set_title(f'Boxplot de {col}')

    plt.tight_layout()
    plt.show()
