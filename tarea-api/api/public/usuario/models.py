from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List


class UsuarioBase(SQLModel):
    nombre: str

    class Config:
        json_schema_extra = {
            'example': {
                'nombre':'Kuky'
            }
        }

class Usuario(UsuarioBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    tareas: List['Tarea'] = Relationship(back_populates='usuario')

class UsuarioCrear(UsuarioBase):
    pass 

class UsuarioLeer(UsuarioBase):
    id: int
    nombre: str | None = None

class UsuarioActualizar(UsuarioBase):
    nombre: str | None = None