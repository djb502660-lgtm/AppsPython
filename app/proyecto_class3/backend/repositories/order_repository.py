from sqlalchemy.orm import Session
from typing import List, Optional
from models.order import Order, OrderItem

class OrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, user_id: Optional[int] = None, statuses: Optional[List[str]] = None) -> List[Order]:
        query = self.db.query(Order)
        if user_id:
            query = query.filter(Order.user_id == user_id)
        if statuses:
            query = query.filter(Order.status.in_(statuses))
        return query.all()

    def get_by_id(self, id: int) -> Order | None:
        return self.db.query(Order).filter(Order.id == id).first()

    def create(self, order: Order) -> Order:
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return order

    def update(self, order: Order) -> Order:
        self.db.commit()
        self.db.refresh(order)
        return order
