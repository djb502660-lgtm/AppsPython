# SPEC 06: Módulo de Roles y Permisos

## 1. Objetivo
Administrar los roles del sistema y la asignación de permisos para controlar el acceso a los diferentes recursos de la aplicación mediante un esquema RBAC (Role-Based Access Control).

## 2. Casos de Uso
- **Listar Roles:** Un administrador visualiza la lista de roles existentes.
- **Crear Rol:** Un administrador crea un nuevo rol personalizado (ej. "Cajero Fin de Semana").
- **Actualizar Rol:** Modificar el nombre, descripción y los permisos asignados a un rol.
- **Eliminar Rol:** Eliminar un rol que ya no es utilizado (No se pueden eliminar roles primarios como Super Admin o Cliente, ni roles que tengan usuarios activos).
- **Listar Permisos:** Obtener el catálogo completo de permisos disponibles en el sistema (generados por el sistema/seeders).

## 3. Endpoints (Router: `/api/v1/roles`)
*Nota: Todos los endpoints de este router requieren que el usuario esté autenticado y tenga el permiso `roles:MANAGE` (o sea Super Admin).*

- `GET /api/v1/roles` -> Retorna la lista de roles (`RoleResponse[]`).
- `POST /api/v1/roles` -> Crea un nuevo rol (`RoleCreateRequest`).
- `GET /api/v1/roles/{role_id}` -> Detalles del rol y sus permisos (`RoleDetailResponse`).
- `PUT /api/v1/roles/{role_id}` -> Actualiza rol y sus permisos (`RoleUpdateRequest`).
- `DELETE /api/v1/roles/{role_id}` -> Elimina el rol (Soft delete o validación de integridad referencial).

- `GET /api/v1/permissions` -> Retorna la lista de todos los permisos (`PermissionResponse[]`).

## 4. Reglas de Negocio y Seguridad
- **Protección de Roles Base:** El ID 1 (Super Admin) y el ID 7 (Cliente, según Spec 04) no pueden ser modificados ni eliminados por los endpoints.
- **Integridad:** No se puede eliminar un rol si hay registros en la tabla `USERS` que apunten a ese `role_id`.
- **Asignación de Permisos:** Al actualizar un rol (`PUT`), se debe enviar la lista completa de `permission_ids` que tendrá el rol. El sistema reemplazará los permisos antiguos por los nuevos.

## 5. DTOs Principales (Pydantic)
```python
class RoleCreateRequest(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    description: Optional[str] = None
    permission_ids: List[int] = []

class RoleResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
```
