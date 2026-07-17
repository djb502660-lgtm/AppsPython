from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from core.deps import get_db, get_current_active_user
from schemas.role import RoleResponse, RoleDetailResponse, RoleCreateRequest, RoleUpdateRequest, PermissionResponse
from services.role_service import RoleService
from models.user import User

router = APIRouter()

# En un sistema real, un middleware o Dependency verificaria el permiso 'roles:MANAGE'
# Por simplificacion, asumiremos que get_current_active_user protege estos endpoints 
# y que se aplicará la validación RBAC en una Skill posterior.

@router.get("", response_model=List[RoleResponse])
def get_roles(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return RoleService(db).get_roles()

@router.post("", response_model=RoleDetailResponse, status_code=status.HTTP_201_CREATED)
def create_role(role_in: RoleCreateRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return RoleService(db).create_role(role_in)

@router.get("/permissions", response_model=List[PermissionResponse])
def get_permissions(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return RoleService(db).get_permissions()

@router.get("/{role_id}", response_model=RoleDetailResponse)
def get_role(role_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return RoleService(db).get_role(role_id)

@router.put("/{role_id}", response_model=RoleDetailResponse)
def update_role(role_id: int, role_in: RoleUpdateRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return RoleService(db).update_role(role_id, role_in)

@router.delete("/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return RoleService(db).delete_role(role_id)
