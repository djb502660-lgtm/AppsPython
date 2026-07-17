# SPEC 00: Project Vision

## 1. Objetivos
Desarrollar una plataforma de gestión y venta de comida rápida que sea robusta, escalable y segura, operando bajo un modelo Cliente-Servidor. El objetivo principal es proveer una experiencia fluida para clientes, y un panel de control completo para la administración, cocina y repartidores.

## 2. Alcance
El sistema funcionará como:
- Aplicación Web (Frontend moderno tipo Rappi)
- Aplicación Android (Futura integración vía WebView o API REST)
- Aplicación de Escritorio (Futura integración mediante Electron)

Contempla la gestión completa del flujo: desde el registro del cliente, navegación del catálogo, carrito de compras, hasta la confirmación, pago (transferencias bancarias validadas manualmente) y seguimiento del pedido.

## 3. Restricciones
- El backend será exclusivamente en Python usando FastAPI.
- La base de datos será MySQL operada mediante SQLAlchemy y migraciones de Alembic.
- La interfaz web utilizará HTML5, CSS3, JS ES6 y Bootstrap 5 puro, sin frameworks JS reactivos adicionales.
- Se debe asegurar un 80% mínimo de cobertura en testing.
- El despliegue inicial se enfocará en un entorno XAMPP (servidor de BD).

## 4. Arquitectura General
El proyecto se dividirá en módulos independientes bajo una arquitectura **Cliente-Servidor**. 
- **Servidor:** API REST en FastAPI que orquestará la lógica de negocio, acceso a datos y seguridad.
- **Cliente Web:** Frontend en HTML/JS que consumirá los endpoints del backend utilizando JWT para autenticación.

## 5. Casos de Uso Principales
- **Cliente:** Se registra, explora productos, agrega al carrito, paga mediante transferencia, sube comprobante, espera validación, visualiza el estado y descarga su ticket.
- **Administrador:** Valida transferencias, gestiona inventario, crea productos, asigna roles, revisa reportes.
- **Inventario/Cocina/Repartidor:** Visualizan los pedidos en sus respectivos estados (Pendiente, Preparación, Listo, Entregado) e interactúan para avanzar el flujo.

## 6. Requisitos Funcionales
- **RF01:** El sistema debe permitir registro y autenticación con JWT.
- **RF02:** El sistema debe incluir un RBAC granular.
- **RF03:** El carrito de compras debe reservar stock temporalmente.
- **RF04:** Debe existir validación manual de comprobantes de pago (JPG, PNG, PDF) con límites de tamaño y auditoría de seguridad.
- **RF05:** Los pedidos deben pasar por estados estrictos: Pendiente -> Validación -> Aprobado -> Preparación -> Listo -> Entregado.
- **RF06:** Todos los eventos críticos deben registrarse en una bitácora de auditoría (IP, Usuario, Acción, Navegador).

## 7. Requisitos No Funcionales
- **RNF01:** Seguridad: Cumplimiento de OWASP TOP 10.
- **RNF02:** Diseño UX: Experiencia comercial tipo Rappi, "Mobile First".
- **RNF03:** Rendimiento: Tiempos de respuesta de API < 200ms en condiciones normales.
- **RNF04:** Testing: Cobertura del 80% mínimo en pruebas unitarias e integración.
