# SKILL: Password Policy Validation

## Objetivo
Garantizar que todas las contraseñas creadas o actualizadas en el sistema cumplan con criterios de seguridad robustos antes de ser hasheadas y almacenadas.

## Entradas
- Código fuente de los validadores Pydantic del módulo de usuarios (`UserRegisterRequest`, `PasswordResetRequest`).
- Pruebas unitarias asociadas a la creación de usuarios.

## Reglas
1. La contraseña debe tener una longitud mínima de 8 caracteres.
2. La contraseña debe contener al menos una letra mayúscula.
3. La contraseña debe contener al menos un número.
4. La contraseña debe contener al menos un carácter especial (ej. `@$!%*?&`).
5. Las contraseñas en texto plano nunca deben registrarse en los logs de la aplicación.

## Checklist
- [ ] ¿El esquema Pydantic usa una expresión regular para validar el formato de la contraseña? (Ej. `^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$`)
- [ ] ¿Se captura el error de validación y se retorna un mensaje genérico pero útil ("La contraseña no cumple con los requisitos de seguridad") sin exponer el regex internamente?
- [ ] ¿Los tests unitarios prueban contraseñas cortas, sin números y sin caracteres especiales esperando un código 422 Unprocessable Entity?

## Validaciones
- **Automática:** Test unitarios sobre los modelos Pydantic `UserRegisterRequest` y los endpoints.
- **Manual:** Revisión del código (Code Review) para verificar que el log de auditoría omite la impresión del payload completo que incluya `password`.

## Resultado Esperado
Evidencia mediante tests (ej. `test_password_validation_fails_on_weak_password`) y una revisión de código limpia.
