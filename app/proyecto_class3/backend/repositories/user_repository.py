from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserRegisterRequest
from core.security import get_password_hash

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def get_by_id(self, id: int) -> User | None:
        return self.db.query(User).filter(User.id == id).first()

    def create(self, user_in: UserRegisterRequest) -> User:
        db_obj = User(
            email=user_in.email,
            password_hash=get_password_hash(user_in.password),
            first_name=user_in.first_name,
            last_name=user_in.last_name
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update(self, user: User) -> User:
        self.db.commit()
        self.db.refresh(user)
        return user
