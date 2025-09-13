document.addEventListener('DOMContentLoaded', function() {
    const h1 = document.querySelector('h1');
    if (h1) {
        h1.textContent = 'Welcome to Django Homepage! (JS updated)';
        h1.style.backgroundColor = '#14f39dff';
    }
});