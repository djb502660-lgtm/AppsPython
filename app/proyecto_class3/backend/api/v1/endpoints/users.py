from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.deps import get_db, get_current_active_user
from schemas.user import UserResponse, UserUpdateRequest, PasswordUpdateRequest
from services.user_service import UserService
from models.user import User

router = APIRouter()

@router.get("/me", response_model=UserResponse)
def get_user_me(
    current_user: User = Depends(get_current_active_user)
):
    return current_user

@router.put("/me", response_model=UserResponse)
def update_user_me(
    user_in: UserUpdateRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    service = UserService(db)
    return service.update_user(current_user.id, user_in)

@router.put("/me/password")
def update_password_me(
    password_in: PasswordUpdateRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    service = UserService(db)
    service.update_password(current_user.id, password_in)
    return {"msg": "Contraseña actualizada correctamente"}
