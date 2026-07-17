from sqlalchemy.orm import Session
from typing import List, Optional
from models.inventory import InventoryTransaction

class InventoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_product_id(self, product_id: int) -> List[InventoryTransaction]:
        return self.db.query(InventoryTransaction)\
            .filter(InventoryTransaction.product_id == product_id)\
            .order_by(InventoryTransaction.created_at.desc())\
            .all()

    def get_recent(self, limit: int = 50) -> List[InventoryTransaction]:
        return self.db.query(InventoryTransaction)\
            .order_by(InventoryTransaction.created_at.desc())\
            .limit(limit)\
            .all()

    def create(self, transaction: InventoryTransaction) -> InventoryTransaction:
        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)
        return transaction
