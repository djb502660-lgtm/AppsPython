# SISTEMA MULTIPLATAFORMA DE GESTIÓN Y VENTA DE COMIDA RÁPIDA

Actúa como un equipo senior compuesto por:

* Software Architect
* Backend Architect
* Frontend Architect
* UX/UI Designer
* Cybersecurity Engineer
* DevOps Engineer
* Database Administrator
* QA Engineer
* Technical Writer

Debes aplicar rigurosamente la metodología:

# SPEC AS SKILL

Basada en:

* Spec Driven Development
* Spec as Source
* Spec as Driver

Antes de generar código debes generar documentación, análisis, validaciones, planes de ejecución y habilidades reutilizables.

NO PUEDES CODIFICAR NINGÚN MÓDULO HASTA QUE SU SPEC HAYA SIDO APROBADA.

---

# OBJETIVO GENERAL

Desarrollar una plataforma de gestión y venta de comida rápida que funcione como:

* Aplicación Web
* Aplicación Android
* Aplicación de Escritorio

utilizando arquitectura Cliente – Servidor.

---

# STACK TECNOLÓGICO

## Backend

* Python
* FastAPI
* SQLAlchemy
* MySQL
* XAMPP
* JWT
* Alembic
* Pydantic

## Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript ES6

## Aplicaciones Futuras

* Android mediante WebView o API REST
* Desktop mediante Electron

---

# ESTRUCTURA RAÍZ DEL PROYECTO

/proyecto

/backend

/frontend

/spec

/skills

/docs

/tests

/deployment

---

# FASE 1 - GENERACIÓN DE SPECS

Generar dentro de /spec

## 00_project_vision

Contendrá:

* Objetivos
* Alcance
* Restricciones
* Arquitectura General
* Casos de Uso
* Requisitos Funcionales
* Requisitos No Funcionales

---

## 01_architecture

Documentar:

* Arquitectura Cliente Servidor
* Arquitectura Modular
* Arquitectura Hexagonal
* Arquitectura por Capas

Definir:

* Controllers
* Services
* Repositories
* DTOs
* Entities

---

## 02_database

Generar:

### DER

### Modelo Relacional

### Diccionario de Datos

### Scripts SQL

### Índices

### Foreign Keys

### Triggers

### Vistas

### Auditoría

---

## 03_security

Aplicar OWASP TOP 10

Documentar mitigaciones para:

* SQL Injection
* XSS
* CSRF
* SSRF
* IDOR
* Broken Access Control
* JWT Hijacking
* Session Fixation
* Credential Stuffing
* Path Traversal
* File Upload Attacks

---

## 04_roles_permissions

Diseñar RBAC granular.

Roles iniciales:

* Super Admin
* Administrador
* Cajero
* Inventario
* Cocina
* Repartidor
* Cliente
* Auditor

Cada módulo debe soportar:

CREATE
READ
UPDATE
DELETE
EXPORT
IMPORT
APPROVE
REJECT
PRINT

---

# FASE 2 - MÓDULOS FUNCIONALES

Crear una SPEC individual para cada módulo.

---

## Módulo Usuarios

Funcionalidades:

* Registro
* Login
* Recuperar contraseña
* Cambio de contraseña
* Perfil
* Avatar
* Historial

---

## Módulo Roles

* CRUD Roles
* CRUD Permisos
* Asignación dinámica

---

## Módulo Productos

* CRUD Productos
* Categorías
* Imágenes
* Precios
* Promociones
* Estado

---

## Módulo Inventario

* Entradas
* Salidas
* Kardex
* Ajustes

---

## Módulo Compras

* Órdenes de compra
* Recepciones
* Historial

---

## Módulo Carrito

* Agregar producto
* Editar cantidades
* Eliminar
* Reservar stock

---

## Módulo Pedidos

Estados:

* Pendiente
* Validación
* Aprobado
* Preparación
* Listo
* Entregado
* Rechazado

---

## Módulo Facturación

* Facturas
* Notas de crédito
* Historial

---

## Módulo Tickets

* Generación PDF
* Impresión
* Descarga

---

## Módulo Transferencias

Permitir:

* JPG
* PNG
* PDF

Validaciones:

* Tamaño máximo
* Antivirus
* Hash
* OCR opcional

---

## Módulo Validación Manual

Administrador valida:

* Recibo
* Monto
* Referencia

y aprueba o rechaza.

---

## Módulo Notificaciones

* Correo
* Sistema
* Push

---

## Módulo Reportes

* Ventas
* Productos
* Inventario
* Clientes
* Auditoría

---

## Módulo Dashboard

Indicadores:

* Ventas
* Pedidos
* Inventario
* Clientes
* Productos más vendidos

---

# EXPERIENCIA COMERCIAL

La página principal debe inspirarse en la experiencia comercial de Rappi.

NO copiar código.

Diseñar:

* Hero principal
* Categorías destacadas
* Productos populares
* Productos más vendidos
* Promociones
* Combos
* Recomendaciones

UX moderna.

Responsive.

Mobile First.

---

# FLUJO DEL CLIENTE

1. Registro
2. Login
3. Explorar productos
4. Carrito
5. Confirmar pedido
6. Transferencia bancaria
7. Subir comprobante
8. Esperar validación
9. Pedido aprobado
10. Descargar ticket
11. Retirar producto

---

# FUNCIONALIDADES DEL PERFIL CLIENTE

* Perfil
* Dirección
* Historial
* Pedidos
* Compras
* Favoritos
* Carrito
* Tickets
* Facturas
* Notificaciones
* Estado de pedidos

---

# AUDITORÍA

Registrar:

* Usuario
* Acción
* Fecha
* IP
* Navegador

Bitácora completa.

---

# SEEDERS

Generar:

* Roles
* Permisos
* Usuario administrador
* Categorías
* Productos demo

---

# TESTING

Generar:

* Unit Testing
* Integration Testing
* Security Testing
* Performance Testing

Cobertura mínima:

80%

---

# FASE 3 - SKILLS

Crear carpeta /skills

Cada SPEC debe generar habilidades reutilizables.

Ejemplo:

skills/

security/

ui_review/

database_review/

code_review/

unit_testing/

integration_testing/

access_control/

api_validation/

audit_validation/

performance_validation/

documentation_validation/

Cada skill debe incluir:

* Objetivo
* Entradas
* Reglas
* Checklist
* Validaciones
* Resultado esperado

---

# REGLAS OBLIGATORIAS

Antes de crear código:

1. Crear SPEC.
2. Validar SPEC.
3. Solicitar aprobación.
4. Crear Skill.
5. Ejecutar Skill.
6. Generar código.

Nunca omitir pasos.

Todo módulo debe incluir:

* Spec
* Skill
* Código
* Test
* Auditoría
* Seguridad
* Documentación

Generar la estructura completa del proyecto lista para desarrollo empresarial.
