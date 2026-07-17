from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List, Optional
from repositories.order_repository import OrderRepository
from repositories.product_repository import ProductRepository
from schemas.order import OrderCreateRequest, OrderStatusUpdateRequest
from models.order import Order, OrderItem
from models.user import User

class OrderService:
    def __init__(self, db: Session):
        self.repo = OrderRepository(db)
        self.prod_repo = ProductRepository(db)
        self.db = db

    def get_orders(self, current_user: User, as_admin: bool = False, statuses: Optional[List[str]] = None):
        # Si no es admin (o rol con permisos globales), solo ve sus propios pedidos
        user_id = None if as_admin else current_user.id
        return self.repo.get_all(user_id=user_id, statuses=statuses)

    def get_order(self, order_id: int, current_user: User, as_admin: bool = False):
        order = self.repo.get_by_id(order_id)
        if not order:
            raise HTTPException(status_code=404, detail="Pedido no encontrado")
        if not as_admin and order.user_id != current_user.id:
            raise HTTPException(status_code=403, detail="No tienes acceso a este pedido")
        return order

    def create_order(self, order_in: OrderCreateRequest, current_user: User):
        total = 0.0
        order_items = []
        
        for item_req in order_in.items:
            product = self.prod_repo.get_by_id(item_req.product_id)
            if not product or not product.is_active:
                raise HTTPException(status_code=400, detail=f"Producto {item_req.product_id} no disponible")
            if product.stock < item_req.quantity:
                raise HTTPException(status_code=400, detail=f"Stock insuficiente para {product.name}")
            
            # Reservar stock temporalmente (Kardex salida)
            product.stock -= item_req.quantity
            
            unit_price = product.price
            total += unit_price * item_req.quantity
            
            order_items.append(
                OrderItem(
                    product_id=product.id,
                    quantity=item_req.quantity,
                    unit_price=unit_price
                )
            )

        new_order = Order(
            user_id=current_user.id,
            total=total,
            status="PENDING",
            items=order_items
        )
        
        return self.repo.create(new_order)

    def update_status(self, order_id: int, status_update: OrderStatusUpdateRequest, current_user: User, as_admin: bool = False):
        order = self.get_order(order_id, current_user, as_admin)
        
        # Logica de máquina de estados y devolucion de stock si REJECTED
        old_status = order.status
        new_status = status_update.status.value
        
        if old_status == "REJECTED" or old_status == "DELIVERED":
             raise HTTPException(status_code=400, detail="El pedido está en un estado final y no puede cambiar")
             
        if new_status == "REJECTED":
            # Devolver stock
            for item in order.items:
                product = self.prod_repo.get_by_id(item.product_id)
                if product:
                    product.stock += item.quantity
        
        order.status = new_status
        return self.repo.update(order)

    def upload_payment_proof(self, order_id: int, file_url: str, current_user: User):
        order = self.get_order(order_id, current_user, as_admin=False)
        if order.status != "PENDING":
             raise HTTPException(status_code=400, detail="El pedido no está esperando pago")
             
        order.payment_proof_url = file_url
        order.status = "VALIDATING"
        return self.repo.update(order)
