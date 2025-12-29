import dataclasses

main_link = "http://localhost:4200/"

@dataclasses.dataclass
class Product:
    name: str
    price: float
    co2: chr
    category: str
    brand: str
    id: str