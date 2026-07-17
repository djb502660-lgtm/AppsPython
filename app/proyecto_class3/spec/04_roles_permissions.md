# SPEC 04: Roles and Permissions

## 1. Diseño RBAC (Role-Based Access Control)
El sistema utiliza un control de acceso granular. Un **Usuario** tiene un **Rol**. Un **Rol** tiene múltiples **Permisos**.

## 2. Roles Iniciales
- **Super Admin:** Acceso irrestricto a todo el sistema.
- **Administrador:** Gestión general del sistema (Módulos de usuarios, configuraciones, reportes).
- **Cajero:** Facturación, gestión de tickets, ventas presenciales o cobro.
- **Inventario:** Control de almacén, entradas, salidas, kardex.
- **Cocina:** Visualización y actualización de pedidos en los estados (Pendiente -> Preparación -> Listo).
- **Repartidor:** Visualización y actualización de pedidos en estado de entrega (Listo -> Entregado).
- **Cliente:** Acceso únicamente a sus propios datos, catálogo público, pedidos propios, perfil.
- **Auditor:** Acceso de solo lectura a todos los módulos y logs del sistema.

## 3. Matriz de Permisos
Cada permiso se forma combinando un **Módulo** y una **Acción**.
### Acciones Base Soportadas:
- `CREATE`, `READ`, `UPDATE`, `DELETE`, `EXPORT`, `IMPORT`, `APPROVE`, `REJECT`, `PRINT`

### Ejemplos de Permisos por Rol:

#### Cliente:
- `orders:CREATE` (Crear su pedido)
- `orders:READ_OWN` (Ver sus pedidos)
- `profile:UPDATE` (Actualizar su perfil)

#### Administrador:
- `products:CREATE`, `products:UPDATE`, `products:DELETE`
- `orders:READ`, `orders:APPROVE`, `orders:REJECT` (Para validar comprobantes de transferencia)

#### Cocina:
- `orders:READ`
- `orders:UPDATE_STATUS` (Mover a preparación/listo)

## 4. Implementación
Los permisos se cargarán dinámicamente mediante middlewares o dependencias de inyección (`Depends`) en FastAPI. Si un usuario intenta acceder a un endpoint para el cual su rol no tiene asignado el permiso, el sistema responderá con `403 Forbidden`.
