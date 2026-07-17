from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Importamos nuestros archivos
import model_user, schemas_user, crud_user
from config import engine, get_db

# =====================================================================
# INICIALIZACIÓN Y CONFIGURACIÓN
# =====================================================================

# 1. Crear las tablas en la Base de Datos
# Esta línea le dice a SQLAlchemy que revise 'models.py' y ejecute los CREATE TABLE
# en MySQL (si las tablas aún no existen).
model_user.Base.metadata.create_all(bind=engine)

# 2. Inicializar la app FastAPI
app = FastAPI(title="CRUD FastAPI Usuarios", description="API para gestión de usuarios")

# 3. Configurar CORS (Cross-Origin Resource Sharing)
# Permite que el frontend (HTML/JS) se comunique con el backend sin errores de seguridad.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permitir peticiones desde cualquier origen (en producción esto debe ser específico)
    allow_credentials=True,
    allow_methods=["*"], # Permitir todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],
)

# 4. Montar archivos estáticos
# Permite a FastAPI servir nuestros archivos HTML, CSS y JS desde la carpeta 'static'
import os
os.makedirs("static/css", exist_ok=True)
os.makedirs("static/js", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ruta raíz para servir el index.html
@app.get("/")
def read_root():
    return {"message": "Bienvenidos a la API de gestión de usuarios"}

# =====================================================================
# RUTAS DE LA API (Endpoints)
# =====================================================================
# 'Depends(get_db)' inyecta la conexión a la base de datos en cada ruta.

# CREAR USUARIO
@app.post("/users/", response_model=schemas_user.UserResponse)
def create_usuario(usuario: schemas_user.UserCreate, db: Session = Depends(get_db)):
    # Verificamos que el email no esté registrado previamente
    db_usuario = db.query(model_user.User).filter(model_user.User.email_user == usuario.email_user).first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="El Email ya está registrado")
    # Si todo está bien, llamamos a la función de crud.py para crearlo
    return crud_user.create_user(db=db, user=usuario)

# LEER TODOS LOS USUARIOS
@app.get("/users/", response_model=list[schemas_user.UserResponse])
def read_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    usuarios = crud_user.get_users(db, skip=skip, limit=limit)
    return usuarios

# LEER UN USUARIO POR ID
@app.get("/users/{user_id}", response_model=schemas_user.UserResponse)
def read_usuario(user_id: int, db: Session = Depends(get_db)):
    db_usuario = crud_user.get_user(db, user_id=user_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

# ACTUALIZAR USUARIO
@app.put("/users/{user_id}", response_model=schemas_user.UserResponse)
def update_usuario(user_id: int, user: schemas_user.UserCreate, db: Session = Depends(get_db)):
    db_usuario = crud_user.update_user(db, user_id=user_id, user_updated=user)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

# ELIMINAR USUARIO
@app.delete("/users/{user_id}")
def delete_usuario(user_id: int, db: Session = Depends(get_db)):
    db_usuario = crud_user.delete_user(db, user_id=user_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado correctamente"}
