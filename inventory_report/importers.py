from typing import Dict, Type, List
from abc import ABC, abstractmethod
import json
from inventory_report.product import Product


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self, path: str) -> List[Product]:
        with open(path, "r") as file:
            product_data = json.load(file)
            return [Product(**product) for product in product_data]


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
