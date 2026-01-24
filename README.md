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

- Python  
- Pandas  
- Visual Studio Code  
- Jupyter Notebooks  
- GitHub  
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
│
├── notebooks/
│   ├── 01_eda_preliminar_bank.ipynb
│   └── 02_limpieza_bank.ipynb
│   └── 03.gestion_nulos_bank.ipynb
│   └── 04.eda_descriptivo_bank.ipynb
│
└── src/
    └── soporte_eda.py
    └── soporte_limpieza.py
    └── soporte_visualizacion.py
```

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

## 💡 Buenas prácticas aplicadas

Durante el desarrollo inicial del proyecto se han aplicado las siguientes buenas prácticas:

- **Preservación de los datos originales**, trabajando siempre sobre copias del DataFrame  
- **Separación de responsabilidades**, diferenciando análisis (notebooks) y lógica reutilizable (`src`)  
- **Modularidad**, encapsulando tareas repetitivas del EDA en funciones personalizadas  
- **Análisis progresivo**, siguiendo un flujo lógico: carga → exploración → limpieza → análisis  
- **Claridad y legibilidad**, utilizando nombres descriptivos y código fácil de mantener  
- **Organización del proyecto**, separando datos crudos, procesados, notebooks y código fuente  

---