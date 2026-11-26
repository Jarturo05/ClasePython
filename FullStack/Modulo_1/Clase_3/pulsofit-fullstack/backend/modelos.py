from pydantic import BaseModel, EmailStr, Field


class Clase(BaseModel):
    id: int
    nombre: str
    entrenador: str
    hora: str
    cupos: int


class ReservaCrear(BaseModel):
    clase_id: int
    nombre: str = Field(min_length=3)
    correo: EmailStr


class Reserva(ReservaCrear):
    id: int
    clase: str
    hora: str