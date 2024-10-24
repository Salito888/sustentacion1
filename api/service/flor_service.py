
from api.model.flor_model import  Girasol, Tulipan, Rosa

# Datos de ejemplo
flores = [
    Girasol(nombre="Girasol", color="Amarillo", precio=10.0, altura=1.5),
    Tulipan(nombre="Tulipán", color="Rojo", precio=12.0, origen="Holanda"),
    Rosa(nombre="Rosa", color="Blanco", precio=15.0, espinas=True),
    Rosa(nombre="Rosa", color="Rojo", precio=20.0, espinas=False)
]

def listar_flores():
    return flores

def flores_por_color(color: str):
    return [flor for flor in flores if flor.color.lower() == color.lower()]

def flores_por_precio(min_precio: float):
    return [flor for flor in flores if flor.precio > min_precio]
