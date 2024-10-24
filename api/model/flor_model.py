
from pydantic import BaseModel

class Flor(BaseModel):
    nombre: str
    color: str
    precio: float

class Girasol(Flor):
    altura: float

class Tulipan(Flor):
    origen: str

class Rosa(Flor):
    espinas: bool
