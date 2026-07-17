from typing import Optional, List
from pydantic import BaseModel, Field

class PermissionResponse(BaseModel):
    id: int
    name: str
    module: str

    class Config:
        from_attributes = True

class RoleBase(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    description: Optional[str] = None

class RoleCreateRequest(RoleBase):
    permission_ids: List[int] = []

class RoleUpdateRequest(RoleBase):
    permission_ids: List[int] = []

class RoleResponse(RoleBase):
    id: int

    class Config:
        from_attributes = True

class RoleDetailResponse(RoleResponse):
    permissions: List[PermissionResponse] = []
