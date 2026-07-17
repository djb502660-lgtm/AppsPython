from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker



host="localhost"
user="root"
password=""
port="3306"
database="base_restaurantes"

#String de conexiones
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

# Motor de base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#Sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base para modelos
Base = declarative_base()


#Función para obtener la base de datos

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()