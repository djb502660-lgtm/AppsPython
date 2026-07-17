from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from core.deps import get_db, get_current_active_user
from schemas.product import CategoryResponse, CategoryCreateRequest, CategoryUpdateRequest
from services.product_service import CategoryService
from models.user import User

router = APIRouter()

@router.get("", response_model=List[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    # Público: Solo activas
    return CategoryService(db).get_categories(active_only=True)

@router.get("/all", response_model=List[CategoryResponse])
def get_all_categories(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    # Protegido: Todas
    return CategoryService(db).get_categories(active_only=False)

@router.post("", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(
    cat_in: CategoryCreateRequest, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    # Protegido
    return CategoryService(db).create_category(cat_in)

@router.put("/{id}", response_model=CategoryResponse)
def update_category(
    id: int, 
    cat_in: CategoryUpdateRequest, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    # Protegido
    return CategoryService(db).update_category(id, cat_in)
