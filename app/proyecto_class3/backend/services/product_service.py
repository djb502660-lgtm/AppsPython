from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import Optional
from repositories.product_repository import CategoryRepository, ProductRepository
from schemas.product import CategoryCreateRequest, CategoryUpdateRequest, ProductCreateRequest, ProductUpdateRequest

class CategoryService:
    def __init__(self, db: Session):
        self.repo = CategoryRepository(db)

    def get_categories(self, active_only: bool = True):
        return self.repo.get_all(active_only)

    def get_category(self, id: int):
        cat = self.repo.get_by_id(id)
        if not cat:
            raise HTTPException(status_code=404, detail="Categoría no encontrada")
        return cat

    def create_category(self, cat_in: CategoryCreateRequest):
        return self.repo.create(cat_in)

    def update_category(self, id: int, cat_in: CategoryUpdateRequest):
        cat = self.get_category(id)
        for field, value in cat_in.model_dump(exclude_unset=True).items():
            setattr(cat, field, value)
        return self.repo.update(cat)


class ProductService:
    def __init__(self, db: Session):
        self.repo = ProductRepository(db)
        self.cat_repo = CategoryRepository(db)

    def get_products(self, active_only: bool = True, category_id: Optional[int] = None, search: Optional[str] = None):
        return self.repo.get_all(active_only, category_id, search)

    def get_product(self, id: int):
        prod = self.repo.get_by_id(id)
        if not prod:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return prod

    def create_product(self, prod_in: ProductCreateRequest):
        cat = self.cat_repo.get_by_id(prod_in.category_id)
        if not cat:
            raise HTTPException(status_code=400, detail="La categoría especificada no existe")
        return self.repo.create(prod_in)

    def update_product(self, id: int, prod_in: ProductUpdateRequest):
        prod = self.get_product(id)
        
        if prod_in.category_id:
            cat = self.cat_repo.get_by_id(prod_in.category_id)
            if not cat:
                raise HTTPException(status_code=400, detail="La categoría especificada no existe")
                
        for field, value in prod_in.model_dump(exclude_unset=True).items():
            setattr(prod, field, value)
            
        return self.repo.update(prod)
