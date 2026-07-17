
from sqlalchemy.orm import Session
import models, schemas


def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    # En SQL sería equivalente a: SELECT * FROM usuarios LIMIT 100 OFFSET 0;
    # db.query(models.Usuario) inicia una consulta a la tabla 'usuarios'.
    # .offset(skip) salta los primeros 'skip' registros (útil para paginación).
    # .limit(limit) trae un máximo de 'limit' registros.
    # .all() ejecuta la consulta y devuelve una lista de objetos.
    return db.query(models.Usuario).offset(skip).limit(limit).all()