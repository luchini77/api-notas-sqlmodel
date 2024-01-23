from fastapi import APIRouter

from api.public.nota import views as notas
from api.public.usuario import views as usuarios

api = APIRouter()

api.include_router(notas.router, prefix="/notas", tags=["Notas"])
api.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])