from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from repositories.role_repository import RoleRepository, PermissionRepository
from schemas.role import RoleCreateRequest, RoleUpdateRequest
from models.role import Role
from models.user import User

class RoleService:
    def __init__(self, db: Session):
        self.repo = RoleRepository(db)
        self.perm_repo = PermissionRepository(db)
        self.db = db # needed for checking users

    def get_roles(self):
        return self.repo.get_all()

    def get_role(self, role_id: int):
        role = self.repo.get_by_id(role_id)
        if not role:
            raise HTTPException(status_code=404, detail="Rol no encontrado")
        return role

    def create_role(self, role_in: RoleCreateRequest):
        perms = self.perm_repo.get_by_ids(role_in.permission_ids)
        if len(perms) != len(role_in.permission_ids):
            raise HTTPException(status_code=400, detail="Uno o más permisos son inválidos")
        return self.repo.create(role_in, perms)

    def update_role(self, role_id: int, role_in: RoleUpdateRequest):
        if role_id in [1, 7]: # Super Admin, Cliente (protegidos)
            raise HTTPException(status_code=403, detail="Roles del sistema no pueden ser modificados")
        
        role = self.get_role(role_id)
        role.name = role_in.name
        role.description = role_in.description
        
        perms = self.perm_repo.get_by_ids(role_in.permission_ids)
        return self.repo.update(role, perms)

    def delete_role(self, role_id: int):
        if role_id in [1, 7]:
            raise HTTPException(status_code=403, detail="Roles del sistema no pueden ser eliminados")
            
        role = self.get_role(role_id)
        
        # Check integrity
        users_count = self.db.query(User).filter(User.role_id == role_id).count()
        if users_count > 0:
            raise HTTPException(status_code=400, detail="No se puede eliminar un rol asignado a usuarios")
            
        self.repo.delete(role)
        return {"msg": "Rol eliminado correctamente"}

    def get_permissions(self):
        return self.perm_repo.get_all()
