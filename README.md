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
- NumPy
- SQLite
- Jupyter Notebook
- Git & GitHub

---

## Día 1: Integración de Datos con Python y SQLite

---

### Pipeline ETL

#### Extract
- Datos de ventas simulados (POS)
- Datos de clientes simulados (CRM)

#### Transform
- Conversión de timestamps a fechas
- Eliminación de registros duplicados
- Cálculo del total de venta
- Enriquecimiento con segmento de cliente
- Normalización de columnas

#### Load
- Carga de los datos transformados en SQLite
- Creación de la tabla `ventas_consolidadas`
- Exportación de resultados a Excel

---

### Resultados
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

## Día 3: Transformación, Validaciones y Enriquecimiento de Datos

### Objetivo
Aplicar transformaciones avanzadas, validaciones de reglas de negocio y
enriquecimiento de datos sobre un conjunto de datos estructurado,
con el fin de garantizar calidad, consistencia e información analítica útil.

Este día se enfoca en la etapa **Transform (T)** del pipeline ETL.

---

### Conjunto de datos
Se trabajó con un dataset sintético de clientes que incluye:

- Edad
- Ingresos
- Gastos mensuales
- Categoría de cliente
- Fecha de registro
- Email
- Teléfono

El dataset contiene **errores intencionales** para simular escenarios reales:
- Edades fuera de rango
- Ingresos negativos
- Gastos mayores a los ingresos

---

### Validaciones aplicadas

#### Validación de edad
- Se validó que la edad esté entre 18 y 80 años.
- Las edades inválidas fueron marcadas como `NaN`.
- Se creó una columna auxiliar `edad_valida` para control de calidad.

#### Validación de ingresos
- Se identificaron ingresos negativos.
- Los valores inválidos fueron corregidos y marcados como faltantes (`NaN`).

#### Validación gastos vs ingresos
- Se calculó el ratio gasto / ingreso.
- Cuando los gastos superaban los ingresos, se ajustaron al **80% del ingreso**.

---

### Transformaciones y enriquecimiento

- Clasificación por grupo etario (`grupo_edad`)
- Cálculo de capacidad de ahorro
- Cálculo de ratio de ahorro
- Clasificación financiera:
  - Ahorra_Mucho
  - Ahorra_Poco
  - Equilibra
  - Déficit
- Extracción de código de área desde el teléfono
- Cálculo de antigüedad del cliente (días y meses)

---

### Métricas agregadas

Se generaron métricas agrupadas por grupo de edad:

- Promedio, mediana y desviación estándar de ingresos
- Capacidad de ahorro promedio
- Ratio de ahorro promedio

Estas métricas permiten analizar el comportamiento financiero
por segmento etario.

---

### Evidencia generada

Se creó un archivo Excel consolidado con múltiples hojas:

- `datos_originales`
- `datos_transformados`
- `antes_vs_despues`
- `metricas_por_edad`
- `resumen_validacion`

**Archivo de evidencia:**
- `evidencia_ETL_dia3_transformaciones.xlsx`

Este archivo documenta de forma clara y auditable
todo el proceso de transformación y validación.

---

## Día 4: Carga a Bases de Datos SQL con Validaciones

### Objetivo
Implementar la etapa **Load (L)** del pipeline ETL asegurando:

- Integridad referencial
- Consistencia de datos
- Carga segura y validada en bases de datos SQL

---

### Esquema de base de datos

Se creó una base de datos SQLite con las siguientes tablas:

- `clientes`
- `productos`
- `ventas`

Cada tabla incluye:
- Claves primarias
- Restricciones (`NOT NULL`, `UNIQUE`)
- Claves foráneas en la tabla `ventas`

---

### Estrategia de carga

- Uso de `to_sql()` para carga básica
- Validación previa de claves foráneas
- Filtrado de registros inválidos
- Carga incremental controlada

Solo se cargaron registros que cumplían las reglas de integridad referencial.

---

### Validaciones durante la carga

- Clientes inexistentes en ventas → descartados
- Productos inexistentes en ventas → descartados
- Confirmación de registros cargados por tabla

Resultado:
- Dataset original de ventas: 20 registros
- Ventas válidas cargadas: **11 registros**

---

### Verificación post-carga

- Conteo de registros por tabla
- Consulta SQL con joins entre clientes y ventas
- Validación de coherencia analítica

Ejemplo:
- Ventas por cliente
- Total de ventas por cliente
- Clientes sin ventas correctamente identificados

---

### Evidencia generada

Se generó un archivo Excel con información completa del proceso:

- `Clientes cargados`
- `Productos cargados`
- `Ventas finales válidas`
- `Resultados de consultas analíticas`


**Archivo de evidencia:**
- `evidencia_ETL_dia4_carga_sql.xlsx`

---

Este ejercicio simula un escenario real de carga productiva,
donde la calidad de los datos es prioritaria frente a la cantidad.

---
### Notebooks asociados

- `ETL_Semana4_Dia1.ipynb`
- `ETL_Semana4_Dia2_Extraccion.ipynb`
- `ETL_Semana4_Dia3_Transformaciones.ipynb`
- `ETL_Semana4_Dia4_Carga.ipynb`

---

## Cómo ejecutar el proyecto

1. Activar el entorno virtual  
2. Abrir Jupyter Notebook  
3. Ejecutar los notebooks según la etapa:
   - `ETL_Semana4_Dia1.ipynb`
   - `ETL_Semana4_Dia2_Extraccion.ipynb`
   - `ETL_Semana4_Dia3_Transformaciones.ipynb`
   - `ETL_Semana4_Dia4_Carga.ipynb`

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
├── ETL_Semana4_Dia3_Transformaciones.ipynb
├── evidencia_ETL_dia3_transformaciones.xlsx
├── ETL_Semana4_Dia4_Carga.ipynb
├── ventas_etl_dia4.db
├── evidencia_ETL_dia4_carga_sql.xlsx
├── README.md
└── .gitignore
```
