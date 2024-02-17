function login(username, password) {
  return fetch("../../api/data.json")
    .then((response) => response.json())
    .then((data) => {
      const usuarios = data.users;
      const usuarioAutenticado = usuarios.find(
        (user) => user.username === username && user.password === password
      );
      
      if (usuarioAutenticado) {
        return { usuario: usuarioAutenticado, rol: usuarioAutenticado.role };
      } else {
        throw new Error("Credenciales incorrectas. Por favor, inténtalo de nuevo.");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      throw error;
    });
}

document.getElementById("loginForm").addEventListener("submit", function (event) {
  event.preventDefault();

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  login(username, password)
    .then(({ usuario, rol }) => {
      alert("Inicio de sesión exitoso");

      // Guardar datos de sesión en sessionStorage
      sessionStorage.setItem("usuario", JSON.stringify(usuario));
      sessionStorage.setItem("rol", rol);

      // Redirigir según el rol del usuario
      switch (rol) {
        case "admin":
          window.location.href = "../../dashboard/admin";
          break;
        case "provider":
          window.location.href = "../../dashboard/provider";
          break;
        case "client":
          window.location.href = "../../dashboard/client";
          break;
        default:
          console.error("Rol no reconocido");
      }
    })
    .catch((error) => {
      alert(error.message);
    });
});

function cerrarSesion() {
  // Eliminar datos de sesión de sessionStorage
  sessionStorage.removeItem("usuario");
  sessionStorage.removeItem("rol");

  // Redirigir a la página de inicio de sesión
  window.location.href = "/login";
}

document.getElementById("cerrarSesionBtn").addEventListener("click", cerrarSesion);
