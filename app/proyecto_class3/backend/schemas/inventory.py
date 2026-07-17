from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from enum import Enum

class TransactionType(str, Enum):
    IN = "IN"
    OUT = "OUT"
    ADJUSTMENT = "ADJUSTMENT"

class InventoryMovementRequest(BaseModel):
    product_id: int
    transaction_type: TransactionType
    quantity: int = Field(gt=0)
    reference: Optional[str] = None
    notes: Optional[str] = None

class InventoryMovementResponse(BaseModel):
    id: int
    product_id: int
    transaction_type: str
    quantity: int
    previous_stock: int
    new_stock: int
    reference: Optional[str]
    notes: Optional[str]
    created_at: datetime
    created_by: int

    class Config:
        from_attributes = True
