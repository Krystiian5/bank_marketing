# Bank Marketing Campaigns – Exploratory Data Analysis with Python

## 📌 Introducción

Este proyecto consiste en un **Análisis Exploratorio de Datos (EDA)** realizado con Python sobre varios conjuntos de datos relacionados con campañas de marketing directo de una institución bancaria portuguesa.

Las campañas se llevaron a cabo principalmente mediante llamadas telefónicas, siendo habitual contactar varias veces con un mismo cliente para determinar si finalmente contrataba un depósito a plazo.  
El análisis busca comprender el comportamiento de los clientes, evaluar la efectividad de las campañas y detectar posibles problemas de calidad en los datos.

El proyecto se desarrolla como parte del módulo **Python for Data**, aplicando técnicas de limpieza, exploración y análisis de datos.

---

## ✅ Requisitos del proyecto

El desarrollo del proyecto contempla los siguientes puntos:

- Transformación y limpieza de los datos
- Análisis descriptivo de los datos
- Visualización de la información
- Elaboración de un informe explicativo del análisis realizado

---
## 🛠️ Herramientas utilizadas
Además de las librerías base de Python, el proyecto hace uso de herramientas y recursos orientados a mantener un flujo de trabajo limpio y reproducible:

- **Python**  
- **Pandas** - Manipulación y análisis de datos
- **NumPy** - Operaciones numéricas
- **Matplotlib y Seaborn** – visualización de datos
- **Visual Studio Code** - Desarrollo del proyecto
- **Jupyter Notebooks** - Análisis exploratorio y documentación del proceso
- **GitHub** - Control de versiones y gestión del repositorio
---

## 📂 Estructura del repositorio

```
bank_marketing/
├── README.md
│
├── data/
│   ├── raw/
│   │   ├── bank-additional.csv
│   │   └── customer-details.xlsx
│   │
│   └── processed/
│   │   ├── 01.data_limpios_bank.csv
│   │   └── 02.data_limpios_no_nulos_bank.csv
│   │   └── 01.data_limpios_customer.csv
│
├── notebooks/
│   ├── 01.eda_preliminar_bank.ipynb
│   └── 02.limpieza_bank.ipynb
│   └── 03.gestion_nulos_bank.ipynb
│   └── 04.eda_descriptivo_bank.ipynb
│   └── 01.eda_preliminar_customer.ipynb
│   └── 02.limpieza_customer.ipynb
│   └── 03.eda_descriptivo_customer.ipynb
│   └── 05.merge_and_insights.ipynb
│
└── src/
    └── soporte_eda.py
    └── soporte_limpieza.py
    └── soporte_visualizacion.py
```

---

## 📁 Código de soporte y reutilización

Con el objetivo de evitar duplicación de código , se desarrollaron varios archivos de soporte ubicados en la carpeta src/:

- `soporte_eda.py`
Contiene funciones reutilizables para:

    - Exploración rápida de datasets
    - Análisis descriptivo inicial
    - Detección de nulos y duplicados

- `soporte_limpieza.py`
Incluye funciones orientadas a:

    - Limpieza de datos
    - Transformación de variables
    - Tratamiento de valores nulos
    - Normalización y estandarización de columnas

- `soporte_visualizacion.py`
Agrupa funciones personalizadas para:

    - Boxplots de variables numéricas frente a la variable objetivo

    - Barplots de tasa de suscripción por variables categóricas

    - Visualizaciones consistentes y reutilizables a lo largo del proyecto

---

## 📊 Conjuntos de datos

El proyecto trabaja con dos conjuntos de datos principales:

### 1️⃣ `bank-additional.csv`
Incluye información sobre campañas de marketing bancario, como:
- Variables demográficas y financieras de los clientes  
- Información sobre préstamos  
- Variables macroeconómicas  
- Resultado de la campaña (`y`), indicando si el cliente contrató o no el producto 

### 2️⃣ `customer-details.xlsx`
Archivo Excel que aporta información adicional sobre los clientes del banco, como:
- Ingresos
- Composición del hogar
- Comportamiento digital
- Fecha de alta como cliente

El archivo contiene tres hojas correspondientes a clientes incorporados al banco en diferentes años.

---

## 🔍 Carga y exploración inicial de los datos

Tras la carga de los datos, se creó una copia del DataFrame original para preservar los datos en bruto.  
Posteriormente, se realizó un **EDA preliminar** mediante una función personalizada, con el objetivo de obtener una visión general del conjunto de datos antes de aplicar transformaciones.

Este análisis incluyó:

- Visualización aleatoria de registros  
- Dimensiones del dataset  
- Tipos de datos por columna  
- Porcentaje de valores nulos  
- Detección de duplicados  
- Distribución de variables categóricas  
- Estadísticos descriptivos de variables numéricas  

