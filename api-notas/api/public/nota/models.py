from typing import Optional
from sqlmodel import Field, SQLModel,Relationship

from api.public.usuario.models import Usuario


class NotaBase(SQLModel):
    titulo: str
    descripcion: str
    terminado: Optional[bool] = False
    fecha_creacion: Optional[str] = None
    usuario_id: int = Field(foreign_key="usuario.id")
    

    class Config:
        json_schema_extra = {
            "example": {
                "titulo":"Comer",
                "descripcion":"Una buena pajarita",
                "terminado": False,
                "usuario_id": 1
            }
        }

class Nota(NotaBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    usuario: Usuario = Relationship(back_populates="notas")

class NotaCrear(NotaBase):
    pass

class NotaLeer(NotaBase):
    id: int
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    terminado: Optional[bool] = None
    fecha_creacion: Optional[str] = None
    usuario_id: Optional[int]

class NotaUpdate(NotaBase):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    terminado: Optional[bool] = None
    fecha_creacion: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "titulo":"Comer",
                "descripcion":"Una buena pajarita",
                "terminado": False
            }
        }
