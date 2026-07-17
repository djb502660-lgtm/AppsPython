# SPEC 12: Frontend Web - Administrador (Dashboard)

## 1. Objetivo
Proveer un panel de control (Dashboard) seguro, rápido y claro para que el personal interno (Administradores, Cajeros, Cocina, Repartidores) gestione la operatividad de la plataforma.

## 2. Pila Tecnológica
- **HTML5, CSS3, Bootstrap 5** (Diseño basado en el patrón "Sidebar layout").
- **Vanilla JavaScript (ES6+)**
- **Chart.js** (Para las gráficas del dashboard).

## 3. Guía de Diseño
- **Limpieza visual:** A diferencia del lado del cliente, el admin panel prioriza la densidad de información y la claridad.
- **Colores:** Uso de un tema "Sleek Dark Mode" por defecto o un tema claro con contrastes fuertes en gris/azul corporativo.
- **Data Tables:** Tablas responsivas para manejar grandes listados (Usuarios, Órdenes, Kardex).

## 4. Vistas Principales (Rutas Protegidas)
1. `admin/index.html`: Dashboard principal con KPIs (Ventas, Pedidos del día, Productos más vendidos).
2. `admin/orders.html`: Vista tipo Kanban o Tabla en tiempo real para gestionar el flujo de pedidos (Aprobar pagos, Mover a Cocina, etc.).
3. `admin/inventory.html`: Visualización del Kardex y botones para registrar mermas o ajustes manuales.
4. `admin/products.html`: CRUD de catálogo de productos.
5. `admin/users.html`: Asignación de Roles y gestión de empleados.

## 5. Arquitectura de Seguridad JS
- En cada carga de página en la ruta `/admin/`, un script en el `<head>` debe verificar la existencia del JWT y consultar el endpoint `/api/v1/users/me` para corroborar que el usuario tiene un `role_id` con acceso al panel. Si falla, redirige a `login.html`.
