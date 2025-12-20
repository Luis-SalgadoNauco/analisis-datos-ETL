from base_pipeline import BaseETLPipeline

class TestPipeline(BaseETLPipeline):
    def extract(self):
        return []

    def transform(self, data):
        return data

    def load(self, data):
        print("Carga simulada OK")

if __name__ == "__main__":
    pipeline = TestPipeline()
    pipeline.run()