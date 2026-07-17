from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config
import model_contacto
import schemas_contacto
import crud_contacto

engine = create_engine(
    config.DATABASE_URL,
    connect_args={"check_same_thread": False}
)
model_contacto.Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI(title="Prueba de Conexión - Contactos")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/contactos/")
def read_contactos(skip=0, limit=100, db=Depends(get_db)):
    return crud_contacto.get_contactos(db, skip=skip, limit=limit)


@app.get("/contactos/{contacto_id}")
def read_contacto(contacto_id, db=Depends(get_db)):
    db_contacto = crud_contacto.get_contacto(db, contacto_id)
    if db_contacto is None:
        raise HTTPException(status_code=404, detail="Contacto no encontrado")
    return db_contacto


@app.post("/contactos/")
def create_contacto(contacto: schemas_contacto.ContactoCrear, db=Depends(get_db)):
    return crud_contacto.create_contacto(db, contacto)


@app.put("/contactos/{contacto_id}")
def update_contacto(contacto_id, contacto: schemas_contacto.ContactoActualizar, db=Depends(get_db)):
    db_contacto = crud_contacto.update_contacto(db, contacto_id, contacto)
    if db_contacto is None:
        raise HTTPException(status_code=404, detail="Contacto no encontrado")
    return db_contacto


@app.delete("/contactos/{contacto_id}")
def delete_contacto(contacto_id, db=Depends(get_db)):
    db_contacto = crud_contacto.delete_contacto(db, contacto_id)
    if db_contacto is None:
        raise HTTPException(status_code=404, detail="Contacto no encontrado")
    return {"mensaje": "Contacto eliminado"}
