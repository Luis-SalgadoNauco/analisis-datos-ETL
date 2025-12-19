\# ETL – Día 1 | Integración de Datos con Python y SQLite



\## 📌 Contexto

Este proyecto corresponde al Día 1 de la semana 4 del curso de Análisis de Datos,

enfocado en el diseño conceptual y práctico de un pipeline ETL (Extract, Transform, Load).



El objetivo es integrar datos provenientes de distintos sistemas de una cadena de tiendas

minoristas para generar una fuente de datos unificada y lista para análisis analítico.



---



\## 🏪 Escenario de Negocio

Una cadena de tiendas minoristas desea integrar información desde:



\- Sistema de Punto de Venta (POS)

\- Sistema de Inventario

\- CRM de clientes

\- Sitio web (analítica digital)



Los datos se encuentran fragmentados, en distintos formatos y con diferentes frecuencias

de actualización.



---



\## 🛠️ Tecnologías Utilizadas

\- Python 3

\- Pandas

\- SQLite

\- Jupyter Notebook

\- Git



---



\## 🔄 Proceso ETL



\### Extract

\- Datos de ventas simulados (POS)

\- Información de clientes simulada (CRM)

\- Datos de analítica web simulados (no persistidos en este ejercicio)



\### Transform

\- Conversión de marcas de tiempo a fechas

\- Eliminación de registros duplicados

\- Cálculo de métricas (total de venta)

\- Enriquecimiento de ventas con segmento de cliente

\- Normalización de columnas



\### Load

\- Carga de los datos transformados en una base de datos SQLite

\- Creación de la tabla `ventas\_consolidadas`

\- Exportación de resultados finales a Excel para validación y visualización





---



\## 📊 Resultado Final

Se generó una base de datos SQLite (`ventas\_etl.db`) con una tabla consolidada de ventas,

verificada tanto desde Python como mediante consultas SQL directas.



La tabla final contiene información limpia, consistente y lista para análisis.



---



\## ✅ Conclusión

Este ejercicio demuestra la implementación completa de un pipeline ETL real,

utilizando Python como orquestador del proceso y SQLite como sistema de almacenamiento,

siguiendo buenas prácticas de integración y calidad de datos.

---

## ▶️ Cómo ejecutar el proyecto

1. Activar el entorno virtual
2. Abrir Jupyter Notebook
3. Ejecutar el archivo `ETL_Semana4_Dia1.ipynb` de arriba hacia abajo
4. La base de datos `ventas_etl.db` y el archivo `ventas_consolidadas.xlsx`
   se generan automáticamente


```

analisis-datos-ETL/

│

├── dia1\_etl\_pipeline.ipynb

├── ventas\_etl.db

├── ventas\_consolidadas.xlsx

├── README.md

└── .gitignore

```

