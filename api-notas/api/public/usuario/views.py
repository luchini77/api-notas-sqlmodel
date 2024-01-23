from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from api.database import get_db
from api.public.usuario.models import UsuarioCrear, UsuarioLeer, UsuarioUpdate
from api.public.usuario.crud import (
    crear_usuario,
    borrar_usuario,
    leer_usuario,
    leer_usuarios,
    actualizar_usuario
)

router = APIRouter()


@router.post("", response_model=UsuarioLeer)
def create_user(usuario:UsuarioCrear, db: Session=Depends(get_db)):
    return crear_usuario(usuario=usuario, db=db)

@router.get("", response_model=list[UsuarioLeer])
def get_users(db:Session=Depends(get_db)):
    return leer_usuarios(db=db)

@router.get("/{id}",response_model=UsuarioLeer)
def get_by_id(id:int, db:Session=Depends(get_db)):
    return leer_usuario(id=id, db=db)

@router.patch("/{id}",response_model=UsuarioLeer)
def update_user(id:int, usuario:UsuarioUpdate, db:Session=Depends(get_db)):
    return actualizar_usuario(id=id, usuario=usuario, db=db)

@router.delete("/{id}")
def delete_user(id:int,db:Session=Depends(get_db)):
    return borrar_usuario(id=id, db=db)

