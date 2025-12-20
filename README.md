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
- SQLite (base de datos relacional)
- Jupyter Notebook
- Git & GitHub
- Logging (módulo logging de Python)

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

## Día 5: Pipeline ETL Robusto y Reutilizable (Enfoque Productivo)

### Objetivo
Diseñar un pipeline ETL con una arquitectura más cercana a entornos reales,
incorporando buenas prácticas de ingeniería de datos como:

- Programación orientada a objetos
- Logging estructurado
- Manejo robusto de errores
- Métricas de ejecución
- Reutilización de código

Este día marca la transición desde notebooks exploratorios
hacia **pipelines ejecutables en producción**.

---

### Pipeline base reutilizable

Se implementó una **clase base de pipeline ETL** que define la estructura
estándar del proceso Extract, Transform y Load.

**Archivo:**
- `base_pipeline.py`

#### Características
- Método central `run()` que orquesta todo el flujo ETL
- Métodos abstractos a sobrescribir:
  - `extract()`
  - `transform(data)`
  - `load(data)`
- Registro de métricas:
  - Tiempo de ejecución
  - Registros procesados
  - Errores
- Logging uniforme y centralizado
- Manejo controlado de excepciones

Este archivo funciona como **plantilla base** para futuros pipelines,
evitando reescribir lógica común.

---

### Pipeline de prueba

Para validar el correcto funcionamiento de la clase base,
se creó un pipeline mínimo de prueba.

**Archivo:**
- `test_base_pipeline.py`

**Objetivo:**
- Verificar que la estructura base se ejecuta correctamente
- Confirmar el flujo completo del pipeline
- Validar el logging sin depender de datos reales

---

### Pipeline ETL robusto completo

Se desarrolló un pipeline ETL funcional que integra todas las buenas prácticas
aprendidas durante el curso.

**Archivo:**
- `ETL_Dia5_Pipeline_Robusto.py`

#### Características principales
- Extracción con estrategia de reintentos
- Transformaciones con validaciones explícitas
- Carga en SQLite usando transacciones
- Rollback automático ante fallos
- Logging detallado de cada etapa
- Reporte final de métricas

Este pipeline representa un escenario cercano a producción
y sirve como referencia para futuros desarrollos ETL.

---

### Logging y evidencias

Durante la ejecución de los pipelines se genera un archivo de log
que registra todas las fases del proceso ETL.

**Archivo generado:**
- `etl_pipeline.log`

> Nota: el archivo de log puede no estar versionado en Git  
> según la configuración del archivo `.gitignore`.

El log incluye:
- Inicio y término del pipeline
- Intentos de extracción
- Resultados de transformaciones
- Estado de la carga
- Duración total del proceso
- Detalle de errores (si ocurren)

---

### Enfoque final del proyecto

Con el Día 5, el proyecto evoluciona desde un enfoque académico
basado en notebooks hacia una **arquitectura reutilizable,
escalable y alineada con prácticas profesionales** de ingeniería de datos.

---

## Cómo ejecutar el proyecto

1. Activar el entorno virtual (analisis_datos_env)  
2. Abrir Jupyter Notebook  
3. Ejecutar los notebooks según la etapa:
   - `ETL_Semana4_Dia1.ipynb`
   - `ETL_Semana4_Dia2_Extraccion.ipynb`
   - `ETL_Semana4_Dia3_Transformaciones.ipynb`
   - `ETL_Semana4_Dia4_Carga.ipynb`

### Ejecución de pipelines productivos (Día 5)

Los pipelines del Día 5 están diseñados para ejecutarse
directamente desde la consola, sin depender de Jupyter Notebook.
Los comandos deben ejecutarse desde la carpeta raíz del proyecto.

Ejecutar el pipeline ETL robusto:

```bash
python ETL_Dia5_Pipeline_Robusto.py
```

---

Ejecutar la prueba de la plantilla base:

```bash
python test_base_pipeline.py
```

---

## Estado del proyecto

Proyecto finalizado como parte del curso de Análisis de Datos.
La arquitectura del Día 5 permite extender el pipeline
a nuevos orígenes de datos y escenarios productivos.

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
├── ETL_Dia5_Pipeline_Robusto.py
├── base_pipeline.py
├── test_base_pipeline.py
├── README.md
└── .gitignore
```
