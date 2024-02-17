//necesita sus mejoras.
function verificarAutenticacionYRol() {
    const usuario = JSON.parse(localStorage.getItem("usuario"));
    const rol = sessionStorage.getItem("rol");
    //const rol = localStorage.getItem("rol");
  
    if (!usuario || !rol) {
      window.location.href = "../../";
      return false;
    }
    switch (window.location.pathname) {
      case "/provider":
        if (rol !== "provider") {
          window.location.href = "/";
          return false;
        }
        break;
    }
    return true;
  }
  document.addEventListener("DOMContentLoaded", function () {
    verificarAutenticacionYRol();
  });
  