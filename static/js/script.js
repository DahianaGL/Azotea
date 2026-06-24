/* =============================================
   AZOTEA — script.js
   Pegar TODO este contenido en: static/js/script.js
   ============================================= */

document.addEventListener('DOMContentLoaded', () => {

  /* ── 1. Navbar scroll ── */
  const nav = document.getElementById('azNav');
  if (nav) {
    window.addEventListener('scroll', () => {
      nav.classList.toggle('scrolled', window.scrollY > 60);
    }, { passive: true });
  }

  /* ── 2. Burger menú móvil ── */
  const burger = document.getElementById('azBurger');
  const navLinks = document.getElementById('azNavLinks');
  if (burger && navLinks) {
    burger.addEventListener('click', () => {
      burger.classList.toggle('open');
      navLinks.classList.toggle('open');
    });
    // Cerrar al hacer clic en un enlace
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        burger.classList.remove('open');
        navLinks.classList.remove('open');
      });
    });
  }

  /* ── 3. Marcar enlace activo en el nav ── */
  const currentPath = window.location.pathname;
  document.querySelectorAll('.az-nav__links a').forEach(link => {
    if (link.getAttribute('href') === currentPath) {
      link.closest('li')?.classList.add('active');
    }
  });

  /* ── 4. Contadores animados (Stats) ── */
  const counters = document.querySelectorAll('.az-stats__num');
  const animateCounter = (el) => {
    const target = parseInt(el.dataset.target, 10);
    const step = target / (1800 / 16);
    let current = 0;
    const update = () => {
      current += step;
      if (current < target) {
        el.textContent = Math.floor(current);
        requestAnimationFrame(update);
      } else {
        el.textContent = target;
      }
    };
    update();
  };
  if (counters.length) {
    const statsObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          counters.forEach(animateCounter);
          statsObserver.disconnect();
        }
      });
    }, { threshold: 0.4 });
    const statsSection = document.querySelector('.az-stats');
    if (statsSection) statsObserver.observe(statsSection);
  }

  /* ── 5. Reveal al hacer scroll ── */
  const revealEls = document.querySelectorAll(
    '.az-card, .az-testcard, .az-welcome__body, .az-welcome__image, .az-reservas__info, .az-reservas__form-wrap'
  );
  revealEls.forEach(el => el.classList.add('az-reveal'));
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('az-visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });
  revealEls.forEach(el => revealObserver.observe(el));

  /* ── 6. Feedback formulario reservas ── */
  const reservaForm = document.querySelector('.az-form');
  if (reservaForm) {
    reservaForm.addEventListener('submit', (e) => {
      const action = reservaForm.getAttribute('action');
      if (!action || action === '#') {
        e.preventDefault();
        const btn = reservaForm.querySelector('button[type="submit"]');
        const originalText = btn.textContent;
        btn.textContent = '✓ ¡Reserva enviada!';
        btn.style.background = '#4CAF50';
        btn.disabled = true;
        setTimeout(() => {
          btn.textContent = originalText;
          btn.style.background = '';
          btn.disabled = false;
          reservaForm.reset();
        }, 3000);
      }
    });
  }

  /* ── 7. Smooth scroll anclas internas ── */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  /* ── 12. Scroll automático al formulario si hay errores de validación ── */
  const formErrors = document.querySelectorAll('.az-form__group p[style*="color:red"]');
  if (formErrors.length > 0) {
    document.querySelector('#reservas').scrollIntoView({ behavior: 'smooth' });
  }

});

/* ── 8. Filtro por categoría en servicios ── */
const filtrosBtns = document.querySelectorAll('.az-filtro-btn');
if (filtrosBtns.length) {
    filtrosBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Marcar activo
            filtrosBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filtro = btn.dataset.filtro;
            const cards = document.querySelectorAll('.az-sv-card[data-categoria]');

            cards.forEach(card => {
                if (filtro === 'todos' || card.dataset.categoria === filtro) {
                    card.classList.remove('oculto');
                } else {
                    card.classList.add('oculto');
                }
            });
        });
    });
}

/* ── 9. Filtro categorías en tienda/menú ── */
const filtrosBtnsTienda = document.querySelectorAll('.az-filtro-btn');
if (filtrosBtnsTienda.length) {
    filtrosBtnsTienda.forEach(btn => {
        btn.addEventListener('click', () => {
            filtrosBtnsTienda.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filtro = btn.dataset.filtro;
            const cards = document.querySelectorAll('.az-menu-card[data-categoria]');
            let visibles = 0;

            cards.forEach(card => {
                if (filtro === 'todos' || card.dataset.categoria === filtro) {
                    card.classList.remove('oculto');
                    visibles++;
                } else {
                    card.classList.add('oculto');
                }
            });

            // Actualizar contador
            const contador = document.getElementById('menuCount');
            if (contador) {
                contador.textContent = visibles + ' plato' + (visibles !== 1 ? 's' : '') + ' en carta';
            }
        });
    });
}

/* ── 10. Confirmación formulario de contacto ── */
const contactoForm = document.querySelector('.az-contacto__form');
if (contactoForm) {
    contactoForm.addEventListener('submit', () => {
        setTimeout(() => {
            const confirmacion = document.getElementById('confirmacion');
            if (confirmacion) {
                contactoForm.style.display = 'none';
                confirmacion.style.display = 'block';
            }
        }, 300);
    });
}

/* ── 11. Filtro galería en blog ── */
const galeriaFiltros = document.querySelectorAll('.az-galeria-filtros .az-filtro-btn');
if (galeriaFiltros.length) {
    galeriaFiltros.forEach(btn => {
        btn.addEventListener('click', () => {
            galeriaFiltros.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filtro = btn.dataset.filtro;
            document.querySelectorAll('.az-galeria-item').forEach(item => {
                if (filtro === 'todos' || item.dataset.categoria === filtro) {
                    item.classList.remove('oculto');
                } else {
                    item.classList.add('oculto');
                }
            });
        });
    });
}