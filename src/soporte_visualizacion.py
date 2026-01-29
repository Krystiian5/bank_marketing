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
def plot_box_vs_target(
    df,
    num_cols,
    target='y',
    title_map=None,
    xlabel='Suscripción',
    ylabel_map=None
):
    """
    Genera boxplots de variables numéricas frente a la variable objetivo.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con los datos.
    num_cols : list
        Columnas numéricas a analizar.
    target : str
        Variable objetivo.
    title_map : dict, opcional
        Títulos descriptivos por variable.
    xlabel : str, opcional
        Etiqueta del eje X.
    ylabel_map : dict, opcional
        Etiquetas descriptivas del eje Y por variable.
    """
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

        title = title_map[col] if title_map and col in title_map else f'{col} según {target}'
        ylabel = ylabel_map[col] if ylabel_map and col in ylabel_map else col

        axes[i].set_title(title, fontsize=12, fontweight='bold')
        axes[i].set_xlabel(xlabel)
        axes[i].set_ylabel(ylabel)
        axes[i].grid(axis='y', linestyle='--', alpha=0.3)
        axes[i].grid(axis='x', visible=False)

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()

#Barplots de tasa de suscripción por categorías 
def plot_bar_rate(
    df,
    cat_cols,
    target='y',
    title_map=None,
    xlabel=None,
    ylabel='Tasa de suscripción'
):
    """
    Muestra barplots de la tasa de suscripción para variables categóricas,
    organizados en un layout de dos columnas.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con los datos.
    cat_cols : list
        Lista de columnas categóricas a analizar.
    target : str, opcional
        Variable objetivo binaria (por defecto 'y').
    title_map : dict, opcional
        Títulos descriptivos por variable.
    xlabel : str, opcional
        Etiqueta del eje X (si no se indica, usa el nombre de la variable).
    ylabel : str, opcional
        Etiqueta del eje Y (por defecto 'Tasa de suscripción').

    Returns
    -------
    None
        Muestra los gráficos por pantalla.
    """

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

        title = title_map[col] if title_map and col in title_map else f'Tasa de suscripción según {col}'
        axes[i].set_title(title, fontweight='bold')

        axes[i].set_xlabel(xlabel if xlabel else col)
        axes[i].set_ylabel(ylabel)

        axes[i].grid(axis='y', linestyle='--', alpha=0.3)
        axes[i].tick_params(axis='x', rotation=45)

    # Eliminar ejes sobrantes
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()

#Evolucion temporal
def plot_time_evolution(
    df,
    time_col,
    target='y',
    color="#4C72B0",
    title=None,
    xlabel=None,
    ylabel=None
):
    """
    Muestra la evolución temporal de la tasa de suscripción con un gráfico de línea.
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con los datos.
    time_col : str
        Columna temporal (por ejemplo 'contact_year').
    target : str, opcional
        Variable objetivo binaria (por defecto 'y').
    color : str, opcional
        Color de la línea (por defecto '#4C72B0').
    title : str, opcional
        Título del gráfico.
    xlabel : str, opcional
        Etiqueta del eje X.
    ylabel : str, opcional
        Etiqueta del eje Y.

    Returns
    -------
    None
        Muestra el gráfico por pantalla.
    """

    # Calcular la tasa por periodo
    rate = df.groupby(time_col)[target].mean()

    plt.figure(figsize=(10, 5))
    plt.plot(
        rate.index,
        rate.values,
        marker='o',
        color=color,
        linewidth=2,
        markersize=6
    )

    # Títulos y etiquetas
    plt.title(title if title else f'Evolución de {target} por {time_col}', fontsize=13, fontweight='bold')
    plt.xlabel(xlabel if xlabel else time_col, fontsize=11)
    plt.ylabel(ylabel if ylabel else f'Proporción de {target}', fontsize=11)

    # Grid horizontal suave
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    
    # Forzar enteros en eje x si es tipo int
    if pd.api.types.is_integer_dtype(rate.index):
        plt.xticks(rate.index.astype(int))
    
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

def scatter_eda(
    df,
    x,
    y,
    title,
    xlabel,
    ylabel,
    alpha=0.5
):
    """
    Scatter plot genérico para EDA exploratorio entre dos variables numéricas.
     Parámetros
    ----------
    df : DataFrame
        Dataset de entrada.
    x : str
        Variable numérica para el eje X.
    y : str
        Variable numérica para el eje Y.
    title : str
        Título del gráfico.
    xlabel : str
        Etiqueta del eje X.
    ylabel : str
        Etiqueta del eje Y.
    alpha : float, opcional
        Nivel de transparencia de los puntos (por defecto 0.5).
    """

    plt.figure(figsize=(7, 4))
    sns.scatterplot(
        data=df,
        x=x,
        y=y,
        alpha=alpha,
        color='#4C72B0'
    )

    plt.title(title, fontweight='bold')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()
