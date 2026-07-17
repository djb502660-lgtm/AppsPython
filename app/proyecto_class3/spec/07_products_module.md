# SPEC 07: Módulo de Productos y Categorías

## 1. Objetivo
Gestionar el catálogo de productos disponibles para la venta, agrupándolos por categorías e integrando atributos como precios, control de stock básico e imágenes.

## 2. Casos de Uso
- **Gestión de Categorías:** (Admin) Crear, editar, listar y desactivar categorías. Las categorías desactivadas no se muestran al cliente.
- **Gestión de Productos:** (Admin) Crear, editar, listar, desactivar productos. Asignar precio, stock inicial y categoría.
- **Catálogo Público:** (Cliente / Público) Listar productos activos organizados por categorías activas. Buscar productos por nombre.
- **Visualización de Producto:** (Cliente / Público) Ver el detalle de un producto específico, incluyendo su stock actual.

## 3. Endpoints (Router: `/api/v1/products` y `/api/v1/categories`)

### Categorías
- `GET /api/v1/categories` -> (Público) Listar todas las categorías activas.
- `GET /api/v1/categories/all` -> (Protegido - Admin) Listar todas las categorías (incluso inactivas).
- `POST /api/v1/categories` -> (Protegido - Admin) Crear categoría.
- `PUT /api/v1/categories/{id}` -> (Protegido - Admin) Modificar categoría.

### Productos
- `GET /api/v1/products` -> (Público) Listar productos activos (Acepta filtros por `category_id`, `search`).
- `GET /api/v1/products/all` -> (Protegido - Admin) Listar todos los productos.
- `GET /api/v1/products/{id}` -> (Público) Ver producto.
- `POST /api/v1/products` -> (Protegido - Admin) Crear producto.
- `PUT /api/v1/products/{id}` -> (Protegido - Admin) Actualizar producto (incluye soft delete con `is_active`).

## 4. Reglas de Negocio
- **Soft Delete:** No se eliminan productos ni categorías de la BD. Solo se cambia `is_active` a `false` para mantener el historial de ventas y auditoría.
- **Stock:** No se puede comprar un producto con stock 0. (Validación a realizar en Módulo de Pedidos, pero el catálogo debe reportar el stock real).
- **Categorías Inactivas:** Si una categoría pasa a inactiva, sus productos asociados no deben aparecer en el catálogo público, incluso si los productos individuales siguen activos.

## 5. DTOs Principales (Pydantic)
```python
class CategoryCreateRequest(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    description: Optional[str] = None
    is_active: bool = True

class ProductCreateRequest(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    description: Optional[str] = None
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    category_id: int
    is_active: bool = True
```
