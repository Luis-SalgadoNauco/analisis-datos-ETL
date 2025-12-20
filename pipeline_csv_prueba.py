import pandas as pd
from base_pipeline import BaseETLPipeline


class CSVPruebaPipeline(BaseETLPipeline):
    def __init__(self, ruta_csv):
        super().__init__()
        self.ruta_csv = ruta_csv

    def extract(self):
        self.logger.info("Extrayendo datos desde CSV")
        df = pd.read_csv(self.ruta_csv)
        return df

    def transform(self, data):
        self.logger.info("Transformación básica")
        data.columns = [c.lower() for c in data.columns]
        return data

    def load(self, data):
        self.logger.info("Carga simulada")
        print(data.head())
        self.metrics["processed"] = len(data)


if __name__ == "__main__":
    pipeline = CSVPruebaPipeline("ventas.csv")
    pipeline.run()