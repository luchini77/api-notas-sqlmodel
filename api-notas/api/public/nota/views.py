from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from .models import NotaCrear,NotaLeer,NotaUpdate
from api.database import get_db
from .crud import leer_notas,crear_nota,obtener_nota,eliminar_nota,actualizar_nota


router = APIRouter()
notas = []

@router.get('',response_model=List[NotaLeer])
def leer(db:Session=Depends(get_db)):
    return leer_notas(db=db)
    


@router.post('',response_model=NotaLeer)
def agregar(nota:NotaCrear,db:Session=Depends(get_db)):
    return crear_nota(nota=nota,db=db)


@router.get('/{id}', response_model=NotaLeer)
def una_nota(id:int,db:Session=Depends(get_db)):
    return obtener_nota(id=id,db=db)

@router.delete('/{id}')
def delete_nota(id:int,db:Session=Depends(get_db)):
    return eliminar_nota(id=id,db=db)


@router.patch('/{id}',response_model=NotaLeer)
def update_nota(id:int, nota:NotaUpdate,db:Session=Depends(get_db)):
    return actualizar_nota(id=id,nota=nota,db=db)