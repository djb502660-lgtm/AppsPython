from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from repositories.user_repository import UserRepository
from schemas.user import UserRegisterRequest, UserLoginRequest, UserUpdateRequest, PasswordUpdateRequest
from core.security import verify_password, get_password_hash, create_access_token
from models.user import User

class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def register_user(self, user_in: UserRegisterRequest) -> User:
        user = self.repo.get_by_email(user_in.email)
        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El correo electrónico ya está registrado."
            )
        return self.repo.create(user_in)

    def authenticate(self, user_in: UserLoginRequest) -> str:
        user = self.repo.get_by_email(user_in.email)
        if not user or not verify_password(user_in.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Correo o contraseña incorrectos."
            )
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cuenta inactiva."
            )
        
        return create_access_token(subject=user.id)

    def get_user(self, user_id: int) -> User:
        user = self.repo.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return user

    def update_user(self, user_id: int, user_in: UserUpdateRequest) -> User:
        user = self.get_user(user_id)
        if user_in.first_name is not None:
            user.first_name = user_in.first_name
        if user_in.last_name is not None:
            user.last_name = user_in.last_name
        return self.repo.update(user)

    def update_password(self, user_id: int, password_in: PasswordUpdateRequest):
        user = self.get_user(user_id)
        if not verify_password(password_in.current_password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="La contraseña actual es incorrecta."
            )
        user.password_hash = get_password_hash(password_in.new_password)
        self.repo.update(user)
