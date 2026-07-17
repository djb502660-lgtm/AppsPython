# SPEC 09: Módulo de Inventario (Kardex)

## 1. Objetivo
Registrar y controlar todas las variaciones de stock (Entradas y Salidas) de los productos del sistema, generando un historial inmutable (Kardex) que permita auditorías, ajustes manuales y valorización del inventario.

## 2. Casos de Uso
- **Registrar Entrada:** (Inventario/Compras) Ingresar nueva mercancía al almacén (aumenta el stock del producto).
- **Registrar Salida:** (Automático por Ventas o manual por mermas/vencimientos) Disminuir el stock de un producto.
- **Ajuste de Inventario:** (Admin/Auditor) Forzar la sincronización del stock físico con el teórico mediante un asiento de ajuste positivo o negativo con su respectiva justificación.
- **Ver Kardex:** (Admin/Inventario) Visualizar el historial cronológico de movimientos de un producto específico, mostrando el stock anterior y el stock resultante tras cada movimiento.

## 3. Endpoints (Router: `/api/v1/inventory`)
*Nota: Todos requieren permisos de `inventory:MANAGE` o `inventory:READ` según la acción.*

- `POST /api/v1/inventory/movements` -> Crea un movimiento manual (Entrada/Salida/Ajuste). Actualiza el stock del producto asociado.
- `GET /api/v1/inventory/kardex/{product_id}` -> Obtiene el historial de movimientos de un producto.
- `GET /api/v1/inventory/movements` -> Obtiene todos los movimientos recientes del almacén (para reportes y filtros).

## 4. Reglas de Negocio
- **Inmutabilidad del Kardex:** Un registro de movimiento de inventario (`InventoryTransaction`) NUNCA debe ser eliminado ni modificado (No hay PUT ni DELETE). Si hay un error, se debe crear un movimiento compensatorio (Ajuste).
- **Tipos de Movimiento:** `IN` (Entrada), `OUT` (Salida), `ADJUSTMENT` (Ajuste).
- **Consistencia:** El stock actual del producto (`Product.stock`) debe ser siempre el resultado exacto de la suma algebraica de sus movimientos en el Kardex.

## 5. DTOs Principales (Pydantic)
```python
class InventoryMovementRequest(BaseModel):
    product_id: int
    transaction_type: str # IN, OUT, ADJUSTMENT
    quantity: int = Field(gt=0)
    reference: Optional[str] # Ej. "Factura #123", "Merma caducidad"
    notes: Optional[str]

class InventoryMovementResponse(BaseModel):
    id: int
    product_id: int
    transaction_type: str
    quantity: int
    previous_stock: int
    new_stock: int
    reference: Optional[str]
    created_at: datetime
    created_by: int
```