Los resultados sirvieron como base para definir las siguientes fases de limpieza y preparación de los datos.

---

## 🧹 Limpieza y preparación de los datos

Tras la exploración inicial, se procedió a una fase de **limpieza y preparación** de los datos de ambos datasets, cuyo objetivo fue mejorar la calidad de la información y dejar los datasets listos para el análisis descriptivo.

Las principales acciones realizadas fueron:

- **Estandarización** de nombres de columnas

- **Conversión** de tipos de datos (fechas, variables numéricas y categóricas)

- **Tratamiento de valores nulos**:

    - Eliminación de registros con información crítica incompleta

    - Análisis específico del impacto de los nulos en variables clave

- **Creación de nuevas variables derivadas** (por ejemplo, antigüedad del cliente)

Como resultado de este proceso, se generaron **datasets limpios** que se almacenaron en la carpeta data/processed, permitiendo distinguir una separación clara entre datos crudos y tratados.

---

## 📈 Análisis exploratorio descriptivo (EDA)

Con los datos ya preparados, se realizó un **EDA descriptivo en profundidad**, centrado en identificar patrones, diferencias entre grupos y posibles relaciones con la variable objetivo (y).

El análisis se compuso de:

**🔢 Variables numéricas**

- Distribución de ingresos, antigüedad del cliente y variables macroeconómicas

- Comparación de distribuciones entre clientes que suscriben y no suscriben el producto mediante boxplots

- Identificación de dispersión, asimetrías y valores atípicos

**🧩 Variables categóricas**

-  Análisis de la tasa de suscripción por categoría

- Comparación de resultados entre distintos perfiles de cliente

- Evaluación del impacto de variables operativas de la campaña

---

## 📊 Visualizaciones clave

Las visualizaciones han permitido interpretar los datos de forma clara y efectiva. Entre los gráficos utilizados destacan:

- **Boxplots** de variables numéricas frente a la variable objetivo

- **Barplots de tasa de suscripción** por variables categóricas

- **Heatmaps de correlación** entre variables numéricas y macroeconómicas

Estas visualizaciones permitieron detectar rápidamente qué variables muestran mayor capacidad explicativa y cuáles presentan un impacto sobre la suscripción.

---

## 🔗 Integración de datasets y análisis conjunto

Una vez tratados y analizados los datos de ambos datasets, se realizó la integración de los datasets bancarios con la información adicional de clientes, mediante un proceso de merge.

Este paso permitió:

- Enriquecer el análisis con variables de ingresos y comportamiento digital

- Evaluar si estas variables aportaban mayor capacidad explicativa

- Comparar perfiles de clientes más allá de la información bancaria

---

## 🧠 Principales conclusiones

Del análisis exploratorio realizado se aprecian las siguientes conclusiones:

- La suscripción al producto no muestra una relación fuerte con variables puramente demográficas o económicas del cliente, como el nivel educativo, el estado civil o los ingresos. Estas variables presentan distribuciones similares entre clientes que suscriben y los que no.

- Las variables operativas de la campaña son las que muestran mayor capacidad explicativa sobre la variable objetivo, destacando:

    - El método de contacto, con una mayor efectividad del contacto telefónico móvil frente a otros canales.

    - El mes de contacto, donde se observan ligeras variaciones, aunque sin patrones extremadamente marcados, destacando octubre con una tasa ligeramente superior.

    - El resultado de campañas anteriores, que se posiciona como la variable más influyente.

- En particular, los clientes que tuvieron un resultado exitoso (success) en campañas previas presentan una tasa de suscripción muy superior al resto de categorías.

En términos generales, los resultados indican que optimizar la estrategia de contacto, priorizar clientes con historial positivo y mejorar la planificación de campañas puede ser más efectivo que basar la toma de decisiones exclusivamente en el perfil sociodemográfico del cliente.

---

## 💡 Buenas prácticas aplicadas

Durante el desarrollo inicial del proyecto se han aplicado las siguientes buenas prácticas:

- **Preservación de los datos originales**, trabajando siempre sobre copias del DataFrame  
- **Separación de responsabilidades**, diferenciando análisis (notebooks) y lógica reutilizable (`src`)  
- **Modularidad**, encapsulando tareas repetitivas del EDA en funciones personalizadas  
- **Análisis progresivo**, siguiendo un flujo lógico: carga → exploración → limpieza → análisis  
- **Claridad y legibilidad**, utilizando nombres descriptivos y código fácil de mantener  
- **Organización del proyecto**, separando datos crudos, procesados, notebooks y código fuente  

---