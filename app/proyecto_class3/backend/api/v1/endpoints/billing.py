from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from core.deps import get_db, get_current_active_user
from schemas.billing import InvoiceResponse, InvoiceCreateRequest, CreditNoteResponse, CreditNoteRequest
from services.billing_service import BillingService
from models.user import User

router = APIRouter()

def has_billing_access(user: User) -> bool:
    return user.role_id in [1, 2, 3] # Super Admin, Admin, Cajero

@router.post("/invoices/order/{order_id}", response_model=InvoiceResponse, status_code=status.HTTP_201_CREATED)
def create_invoice(
    order_id: int,
    invoice_in: InvoiceCreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    if not has_billing_access(current_user):
        raise HTTPException(status_code=403, detail="Acceso denegado a facturación")
    return BillingService(db).create_invoice(order_id, invoice_in)

@router.get("/invoices", response_model=List[InvoiceResponse])
def get_invoices(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    if not has_billing_access(current_user):
        raise HTTPException(status_code=403, detail="Acceso denegado a facturación")
    return BillingService(db).get_invoices()

@router.get("/invoices/{id}", response_model=InvoiceResponse)
def get_invoice(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    # Un cliente podría querer ver su factura, omitiendo validación estricta para el demo 
    # (en producción, validar si el cliente es dueño del pedido asociado)
    return BillingService(db).get_invoice(id)

@router.post("/credit-notes/invoice/{invoice_id}", response_model=CreditNoteResponse, status_code=status.HTTP_201_CREATED)
def create_credit_note(
    invoice_id: int,
    request: CreditNoteRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    if not has_billing_access(current_user):
        raise HTTPException(status_code=403, detail="Acceso denegado a facturación")
    return BillingService(db).create_credit_note(invoice_id, request)
