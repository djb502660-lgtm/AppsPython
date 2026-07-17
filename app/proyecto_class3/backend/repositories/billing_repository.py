from sqlalchemy.orm import Session
from typing import List, Optional
from models.billing import Invoice, CreditNote

class BillingRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_invoices(self) -> List[Invoice]:
        return self.db.query(Invoice).all()

    def get_invoice_by_id(self, id: int) -> Invoice | None:
        return self.db.query(Invoice).filter(Invoice.id == id).first()

    def get_invoice_by_order(self, order_id: int) -> Invoice | None:
        return self.db.query(Invoice).filter(Invoice.order_id == order_id).first()

    def create_invoice(self, invoice: Invoice) -> Invoice:
        self.db.add(invoice)
        self.db.commit()
        self.db.refresh(invoice)
        return invoice

    def update_invoice(self, invoice: Invoice) -> Invoice:
        self.db.commit()
        self.db.refresh(invoice)
        return invoice

    def create_credit_note(self, credit_note: CreditNote) -> CreditNote:
        self.db.add(credit_note)
        self.db.commit()
        self.db.refresh(credit_note)
        return credit_note
