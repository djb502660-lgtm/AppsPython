# SPEC 08: Módulo de Pedidos

## 1. Objetivo
Gestionar el flujo comercial completo desde la creación del carrito hasta la entrega del producto final, pasando por la validación de pagos manual y la preparación en cocina.

## 2. Estados del Pedido (Máquina de Estados)
De acuerdo a la visión general, un pedido fluye así:
1. **PENDING:** El cliente creó el pedido (agregó al carrito y confirmó) pero aún no ha subido comprobante de transferencia.
2. **VALIDATING:** El cliente subió el comprobante (JPG/PDF). En espera de aprobación por Admin.
3. **APPROVED:** El Admin validó el pago. (Si se rechaza, pasa a `REJECTED`).
4. **PREPARING:** La cocina toma el pedido y comienza a prepararlo.
5. **READY:** La cocina terminó, listo para ser entregado o despachado.
6. **DELIVERED:** El repartidor o cajero entregó el pedido al cliente.
7. **REJECTED:** El pago no fue válido o el pedido fue cancelado.

## 3. Casos de Uso
- **Crear Pedido:** (Cliente) Convierte el contenido de su carrito en una Orden `PENDING`. Se reserva stock de los productos.
- **Subir Comprobante:** (Cliente) Sube una imagen/PDF al pedido `PENDING`, cambiándolo a `VALIDATING`.
- **Validar Pago:** (Admin) Visualiza comprobante y marca como `APPROVED` o `REJECTED`. Si se rechaza, el stock reservado debe ser devuelto (Kardex inverso).
- **Gestión Cocina:** (Cocina) Lista pedidos `APPROVED`, los toma (`PREPARING`) y los finaliza (`READY`).
- **Gestión Entrega:** (Repartidor/Cajero) Marca pedidos `READY` como `DELIVERED`.
- **Historial:** (Cliente) Ve sus pedidos. (Auditor/Admin) Ve todos los pedidos del sistema.

## 4. Endpoints (Router: `/api/v1/orders`)

- `POST /api/v1/orders` -> (Cliente) Crea un pedido con sus items.
- `GET /api/v1/orders/me` -> (Cliente) Lista pedidos propios.
- `GET /api/v1/orders` -> (Protegido) Lista pedidos según el rol (Cocina solo ve Aprobados/Preparando, Admin ve todos).
- `GET /api/v1/orders/{id}` -> (Protegido/Cliente) Detalles del pedido.
- `PUT /api/v1/orders/{id}/status` -> (Protegido) Cambiar el estado según la máquina de estados.
- `POST /api/v1/orders/{id}/payment-proof` -> (Cliente) Subir archivo y pasar a `VALIDATING`.

## 5. DTOs Principales (Pydantic)
```python
class OrderItemRequest(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)

class OrderCreateRequest(BaseModel):
    items: List[OrderItemRequest]

class OrderStatusUpdateRequest(BaseModel):
    status: str # Enum: PENDING, VALIDATING, APPROVED, PREPARING, READY, DELIVERED, REJECTED
```
