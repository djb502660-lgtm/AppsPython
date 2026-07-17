// app.js - Lógica principal del Frontend Cliente

document.addEventListener('DOMContentLoaded', () => {
    // Inicializar UI
    initNavbarScroll();
    
    // Mock de carga de productos si la API no está encendida
    // En producción se usaría: APIClient.get('/products').then(renderProducts);
    console.log("App Inicializada - Experiencia Rappi Style");
});

function initNavbarScroll() {
    const navbar = document.querySelector('.custom-navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(15, 17, 21, 0.95)';
            navbar.style.boxShadow = '0 10px 30px rgba(0,0,0,0.5)';
        } else {
            navbar.style.background = 'rgba(15, 17, 21, 0.8)';
            navbar.style.boxShadow = 'none';
        }
    });
}

// Lógica de Carrito Básica (Mock)
let cart = [];
function updateCartCount() {
    document.getElementById('cart-count').innerText = cart.length;
}

document.querySelectorAll('.btn-add-cart').forEach(btn => {
    btn.addEventListener('click', (e) => {
        // Animación de pulso
        const icon = e.currentTarget.querySelector('i');
        icon.classList.remove('fa-plus');
        icon.classList.add('fa-check');
        setTimeout(() => {
            icon.classList.remove('fa-check');
            icon.classList.add('fa-plus');
        }, 1000);
        
        cart.push({ id: Date.now() });
        updateCartCount();
    });
});
