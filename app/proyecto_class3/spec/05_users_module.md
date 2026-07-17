# SPEC 05: Módulo de Usuarios

## 1. Objetivo
Gestionar el ciclo de vida de los usuarios (Clientes, Administradores, Empleados) dentro de la plataforma, asegurando autenticación robusta y manejo seguro de identidad.

## 2. Casos de Uso
- **Registro de Cliente:** Un usuario externo se registra proveyendo nombre, correo y contraseña. El sistema envía un OTP/Link al correo para confirmación.
- **Login:** Autenticación mediante email y contraseña, retornando un JWT.
- **Recuperación de Contraseña:** Flujo de "olvidé mi contraseña" que envía un token temporal al correo para restablecerla.
- **Cambio de Contraseña:** Un usuario autenticado cambia su contraseña actual por una nueva.
- **Perfil:** Visualizar y actualizar información personal (nombres, avatar).
- **Historial:** (Administradores) Ver log de actividad de los usuarios.

## 3. Endpoints (Router: `/api/v1/users` y `/api/v1/auth`)

### Públicos (Auth)
- `POST /api/v1/auth/register` (DTO: `UserRegisterRequest`) -> Retorna `201 Created` o `400 Bad Request`.
- `POST /api/v1/auth/login` (DTO: `UserLoginRequest`) -> Retorna `200 OK` con Token JWT.
- `POST /api/v1/auth/forgot-password` -> Envía correo de recuperación.
- `POST /api/v1/auth/reset-password` -> Valida token temporal y actualiza contraseña.

### Protegidos (Users)
- `GET /api/v1/users/me` -> Retorna perfil del usuario logueado (`UserResponse`).
- `PUT /api/v1/users/me` -> Actualiza perfil (`UserUpdateRequest`).
- `PUT /api/v1/users/me/password` -> Cambia contraseña, requiere validación de contraseña actual.
- `POST /api/v1/users/me/avatar` -> Sube imagen (Valida tipo y tamaño).

## 4. Validaciones de Seguridad
- **Contraseñas:** Política estricta (Mínimo 8 caracteres, 1 mayúscula, 1 número, 1 símbolo). Se almacenan hasheadas con bcrypt/argon2.
- **Rate Limiting:** `/login` bloqueado por IP tras 5 intentos fallidos (ventana de 15 minutos).
- **Aislamiento de Datos:** El endpoint `PUT /api/v1/users/me` ignorará cualquier intento de modificar campos como `role_id` o `is_active` (Prevención Mass Assignment mediante exclusión en el esquema Pydantic de Request).

## 5. DTOs Principales (Pydantic)
```python
class UserRegisterRequest(BaseModel):
    email: EmailStr
    password: str # Validado con Regex
    first_name: str = Field(min_length=2, max_length=50)
    last_name: str = Field(min_length=2, max_length=50)

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    role_id: int
    is_active: bool
```
