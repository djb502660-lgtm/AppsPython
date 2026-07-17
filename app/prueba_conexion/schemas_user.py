from pydantic import BaseModel, EmailStr
from typing import Optional

# =====================================================================
# EXPLICACIÓN DE LOS ESQUEMAS (PYDANTIC)
# =====================================================================
# Pydantic se encarga de la VALIDACIÓN de los datos que entran y salen
# de nuestra API. A diferencia de SQLAlchemy (que habla con la BD), 
# Pydantic asegura que el JSON que envía el frontend tenga el formato correcto.

# Esquema base con los campos comunes.
class UserBase(BaseModel):
    name_user: str
    email_user: EmailStr 
    password_user: str


class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserDelete(UserBase):
    pass

class UserLogin(UserBase):
    pass

class UserLogout(BaseModel):
    pass

class UserRegister(UserBase):
    pass


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True 
