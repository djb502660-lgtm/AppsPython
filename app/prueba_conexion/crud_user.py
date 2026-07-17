from sqlalchemy.orm import Session
import model_user, schemas_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_user.User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    
    return db.query(model_user.User).filter(model_user.User.id == user_id).first()


def create_user(db: Session, user: schemas_user.UserCreate):
    db_user = model_user.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: schemas_user):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    for var, value in vars(user).items():
        setattr(db_user, var, value)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user

def login_user(db: Session, user: schemas_user.UserLogin):
    db_user = db.query(model_user.User).filter(model_user.User.email == user.email_user).first()
    if not db_user:
        return None
    return db_user

def logout_user(db: Session, user: schemas_user.UserLogout):
    db_user = db.query(model_user.User).filter(model_user.User.email == user.email_user).first()
    if not db_user:
        return None
    return db_user

def register_user(db: Session, user: schemas_user.UserRegister):
    db_user = model_user.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user