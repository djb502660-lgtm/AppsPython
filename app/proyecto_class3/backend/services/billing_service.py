from sqlalchemy.orm import Session
from fastapi import HTTPException
from repositories.billing_repository import BillingRepository
from repositories.order_repository import OrderRepository
from schemas.billing import InvoiceCreateRequest, CreditNoteRequest
from models.billing import Invoice, CreditNote
import uuid

class BillingService:
    def __init__(self, db: Session):
        self.repo = BillingRepository(db)
        self.order_repo = OrderRepository(db)

    def generate_invoice_number(self) -> str:
        # En la realidad usaría una secuencia atómica en BD, o formato F001-XXXX
        # Para propósitos de este módulo, generamos un identificador único corto
        return f"F001-{uuid.uuid4().hex[:8].upper()}"

    def generate_credit_note_number(self) -> str:
        return f"NC01-{uuid.uuid4().hex[:8].upper()}"

    def get_invoices(self):
        return self.repo.get_invoices()

    def get_invoice(self, id: int):
        invoice = self.repo.get_invoice_by_id(id)
        if not invoice:
            raise HTTPException(status_code=404, detail="Factura no encontrada")
        return invoice

    def create_invoice(self, order_id: int, invoice_in: InvoiceCreateRequest):
        order = self.order_repo.get_by_id(order_id)
        if not order:
            raise HTTPException(status_code=404, detail="Pedido no encontrado")
        
        # Regla: Solo pedidos aprobados o superiores pueden ser facturados
        if order.status in ["PENDING", "VALIDATING", "REJECTED"]:
            raise HTTPException(status_code=400, detail="El pedido no está en un estado válido para ser facturado")
            
        existing_invoice = self.repo.get_invoice_by_order(order_id)
        if existing_invoice:
            raise HTTPException(status_code=400, detail="Este pedido ya tiene una factura activa")

        # Simplificaremos los impuestos: 16% sobre el total, asumiendo total_amount es base + tax 
        # O en este caso, tomaremos order.total como base y agregaremos tax, o asumimos que ya lo tiene.
        # Asumiremos que order.total ya es el valor a pagar total (incluido impuestos para B2C).
        tax = order.total * 0.16
        
        invoice = Invoice(
            order_id=order_id,
            invoice_number=self.generate_invoice_number(),
            billing_address=invoice_in.billing_address,
            tax_id=invoice_in.tax_id,
            total_amount=order.total,
            tax_amount=tax,
            status="ISSUED"
        )
        return self.repo.create_invoice(invoice)

    def create_credit_note(self, invoice_id: int, request: CreditNoteRequest):
        invoice = self.get_invoice(invoice_id)
        if invoice.status == "CANCELLED":
            raise HTTPException(status_code=400, detail="La factura ya fue anulada")

        credit_note = CreditNote(
            invoice_id=invoice.id,
            credit_note_number=self.generate_credit_note_number(),
            amount=invoice.total_amount,
            reason=request.reason
        )
        
        invoice.status = "CANCELLED"
        self.repo.update_invoice(invoice)
        
        return self.repo.create_credit_note(credit_note)
