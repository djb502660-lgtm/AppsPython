# SPEC 03: Security

## 1. Aplicación de OWASP TOP 10
El sistema estará diseñado tomando en cuenta los principales riesgos de seguridad definidos en el OWASP TOP 10, aplicando las siguientes medidas de mitigación:

### 1.1. Inyección (SQL Injection)
- **Mitigación:** Uso exclusivo del ORM (SQLAlchemy) para todas las consultas. Prohibición de concatenación de strings para construir queries.

### 1.2. Cross-Site Scripting (XSS)
- **Mitigación:** El backend validará (con Pydantic) y sanitizará todas las entradas. El frontend escapará la salida de variables (las plantillas, incluso puras en HTML/JS, deberán usar `textContent` en lugar de `innerHTML` o escapar los datos previamente).

### 1.3. Cross-Site Request Forgery (CSRF)
- **Mitigación:** Uso de autenticación basada en JWT enviados en los headers de autorización (`Authorization: Bearer <token>`) en lugar de cookies de sesión tradicionales para las peticiones de API.

### 1.4. Server-Side Request Forgery (SSRF)
- **Mitigación:** Deshabilitación y validación estricta de cualquier parámetro que intente buscar recursos externos. Si el sistema debe descargar algo (ej. validación de recibos remotos), sólo permitirá dominios de lista blanca.

### 1.5. Insecure Direct Object References (IDOR)
- **Mitigación:** Todos los endpoints que acceden a recursos por ID validarán obligatoriamente que el recurso pertenece al usuario que realiza la petición o que el usuario tiene permisos de lectura global (ej. Administrador).

### 1.6. Broken Access Control
- **Mitigación:** Implementación del modelo RBAC (Role-Based Access Control). Cada endpoint requerirá la inyección de una dependencia que verifique el rol y permiso adecuado.

### 1.7. JWT Hijacking & Session Fixation
- **Mitigación:** Los JWT tendrán un tiempo de vida (TTL) corto (ej. 15-30 minutos) e implementaremos Refresh Tokens rotatorios almacenados en HTTP-Only Cookies (si se desea en el frontend web) o manejo local seguro con revocación (blacklisting) en el servidor de base de datos o Redis.

### 1.8. Credential Stuffing
- **Mitigación:** Implementar "Rate Limiting" (ej. mediante FastAPI-Limiter) en el endpoint de `/login` para bloquear intentos de fuerza bruta, y bloqueo temporal de cuenta tras múltiples intentos fallidos.

### 1.9. Path Traversal & File Upload Attacks
- **Mitigación:** 
    - Las transferencias/comprobantes se guardarán en un bucket de almacenamiento o carpeta aislada sin permisos de ejecución.
    - Se usarán nombres de archivo aleatorios (UUID) generados en backend, descartando el nombre original del cliente.
    - Se validará el MIME type real del archivo (no solo la extensión) verificando la firma (Magic numbers). Solo se permitirán imágenes (JPG, PNG) y PDF.
    - Límite estricto de tamaño de archivo (ej. 5MB).
