# SKILL: Access Control Review

## Objetivo
Auditar sistemáticamente los endpoints de la API (Backend) y los componentes de la interfaz de usuario (Frontend) para garantizar que los permisos RBAC se apliquen correctamente.

## Entradas
- Código fuente de los Controllers/Routers de FastAPI.
- Vistas del Frontend que exponen funcionalidades.
- Matriz de permisos de `spec/04_roles_permissions.md`.

## Reglas
1. Todo endpoint, excepto los públicos explícitos (ej. `/login`, `/register`, catálogo público), debe estar protegido.
2. La inyección de dependencias de seguridad debe comprobar tanto la autenticación (Token Válido) como la autorización (Permiso Válido).
3. El frontend no debe mostrar botones o enlaces de acciones a las que el usuario no tiene acceso.

## Checklist
- [ ] ¿El endpoint `POST /productos` verifica el permiso `products:CREATE`?
- [ ] ¿El endpoint `PUT /pedidos/estado` verifica el permiso correspondiente (ej. `orders:UPDATE_STATUS`)?
- [ ] ¿La lógica previene IDOR validando la propiedad de los recursos en los permisos `_OWN`?

## Validaciones
- **Automática:** Pruebas unitarias de seguridad (Testing 401 y 403 con distintos perfiles falsos).
- **Manual:** Revisión de código (Code Review) en el PR de implementación.

## Resultado Esperado
Evidencia en forma de tests unitarios que pasan correctamente validando accesos positivos y negativos (Security Testing Report).
