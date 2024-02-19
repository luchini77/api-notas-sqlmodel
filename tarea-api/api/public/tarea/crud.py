from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select
from datetime import datetime

from api.database import get_db
from api.public.tarea.models import Tarea, TareaCrear, TareaActualizar
from api.public.usuario.models import Usuario


def fecha_actual():
    fecha = datetime.today()
    date = fecha.strftime('%d/%m/%Y')
    return date

def leer_tareas(db:Session=Depends(get_db)):
    tareas = db.exec(select(Tarea)).all()
    return tareas
        
def crear_tarea(tarea:TareaCrear, db:Session=Depends(get_db)):
    usuarios = db.exec(select(Usuario)).all()

    if len(usuarios) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No hay usuarios, primero ingrese un usuario!")
    else:
        nueva_tarea = Tarea.model_validate(tarea)
        nueva_tarea.fecha_creacion = fecha_actual()

        db.add(nueva_tarea)
        db.commit()
        db.refresh(nueva_tarea)

        return nueva_tarea
    
def leer_tarea(id:int, db:Session=Depends(get_db)):
    tarea = db.get(Tarea, id)

    if not tarea:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No existe esa tarea con el id {id}')
    return tarea

def actualizar_tarea(id:int, tarea:TareaActualizar, db:Session=Depends(get_db)):
    tarea_update = db.get(Tarea, id)

    if not tarea_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No existe esa tarea con el id {id}')
    
    tarea_data = tarea.model_dump(exclude_unset=True)

    for key, value in tarea_data.items():
        setattr(tarea_update, key, value)

    db.add(tarea_update)
    db.commit()
    db.refresh(tarea_update)
    return tarea_update

def borrar_tarea(id:int, db:Session=Depends(get_db)):
    tarea = db.get(Tarea, id)

    if not tarea:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No existe esa tarea con el id {id}')
    
    db.delete(tarea)
    db.commit()
    return {'ok':True}