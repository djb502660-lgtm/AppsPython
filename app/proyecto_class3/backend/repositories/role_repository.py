from sqlalchemy.orm import Session
from models.role import Role, Permission
from schemas.role import RoleCreateRequest
from typing import List

class RoleRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Role]:
        return self.db.query(Role).all()

    def get_by_id(self, id: int) -> Role | None:
        return self.db.query(Role).filter(Role.id == id).first()

    def create(self, role_in: RoleCreateRequest, permissions: List[Permission]) -> Role:
        db_obj = Role(name=role_in.name, description=role_in.description)
        db_obj.permissions = permissions
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update(self, role: Role, permissions: List[Permission] = None) -> Role:
        if permissions is not None:
            role.permissions = permissions
        self.db.commit()
        self.db.refresh(role)
        return role

    def delete(self, role: Role):
        self.db.delete(role)
        self.db.commit()

class PermissionRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Permission]:
        return self.db.query(Permission).all()

    def get_by_ids(self, ids: List[int]) -> List[Permission]:
        return self.db.query(Permission).filter(Permission.id.in_(ids)).all()
