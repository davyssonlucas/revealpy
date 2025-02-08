# core/exporter.py
import os

class Exporter:
    @staticmethod
    def export(filename: str, content: str):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
