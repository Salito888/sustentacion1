
from fastapi import APIRouter
from api.service.flor_service import listar_flores, flores_por_color, flores_por_precio

router = APIRouter()

@router.get("/flores", summary="Listar todas las flores")
def obtener_flores():
    return listar_flores()

@router.get("/flores/color", summary="Listar flores por color")
def obtener_flores_por_color(color: str):
    return flores_por_color(color)

@router.get("/flores/precio", summary="Listar flores con precio mayor al dado")
def obtener_flores_por_precio(precio: float):
    return flores_por_precio(precio)
