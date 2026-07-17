# SPEC 02: Database

## 1. Consideraciones Generales
La base de datos será **MySQL** administrada localmente mediante **XAMPP**.
La gestión de esquemas se realizará a través de migraciones de **Alembic** y el ORM **SQLAlchemy**.

## 2. Diagrama Entidad-Relación (DER) / Relacional
```mermaid
erDiagram
    USERS {
        int id PK
        string email UK
        string password_hash
        string first_name
        string last_name
        int role_id FK
        boolean is_active
        datetime created_at
    }
    
    ROLES {
        int id PK
        string name UK
        string description
    }
    
    PERMISSIONS {
        int id PK
        string name UK
        string module
    }
    
    ROLE_PERMISSIONS {
        int role_id FK
        int permission_id FK
    }

    CATEGORIES {
        int id PK
        string name UK
        string description
        boolean is_active
    }

    PRODUCTS {
        int id PK
        string name
        string description
        decimal price
        int stock
        int category_id FK
        boolean is_active
    }

    ORDERS {
        int id PK
        int user_id FK
        decimal total
        string status
        string payment_proof_url
        datetime created_at
    }

    ORDER_ITEMS {
        int id PK
        int order_id FK
        int product_id FK
        int quantity
        decimal unit_price
    }

    AUDIT_LOGS {
        int id PK
        int user_id FK
        string action
        string entity_type
        int entity_id
        string ip_address
        string browser
        datetime created_at
    }

    USERS }|--|| ROLES : "has"
    ROLES ||--|{ ROLE_PERMISSIONS : "contains"
    PERMISSIONS ||--|{ ROLE_PERMISSIONS : "assigned_to"
    
    CATEGORIES ||--|{ PRODUCTS : "groups"
    
    USERS ||--|{ ORDERS : "places"
    ORDERS ||--|{ ORDER_ITEMS : "contains"
    PRODUCTS ||--|{ ORDER_ITEMS : "included_in"
    
    USERS ||--|{ AUDIT_LOGS : "generates"
```

## 3. Auditoría y Trazabilidad
Se implementará una tabla global `AUDIT_LOGS` que registrará todas las acciones de modificación (CREATE, UPDATE, DELETE) en tablas críticas, guardando la IP, el agente de usuario, el ID del usuario y el registro afectado.

## 4. Índices
Se crearán índices explícitos en:
- `users.email`
- `orders.user_id`
- `orders.status`
- `products.category_id`
- `audit_logs.created_at`
- `audit_logs.user_id`

## 5. Triggers
(Opcional, preferible manejar mediante lógica de la aplicación en el nivel de `Services` o eventos de SQLAlchemy, a menos que el rendimiento exija consistencia dura en el motor para evitar desajustes de inventario en Kardex).

## 6. Soporte Multi-Sucursal (Futuro)
El diseño contempla a futuro la adición de `branch_id` en `USERS`, `ORDERS` y un inventario separado para escalar a un modelo multi-sucursal o multitenant.
