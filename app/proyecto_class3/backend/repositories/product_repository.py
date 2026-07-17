from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List, Optional
from models.product import Product, Category
from schemas.product import CategoryCreateRequest, ProductCreateRequest

class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, active_only: bool = True) -> List[Category]:
        query = self.db.query(Category)
        if active_only:
            query = query.filter(Category.is_active == True)
        return query.all()

    def get_by_id(self, id: int) -> Category | None:
        return self.db.query(Category).filter(Category.id == id).first()

    def create(self, cat_in: CategoryCreateRequest) -> Category:
        db_obj = Category(**cat_in.model_dump())
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update(self, category: Category) -> Category:
        self.db.commit()
        self.db.refresh(category)
        return category


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, active_only: bool = True, category_id: Optional[int] = None, search: Optional[str] = None) -> List[Product]:
        query = self.db.query(Product)
        if active_only:
            query = query.filter(Product.is_active == True)
            # Only return products if their category is also active
            query = query.join(Category).filter(Category.is_active == True)
        
        if category_id:
            query = query.filter(Product.category_id == category_id)
            
        if search:
            query = query.filter(or_(Product.name.ilike(f"%{search}%"), Product.description.ilike(f"%{search}%")))
            
        return query.all()

    def get_by_id(self, id: int) -> Product | None:
        return self.db.query(Product).filter(Product.id == id).first()

    def create(self, prod_in: ProductCreateRequest) -> Product:
        db_obj = Product(**prod_in.model_dump())
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update(self, product: Product) -> Product:
        self.db.commit()
        self.db.refresh(product)
        return product
