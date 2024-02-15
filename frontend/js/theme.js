const toggleModoBtn = document.getElementById('toggleModo');
const body = document.body;

const modoActual = localStorage.getItem('modo');
if (modoActual === 'oscuro') {
  body.classList.add('dark-mode');
}

toggleModoBtn.addEventListener('click', () => {
  if (body.classList.contains('dark-mode')) {
    body.classList.remove('dark-mode');
    localStorage.setItem('modo', 'claro');
  } else {
    body.classList.add('dark-mode');
    localStorage.setItem('modo', 'oscuro');
  }
});
