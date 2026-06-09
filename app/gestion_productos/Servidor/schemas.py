from pydantic import BaseModel
from typing import Optional


class ProductoBase(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    cantidad: int

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    pass

class Producto(ProductoBase):
    id: int
    
    class Config:
        from_attributes = True
