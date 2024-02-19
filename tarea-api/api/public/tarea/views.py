from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List

from api.database import get_db
from api.public.tarea.models import TareaCrear, TareaLeer, TareaActualizar, TareaLeerJoin
from api.public.tarea.crud import (
    leer_tareas,
    crear_tarea,
    leer_tarea,
    borrar_tarea,
    actualizar_tarea
)


router = APIRouter()

@router.get('', response_model=list[TareaLeerJoin])
def get_tasks(db:Session=Depends(get_db)):
    return leer_tareas(db=db)

@router.post('', response_model=TareaLeer)
def create_task(tarea:TareaCrear, db:Session=Depends(get_db)):
    return crear_tarea(tarea=tarea, db=db)

@router.get('/{id}', response_model=TareaLeerJoin)
def get_by_id(id:int, db:Session=Depends(get_db)):
    return leer_tarea(id=id, db=db)

@router.patch('/{id}', response_model=TareaLeer)
def update_task(id:int, tarea:TareaActualizar, db:Session=Depends(get_db)):
    return actualizar_tarea(id=id, tarea=tarea, db=db)

@router.delete('/{id}')
def delete_task(id:int, db:Session=Depends(get_db)):
    return borrar_tarea(id=id, db=db)