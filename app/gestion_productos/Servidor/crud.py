from sqlalchemy.orm import Session
import models, schemas

# 1.Crear un producto
def crear_producto(db:Session, producto:schemas.ProductoCreate):
    db_producto=models.Producto(
        nombre=producto.nombre,
        descripcion=producto.descripcion,
        precio=producto.precio,
        cantidad=producto.cantidad
    )
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

# Obteener los productos
def get_productos(db:Session,skip: int=0,limit:int=100):
  return db.query(models.Producto).offset(skip).limit(limit).all()
# Obtener un solo registro por id
def get_producto(db:Session, producto_id:int):
  return db.query(models.Producto).filter(models.Producto.id==producto_id).first()