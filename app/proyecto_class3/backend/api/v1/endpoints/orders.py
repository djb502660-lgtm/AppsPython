from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from core.deps import get_db, get_current_active_user
from schemas.order import OrderResponse, OrderCreateRequest, OrderStatusUpdateRequest
from services.order_service import OrderService
from models.user import User

router = APIRouter()

# Función auxiliar temporal para saber si es admin (en la práctica se usa RBAC via dependency)
def is_admin(user: User) -> bool:
    return user.role_id in [1, 2] # Super Admin, Administrador

@router.post("", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(
    order_in: OrderCreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return OrderService(db).create_order(order_in, current_user)

@router.get("/me", response_model=List[OrderResponse])
def get_my_orders(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return OrderService(db).get_orders(current_user=current_user, as_admin=False)

@router.get("", response_model=List[OrderResponse])
def get_orders(
    status_filter: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    if not is_admin(current_user) and current_user.role_id not in [5, 6]: # Cocina, Repartidor
        raise HTTPException(status_code=403, detail="Acceso denegado")
        
    statuses = [status_filter] if status_filter else None
    return OrderService(db).get_orders(current_user=current_user, as_admin=True, statuses=statuses)

@router.get("/{id}", response_model=OrderResponse)
def get_order(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    admin_access = is_admin(current_user) or current_user.role_id in [5, 6]
    return OrderService(db).get_order(id, current_user, as_admin=admin_access)

@router.put("/{id}/status", response_model=OrderResponse)
def update_order_status(
    id: int,
    status_update: OrderStatusUpdateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    # En un sistema real esto lo validaría RBAC dependiendo del estado destino.
    admin_access = is_admin(current_user) or current_user.role_id in [5, 6]
    if not admin_access:
        raise HTTPException(status_code=403, detail="Solo el staff puede cambiar estados")
    return OrderService(db).update_status(id, status_update, current_user, as_admin=True)

# Endpoint simulado de carga de archivo
@router.post("/{id}/payment-proof", response_model=OrderResponse)
def upload_payment_proof(
    id: int,
    file_url: str, # En un caso real usaríamos UploadFile
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    return OrderService(db).upload_payment_proof(id, file_url, current_user)
