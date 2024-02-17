//
function verificarAutenticacionYRol() {
  const usuario = JSON.parse(sessionStorage.getItem("usuario"));
  const rol = sessionStorage.getItem("rol");

  if (!usuario || !rol) {
    redirigirALogin("Debes iniciar sesión para acceder a esta página.");
    return false;
  }

  const rutasProtegidas = {
    "/admin": "admin",
  };

  const rutaActual = window.location.pathname;
  const rolRequerido = rutasProtegidas[rutaActual];

  if (rolRequerido && rol !== rolRequerido) {
    redirigirALogin("No tienes permisos para acceder a esta página.");
    return false;
  }

  return true;
}

function redirigirALogin(mensaje) {
  sessionStorage.removeItem("usuario");
  sessionStorage.removeItem("rol");
  alert(mensaje);
  window.location.href = "../../";
}

document.addEventListener("DOMContentLoaded", function () {
  verificarAutenticacionYRol();
});
