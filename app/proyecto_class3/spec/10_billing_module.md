# SPEC 10: Módulo de Facturación y Tickets

## 1. Objetivo
Permitir la generación de facturas (comprobantes fiscales) y tickets (recibos) asociados a los pedidos que hayan sido entregados o pagados.

## 2. Casos de Uso
- **Generar Factura:** (Admin/Cajero) Emitir una factura formal para un pedido que se encuentra en estado `APPROVED` o superior. La factura toma los datos del usuario y los items del pedido.
- **Generar Ticket:** (Cliente/Admin/Cajero) Descargar o imprimir un ticket simple de la compra.
- **Notas de Crédito:** (Admin) Anular una factura emitida en caso de devoluciones y generar un comprobante negativo (Nota de Crédito).
- **Listar Facturas:** (Admin) Ver el historial de facturación para cuadre de caja.

## 3. Endpoints (Router: `/api/v1/billing`)

- `POST /api/v1/billing/invoices/order/{order_id}` -> (Cajero) Genera factura a partir de una orden.
- `GET /api/v1/billing/invoices` -> (Admin/Cajero) Lista facturas.
- `GET /api/v1/billing/invoices/{id}` -> (Cliente/Admin) Detalle de factura.
- `POST /api/v1/billing/credit-notes/invoice/{invoice_id}` -> (Admin) Anula la factura creando una nota de crédito.

## 4. Reglas de Negocio
- **Relación 1 a 1:** Un pedido (Order) solo puede tener UNA Factura activa.
- **Inmutabilidad Fiscal:** Una factura generada no puede ser eliminada. Si hay un error, se debe generar una Nota de Crédito para anular contablemente la factura y luego, si es necesario, generar otra.
- **Numeración Secuencial:** Las facturas deben llevar un correlativo (ej. `F001-0000123`).

## 5. DTOs Principales (Pydantic)
```python
class InvoiceCreateRequest(BaseModel):
    # En un caso real incluiría datos fiscales como RFC/RUC del cliente si difieren del perfil
    billing_address: Optional[str] = None
    tax_id: Optional[str] = None

class InvoiceResponse(BaseModel):
    id: int
    order_id: int
    invoice_number: str
    total_amount: float
    tax_amount: float
    status: str # ISSUED, CANCELLED
    created_at: datetime

class CreditNoteResponse(BaseModel):
    id: int
    invoice_id: int
    credit_note_number: str
    amount: float
    created_at: datetime
```
