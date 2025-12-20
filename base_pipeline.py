import logging
import pandas as pd
import sqlite3
import time

# =========================
# CONFIGURACIÓN DE LOGGING
# =========================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('etl_pipeline.log'),
        logging.StreamHandler()
    ]
)

class BaseETLPipeline:
    """
    Clase base para pipelines ETL robustos.
    Solo se deben personalizar los métodos:
    - extract()
    - transform()
    - load()
    """

    def __init__(self, db_path='etl_database.db'):
        self.db_path = db_path
        self.logger = logging.getLogger(self.__class__.__name__)
        self.metrics = {
            'processed': 0,
            'errors': 0,
            'start_time': None
        }

    # =========================
    # PIPELINE GENERAL
    # =========================
    def run(self):
        self.metrics['start_time'] = pd.Timestamp.now()
        self.logger.info("=== INICIANDO PIPELINE ETL ===")

        try:
            data = self.extract()
            data = self.transform(data)
            self.load(data)
            self.report_success()

        except Exception as e:
            self.metrics['errors'] += 1
            self.report_failure(e)
            raise

    # =========================
    # MÉTODOS A SOBRESCRIBIR
    # =========================
    def extract(self):
        raise NotImplementedError("Debes implementar extract()")

    def transform(self, data):
        raise NotImplementedError("Debes implementar transform()")

    def load(self, data):
        raise NotImplementedError("Debes implementar load()")

    # =========================
    # REPORTES
    # =========================
    def report_success(self):
        duration = pd.Timestamp.now() - self.metrics['start_time']
        self.logger.info("=== PIPELINE COMPLETADO ===")
        self.logger.info(f"Duración: {duration}")
        self.logger.info(f"Registros procesados: {self.metrics['processed']}")

    def report_failure(self, error):
        duration = pd.Timestamp.now() - self.metrics['start_time']
        self.logger.error("=== PIPELINE FALLÓ ===")
        self.logger.error(f"Duración hasta fallo: {duration}")
        self.logger.error(f"Error: {error}")