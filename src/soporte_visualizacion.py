#Visualizaciones
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors

#Tratamiento de datos
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
import numpy as np




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

    col_nums = df.select_dtypes(include='number').columns
    col_nums_nulos = [col for col in col_nums if df[col].isna().sum() > 0]

    if len(col_nums_nulos) == 0:
        print("No hay columnas numéricas con nulos.")
        return

    n_rows = len(col_nums_nulos)

    fig, axes = plt.subplots(n_rows, 2, figsize=(15, 5 * n_rows))

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

# Histogramas de variables numéricas

def plot_hist(df, cols, bins=30):
    """
    Genera histogramas con KDE para variables numéricas.

    Permite analizar la distribución de cada columna numérica, detectar sesgos,
    rangos dominantes y posibles valores atípicos. 

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame que contiene las columnas a analizar.
    cols : list
        Lista de nombres de columnas numéricas que se van a graficar.
    bins : int, opcional
        Número de bins del histograma (por defecto 30).

    Returns
    -------
    None
    """
    for col in cols:
        plt.figure(figsize=(7, 4))
        
        sns.histplot(
            df[col],
            bins=bins,
            kde=True,
            color='#4C72B0',      
            edgecolor='white',    
            alpha=0.85
        )
        
        plt.title(f'Distribución de {col}', fontsize=13, fontweight='bold')
        plt.xlabel(col, fontsize=11)
        plt.ylabel('Frecuencia', fontsize=11)
        plt.grid(axis='y', linestyle='--', alpha=0.3) 
        
        plt.tight_layout()
        plt.show()

# Boxplots vs variable objetivo

def plot_box_vs_target(df, num_cols, target='y'):
    """
    Genera boxplots de variables numéricas frente a la variable objetivo
    utilizando un layout de dos columnas para una visualización compacta.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame que contiene las variables a analizar.
    num_cols : list
        Lista de columnas numéricas.
    target : str, opcional
        Variable objetivo (por defecto 'y').

    Returns
    -------
    None
        Muestra los gráficos por pantalla.
    """
    if len(num_cols) == 0:
        print("No hay columnas numéricas para representar.")
        return

    n_rows = (len(num_cols) + 1) // 2
    fig, axes = plt.subplots(n_rows, 2, figsize=(12, n_rows * 5))
    axes = axes.flatten()

    for i, col in enumerate(num_cols):
        sns.boxplot(
            x=target,
            y=col,
            data=df,
            ax=axes[i],
            color='#4C72B0',
            width=0.5,
            fliersize=3
        )

        axes[i].set_title(f'{col} según {target}', fontsize=12, fontweight='bold')
        axes[i].set_xlabel(target)
        axes[i].set_ylabel(col)
        axes[i].grid(axis='y', linestyle='--', alpha=0.3)
        axes[i].grid(axis='x', visible=False)

    # Eliminar subplots vacíos
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()

#Barplots de tasa de suscripción por categorías 
def plot_bar_rate(df, cat_cols, target='y'):
    """
    Muestra barplots de la tasa de suscripción para variables categóricas,
    organizados en un layout de dos columnas.

    La intensidad del color azul representa la magnitud de la tasa:
    barras más altas → azul más oscuro.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con los datos.
    cat_cols : list
        Lista de columnas categóricas a analizar.
    target : str, opcional
        Variable objetivo binaria (por defecto 'y').

    Returns
    -------
    None
        La función muestra los gráficos por pantalla.
    """
    import matplotlib.colors as mcolors
    import numpy as np
    import matplotlib.pyplot as plt

    n_cols = 2
    n_plots = len(cat_cols)
    n_rows = int(np.ceil(n_plots / n_cols))

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(14, 4 * n_rows))
    axes = axes.flatten()

    base_color = "#4C72B0"
    cmap = mcolors.LinearSegmentedColormap.from_list(
        "blue_grad", ["#dbe9f6", base_color]
    )

    for i, col in enumerate(cat_cols):
        rate = df.groupby(col, as_index=False)[target].mean()

        values = rate[target].values
        norm = (values - values.min()) / (values.max() - values.min() + 1e-9)
        colors = cmap(norm)

        axes[i].bar(rate[col], values, color=colors)
        axes[i].set_title(f'Tasa de {target} por {col}', fontweight='bold')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel(f'Proporción de {target}')
        axes[i].grid(axis='y', linestyle='--', alpha=0.3)
        axes[i].tick_params(axis='x', rotation=45)

    # Eliminar ejes sobrantes
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()

def plot_time_evolution(df, time_col, target='y', color='#4C72B0'):
   
    """
    Muestra la evolución temporal de la tasa de suscripción a lo largo del tiempo.

    Parámetros
    ----------
    df : pandas.DataFrame
        DataFrame con los datos
    time_col : str
        Columna temporal (por ejemplo 'contact_year')
    target : str, opcional
        Variable objetivo binaria (por defecto 'y')
    color : str, opcional
        Color de la línea (por defecto '#4C72B0')
    """

    rate = df.groupby(time_col)[target].mean()

    plt.figure(figsize=(8, 5))
    plt.plot(
        rate.index,
        rate.values,
        marker='o',
        color=color
    )

    plt.xticks(rate.index)  # 🔹 fuerza años enteros
    plt.title(f'Evolución temporal de {target} por {time_col}')
    plt.xlabel(time_col)
    plt.ylabel(f'Proporción de {target}')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

#Heatmap 
def plot_corr_heatmap(df):
    """
    Muestra un heatmap de correlaciones entre variables numéricas.

    Permite identificar relaciones lineales entre variables cuantitativas.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame que contiene las variables numéricas a analizar.

    Returns
    -------
    None
        Muestra el heatmap por pantalla.
    """

    corr = df.select_dtypes(include='number').corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(
        corr,
        cmap='coolwarm',
        center=0,
        linewidths=0.5,
        cbar_kws={'shrink': 0.8}
    )

    plt.title(
        'Matriz de correlaciones entre variables numéricas',
        fontsize=13,
        fontweight='bold'
    )

    plt.tight_layout()
    plt.show()