(function () {
    'use strict';

    var navToggle = document.getElementById('nav-toggle');
    var nav = document.getElementById('nav-principal');

    if (navToggle && nav) {
        navToggle.addEventListener('click', function () {
            var abierta = nav.classList.toggle('abierto');
            navToggle.setAttribute('aria-expanded', abierta ? 'true' : 'false');
            navToggle.setAttribute('aria-label', abierta ? 'Cerrar menú de navegación' : 'Abrir menú de navegación');
        });
    }

    var btnPassword = document.getElementById('btn-password');
    var campoPassword = document.getElementById('id_password');

    if (btnPassword && campoPassword) {
        btnPassword.addEventListener('click', function () {
            var oculta = campoPassword.type === 'password';
            campoPassword.type = oculta ? 'text' : 'password';
            btnPassword.textContent = oculta ? 'Ocultar' : 'Mostrar';
            btnPassword.setAttribute('aria-pressed', oculta ? 'true' : 'false');
            btnPassword.setAttribute('aria-label', oculta ? 'Ocultar contraseña' : 'Mostrar contraseña');
        });
    }

    var enlacesSeccion = document.querySelectorAll('.nav-link[href*="#"]');

    enlacesSeccion.forEach(function (enlace) {
        enlace.addEventListener('click', function () {
            if (nav && nav.classList.contains('abierto')) {
                nav.classList.remove('abierto');
                if (navToggle) {
                    navToggle.setAttribute('aria-expanded', 'false');
                }
            }
        });
    });
})();
