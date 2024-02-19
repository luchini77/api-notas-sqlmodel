from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select, text

from api.database import get_db
from api.public.usuario.models import Usuario, UsuarioCrear, UsuarioActualizar


def leer_usuarios(db:Session=Depends(get_db)):
    usuarios = db.exec(select(Usuario)).all()
    return usuarios

def crear_usuario(usuario:UsuarioCrear, db:Session=Depends(get_db)):
    new_usuario = Usuario.model_validate(usuario)

    db.add(new_usuario)
    db.commit()
    db.refresh(new_usuario)
    return new_usuario

def leer_usuario(id:int, db:Session=Depends(get_db)):
    usuario = db.get(Usuario, id)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No existe usuario con el id {id}")
    return usuario

def actualizar_usuario(id:int, usuario:UsuarioActualizar, db:Session=Depends(get_db)):
    usuario_actualizar = db.get(Usuario, id)

    if not usuario_actualizar:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No existe usuario con el id {id}")

    usuario_data = usuario.model_dump(exclude_unset=True)
    for key, value in usuario_data.items():
        setattr(usuario_actualizar, key, value)

    db.add(usuario_actualizar)
    db.commit()
    db.refresh(usuario_actualizar)

    return usuario_actualizar

def borrar_usuario(id:int, db:Session=Depends(get_db)):
    usuario = db.get(Usuario, id)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No existe usuario con el id {id}")
    
    db.delete(usuario)
    db.commit()
    return {"ok": True}
