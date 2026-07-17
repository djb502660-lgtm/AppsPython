from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from core.deps import get_db, get_current_active_user
from schemas.inventory import InventoryMovementRequest, InventoryMovementResponse
from services.inventory_service import InventoryService
from models.user import User

router = APIRouter()

# Función auxiliar temporal
def has_inventory_access(user: User) -> bool:
    return user.role_id in [1, 2, 4] # Super Admin, Administrador, Inventario

@router.post("/movements", response_model=InventoryMovementResponse, status_code=status.HTTP_201_CREATED)
def record_movement(
    request: InventoryMovementRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    if not has_inventory_access(current_user):
        raise HTTPException(status_code=403, detail="Acceso denegado")
    return InventoryService(db).record_movement(request, current_user)

@router.get("/kardex/{product_id}", response_model=List[InventoryMovementResponse])
def get_kardex(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    if not has_inventory_access(current_user):
        raise HTTPException(status_code=403, detail="Acceso denegado")
    return InventoryService(db).get_kardex(product_id)

@router.get("/movements", response_model=List[InventoryMovementResponse])
def get_recent_movements(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    if not has_inventory_access(current_user):
        raise HTTPException(status_code=403, detail="Acceso denegado")
    return InventoryService(db).get_recent_movements()
