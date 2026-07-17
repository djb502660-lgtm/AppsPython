from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List, Optional
from core.deps import get_db, get_current_active_user
from schemas.product import ProductResponse, ProductCreateRequest, ProductUpdateRequest
from services.product_service import ProductService
from models.user import User

router = APIRouter()

@router.get("", response_model=List[ProductResponse])
def get_products(
    category_id: Optional[int] = None, 
    search: Optional[str] = None, 
    db: Session = Depends(get_db)
):
    # Público: Sólo productos activos de categorías activas
    return ProductService(db).get_products(active_only=True, category_id=category_id, search=search)

@router.get("/all", response_model=List[ProductResponse])
def get_all_products(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    # Protegido: Todos los productos
    return ProductService(db).get_products(active_only=False)

@router.get("/{id}", response_model=ProductResponse)
def get_product(id: int, db: Session = Depends(get_db)):
    # Público
    return ProductService(db).get_product(id)

@router.post("", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(
    prod_in: ProductCreateRequest, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    # Protegido
    return ProductService(db).create_product(prod_in)

@router.put("/{id}", response_model=ProductResponse)
def update_product(
    id: int, 
    prod_in: ProductUpdateRequest, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    # Protegido
    return ProductService(db).update_product(id, prod_in)
