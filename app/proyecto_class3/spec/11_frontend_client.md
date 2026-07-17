# SPEC 11: Frontend Web - Cliente (Experiencia Comercial)

## 1. Objetivo
Desarrollar una interfaz de usuario pública enfocada en la conversión, con un diseño "Mobile First", estético y dinámico, inspirado en la experiencia de aplicaciones comerciales como Rappi.

## 2. Pila Tecnológica Estricta
- **HTML5** (Semántico)
- **CSS3** (Variables nativas, Flexbox/Grid, Animaciones CSS)
- **Bootstrap 5** (Para el sistema de grillas y componentes base)
- **Vanilla JavaScript (ES6+)** (Consumo de API con Fetch, sin frameworks reactivos)

## 3. Guía de Diseño (UI/UX)
- **Paleta de Colores:** Uso de colores vibrantes sobre fondos neutros (ej. Naranja neón/Rojo vibrante para Call-To-Actions principales).
- **Tipografía:** Moderna y limpia (ej. `Inter` o `Outfit` importadas de Google Fonts).
- **Glassmorphism:** Uso sutil de fondos translúcidos y desenfoques (`backdrop-filter`) para las barras de navegación fijas o el modal del carrito.
- **Micro-interacciones:** Hover states suaves (transformaciones `scale` en las tarjetas de producto), transiciones en botones.

## 4. Vistas Principales
1. `index.html`: Página de inicio con:
   - **Hero Section:** Banner promocional con diseño atractivo y botón a la acción (CTA).
   - **Categorías Destacadas:** Carrusel horizontal tipo scroll en móviles (scroll-snap).
   - **Productos Populares:** Grid de productos usando tarjetas (cards) con imagen, precio, descripción corta y botón "Agregar".
2. `login.html` / `register.html`: Formularios limpios, validación en tiempo real.
3. `cart.html` (o un Offcanvas global): Resumen de orden, manipulación de cantidades y botón de checkout.
4. `profile.html`: Panel para clientes donde pueden subir su comprobante de transferencia y ver el estado de su pedido (`PENDING` -> `DELIVERED`).

## 5. Arquitectura JS (Vanilla)
- `js/api.js`: Wrapper centralizado para las peticiones HTTP (`fetch`). Se encarga de inyectar el `Authorization: Bearer <token>` de `localStorage`.
- `js/auth.js`: Lógica de inicio de sesión y registro.
- `js/cart.js`: Gestión del estado del carrito en `localStorage` y renderizado de la UI del Offcanvas.
- `js/app.js`: Lógica de renderizado dinámico de productos en el `index.html`.
