from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class InvoiceCreateRequest(BaseModel):
    billing_address: Optional[str] = None
    tax_id: Optional[str] = None

class InvoiceResponse(BaseModel):
    id: int
    order_id: int
    invoice_number: str
    billing_address: Optional[str]
    tax_id: Optional[str]
    total_amount: float
    tax_amount: float
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

class CreditNoteRequest(BaseModel):
    reason: Optional[str] = None

class CreditNoteResponse(BaseModel):
    id: int
    invoice_id: int
    credit_note_number: str
    amount: float
    reason: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True
