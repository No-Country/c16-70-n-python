function verificarAutenticacionYRol() {
    const usuario = JSON.parse(localStorage.getItem("usuario"));
    const rol = sessionStorage.getItem("rol");
  
    if (!usuario || !rol) {
      window.location.href = "../../";
      return false;
    }
    switch (window.location.pathname) {
      case "/client":
        if (rol !== "client") {
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
  