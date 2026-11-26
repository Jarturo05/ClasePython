from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import clases, reservas

app = FastAPI(title="API de PulsoFit")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(clases.router)
app.include_router(reservas.router)