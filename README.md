# ETL – Curso de Análisis de Datos

---

## Descripción General

Este repositorio corresponde a un proyecto práctico del curso de **Análisis de Datos**  
y documenta la construcción progresiva de un **pipeline ETL (Extract, Transform, Load)**.

El proyecto está organizado por etapas (Día 1, Día 2, etc.), donde se abordan
distintos aspectos del proceso ETL, desde la integración inicial de datos
hasta la extracción desde múltiples fuentes heterogéneas.

El objetivo general es integrar datos provenientes de diversos sistemas empresariales
para generar una fuente de datos unificada, limpia y lista para su análisis.

---

## Escenario de Negocio
Una cadena de tiendas minoristas necesita consolidar información desde:

- Sistema de Punto de Venta (POS)
- Sistema de Inventario
- CRM de clientes
- Sitio web (analítica digital)

Los datos se encuentran fragmentados, en formatos heterogéneos
y con distintas frecuencias de actualización.

---

## Tecnologías Utilizadas
- Python 3
- Pandas
- SQLite
- Jupyter Notebook
- Git & GitHub

---

## Día 1: Integración de Datos con Python y SQLite

---

## Pipeline ETL

### Extract
- Datos de ventas simulados (POS)
- Datos de clientes simulados (CRM)

### Transform
- Conversión de timestamps a fechas
- Eliminación de registros duplicados
- Cálculo del total de venta
- Enriquecimiento con segmento de cliente
- Normalización de columnas

### Load
- Carga de los datos transformados en SQLite
- Creación de la tabla `ventas_consolidadas`
- Exportación de resultados a Excel

---

## Resultados
Se generó una base de datos SQLite (`ventas_etl.db`) con información consolidada
y validada mediante consultas SQL.

También se generó un archivo Excel como evidencia del proceso.

---

## Día 2: Extracción desde múltiples fuentes

### Objetivo
Extraer datos desde fuentes heterogéneas y convertirlos en estructuras consistentes
(DataFrames) listas para su posterior transformación.

### Fuentes de datos utilizadas
- Archivo CSV
- Archivo Excel con múltiples hojas
- Archivo JSON
- Base de datos SQLite
- API REST simulada

### Proceso realizado
- Lectura de archivos CSV con Pandas
- Lectura de hojas específicas desde Excel
- Conversión de datos JSON a formato tabular
- Conexión y consulta a base de datos SQLite
- Simulación de consumo de API REST
- Validación de consistencia mediante dimensiones (filas y columnas)

### Evidencia generada
Se creó un archivo Excel con una hoja por cada fuente de datos extraída,
permitiendo validar visualmente el proceso de extracción.

**Archivo de evidencia:**
- `evidencia_extraccion_dia2.xlsx`

---

## Cómo ejecutar el proyecto

1. Activar el entorno virtual  
2. Abrir Jupyter Notebook  
3. Ejecutar los notebooks según la etapa:
   - `ETL_Semana4_Dia1.ipynb`
   - `ETL_Semana4_Dia2_Extraccion.ipynb`

---

## Estructura del Proyecto

```text
analisis-datos-ETL/
│
├── ETL_Semana4_Dia1.ipynb
├── ventas_etl.db
├── ventas_consolidadas.xlsx
├── ETL_Semana4_Dia2_Extraccion.ipynb
├── crear_fuentes.py
├── ventas.csv
├── datos.xlsx
├── productos.json
├── ventas.db
├── evidencia_extraccion_dia2.xlsx
├── README.md
└── .gitignore
```
