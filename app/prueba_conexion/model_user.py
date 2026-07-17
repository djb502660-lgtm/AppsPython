from sqlalchemy import Column, Integer, String
from config import Base

# =====================================================================
# EXPLICACIÓN DE LOS MODELOS (ORM)
# =====================================================================
# SQLAlchemy es un ORM (Object Relational Mapper). Esto significa que 
# mapea (relaciona) Clases de Python con Tablas en tu base de datos MySQL.
# Al heredar de 'Base' (creado en database.py), le decimos a SQLAlchemy
# que esta clase debe convertirse en una tabla.

class User(Base):
    # '__tablename__' define el nombre exacto de la tabla en MySQL.
    __tablename__ = "users"

    # A continuación, definimos las columnas de la tabla.
    # Column(Tipo, configuraciones adicionales...)
    
    # 'id': Es la llave primaria (primary_key=True), única por registro. 
    # 'index=True' crea un índice en la BD para buscar usuarios por ID mucho más rápido.
    id = Column(Integer, primary_key=True, index=True)
    
    # 'nombre': Una cadena de texto (String).
    name_user = Column(String(100), nullable=False)
    
    # 'email': Cadena de texto, debe ser único (unique=True).
    email_user = Column(String(100), unique=True, index=True, nullable=False)
    
    # 'telefono': Cadena de texto, opcional.
    password_user= Column(String(100), nullable=False)
