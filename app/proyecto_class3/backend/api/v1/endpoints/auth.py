from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from core.deps import get_db
from schemas.user import UserRegisterRequest, UserLoginRequest, UserResponse, Token
from services.user_service import UserService

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_in: UserRegisterRequest, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.register_user(user_in)

@router.post("/login", response_model=Token)
def login(user_in: UserLoginRequest, db: Session = Depends(get_db)):
    service = UserService(db)
    access_token = service.authenticate(user_in)
    return {"access_token": access_token, "token_type": "bearer"}
