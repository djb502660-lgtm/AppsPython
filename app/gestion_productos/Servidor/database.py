from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# String de conexión a la base de datos
SQLALCHEMY_DATABASE_URL="mysql+pymysql://root:@localhost:3306/Gestion_productos_dbs"

# Crear motor de conexiones a la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# Sesiones locales las cuales son espacios temporales para trabajr con la abe de dato
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

