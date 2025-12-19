# ETL – Día 1  
## Integración de Datos con Python y SQLite

---

## Descripción General
Este proyecto corresponde al **Día 1 de la Semana 4** del curso de **Análisis de Datos**  
y se centra en el diseño e implementación de un **pipeline ETL (Extract, Transform, Load)**.

El objetivo es integrar datos provenientes de múltiples sistemas empresariales
para generar una fuente de datos unificada, limpia y lista para análisis.

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

## Cómo ejecutar el proyecto

1. Activar el entorno virtual  
2. Abrir Jupyter Notebook  
3. Ejecutar `ETL_Semana4_Dia1.ipynb`  
4. Archivos generados automáticamente:
   - `ventas_etl.db`
   - `ventas_consolidadas.xlsx`

---

## Estructura del Proyecto

```text
analisis-datos-ETL/
│
├── ETL_Semana4_Dia1.ipynb
├── ventas_etl.db
├── ventas_consolidadas.xlsx
├── README.md
└── .gitignore
```
