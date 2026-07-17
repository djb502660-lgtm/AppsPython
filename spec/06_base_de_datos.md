# Spec 06: Base de Datos - CRUD de Contactos

## Objetivo
Crear una API REST con FastAPI y SQLAlchemy para guardar contactos (nombre, teléfono, correo) en base de datos.

## Alcance
- **Entidad:** Contacto.
- **BD:** SQLite local.
- **Operaciones:** Crear, listar, obtener uno, actualizar, eliminar.
- **Ubicación:** `app/base_de_datos/`.
- **Prueba de conexión:** carpeta `prueba_conexion/`.

## Pasos
1. Configurar `database.py` y `requirements.txt`.
2. Crear modelo `models.py` y esquemas `schemas.py`.
3. Funciones CRUD en `crud.py`.
4. Endpoints en `main.py`.
5. Script de prueba en `prueba_conexion/index.py`.

## Riesgos
- Datos duplicados si no se valida el correo.
- **Mitigación:** Validar que nombre y correo no estén vacíos.
