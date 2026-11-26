from fastapi import APIRouter, HTTPException

from datos import buscar_clase, clases
from modelos import Clase

router = APIRouter(prefix="/clases", tags=["clases"])


@router.get("", response_model=list[Clase])
def listar_clases():
    return clases


@router.get("/{clase_id}", response_model=Clase)
def obtener_clase(clase_id: int):
    clase = buscar_clase(clase_id)
    if clase is None:
        raise HTTPException(status_code=404, detail="Esa clase no existe.")
    return clase