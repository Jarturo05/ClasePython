from fastapi import APIRouter, HTTPException

from datos import buscar_clase, reservas
from modelos import Reserva, ReservaCrear

router = APIRouter(prefix="/reservas", tags=["reservas"])


@router.post("", response_model=Reserva, status_code=201)
def crear_reserva(datos: ReservaCrear):
    clase = buscar_clase(datos.clase_id)
    if clase is None:
        raise HTTPException(status_code=404, detail="Esa clase no existe.")
    if clase["cupos"] == 0:
        raise HTTPException(status_code=409, detail="Esa clase ya no tiene cupos.")
    clase["cupos"] -= 1
    reserva = {
        "id": len(reservas) + 1,
        "clase": clase["nombre"],
        "hora": clase["hora"],
        **datos.model_dump(),
    }
    reservas.append(reserva)
    return reserva


@router.get("", response_model=list[Reserva])
def listar_reservas():
    return reservas