from typing import Optional, List
from pydantic import BaseModel, Field

# --- Categories ---
class CategoryBase(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    description: Optional[str] = None
    is_active: bool = True

class CategoryCreateRequest(CategoryBase):
    pass

class CategoryUpdateRequest(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True

# --- Products ---
class ProductBase(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    description: Optional[str] = None
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    is_active: bool = True

class ProductCreateRequest(ProductBase):
    category_id: int

class ProductUpdateRequest(ProductBase):
    category_id: Optional[int] = None

class ProductResponse(ProductBase):
    id: int
    category_id: int
    category: Optional[CategoryResponse] = None

    class Config:
        from_attributes = True
