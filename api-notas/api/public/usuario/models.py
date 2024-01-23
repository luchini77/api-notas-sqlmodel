from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional

#from api.public.nota.models import Nota


class UsuarioBase(SQLModel):
    nombre: str

    class Config:
        json_schema_extra = {
            "example": {
                "nombre":"Kuky"
            }
        }

class Usuario(UsuarioBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    notas: List["Nota"] = Relationship(back_populates="usuario")

class UsuarioCrear(UsuarioBase):
    pass 

class UsuarioLeer(UsuarioBase):
    id: int
    nombre: str | None = None


class UsuarioUpdate(UsuarioBase):
    nombre: str | None = None