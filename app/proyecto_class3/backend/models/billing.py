from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from core.database import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'), unique=True, nullable=False)
    invoice_number = Column(String(50), unique=True, nullable=False)
    billing_address = Column(String(255), nullable=True)
    tax_id = Column(String(50), nullable=True)
    total_amount = Column(Float, nullable=False)
    tax_amount = Column(Float, nullable=False)
    status = Column(String(20), nullable=False, default="ISSUED") # ISSUED, CANCELLED
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    order = relationship("Order")
    credit_notes = relationship("CreditNote", back_populates="invoice")

class CreditNote(Base):
    __tablename__ = "credit_notes"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey('invoices.id'), nullable=False)
    credit_note_number = Column(String(50), unique=True, nullable=False)
    amount = Column(Float, nullable=False)
    reason = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    invoice = relationship("Invoice", back_populates="credit_notes")
