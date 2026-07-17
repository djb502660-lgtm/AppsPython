from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field
from enum import Enum

class OrderStatus(str, Enum):
    PENDING = "PENDING"
    VALIDATING = "VALIDATING"
    APPROVED = "APPROVED"
    PREPARING = "PREPARING"
    READY = "READY"
    DELIVERED = "DELIVERED"
    REJECTED = "REJECTED"

class OrderItemRequest(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)

class OrderCreateRequest(BaseModel):
    items: List[OrderItemRequest]

class OrderStatusUpdateRequest(BaseModel):
    status: OrderStatus

class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    unit_price: float

    class Config:
        from_attributes = True

class OrderResponse(BaseModel):
    id: int
    user_id: int
    total: float
    status: str
    payment_proof_url: Optional[str]
    created_at: datetime
    items: List[OrderItemResponse] = []

    class Config:
        from_attributes = True
