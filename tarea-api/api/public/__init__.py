from fastapi import APIRouter, Depends

from api.auth import authent
from api.public.usuario import views as usuarios
from api.public.tarea import views as tareas

api = APIRouter()

api.include_router(tareas.router, prefix="/tareas",tags=['Tareas'], dependencies=[Depends(authent)])
api.include_router(usuarios.router, prefix="/usuarios",tags=['Usuarios'], dependencies=[Depends(authent)])