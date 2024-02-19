from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship

from api.public.usuario.models import Usuario, UsuarioLeer

class TareaBase(SQLModel):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    terminado: Optional[bool] = False
    fecha_creacion: Optional[str] = None

    usuario_id: Optional[int] = Field(default=None, foreign_key='usuario.id')

    class Config:
        json_schema_extra = {
            'example': {
                'titulo':'Mimir',
                'descripcion':'Todo el dia',
                'terminado':False,
                'usuario_id':1
            }
        }

class Tarea(TareaBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    usuario: Usuario = Relationship(back_populates='tareas')

class TareaCrear(TareaBase):
    pass 

class TareaLeer(TareaBase):
    id: int
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    terminado: Optional[bool] = None
    fecha_creacion: Optional[str] = None
    usuario_id: Optional[int] = None

class TareaLeerJoin(TareaBase):
    usuario: Optional[UsuarioLeer] = None

class TareaActualizar(TareaBase):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    terminado: Optional[bool] = None
    fecha_creacion: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "titulo":"Mimir",
                "descripcion":"Todo el dia",
                "terminado": False
            }
        }