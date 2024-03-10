import { apiUrlServer } from "../js/config.js";
const register = (userData) => {
  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  const requestOptions = {
    method: "POST",
    headers: myHeaders,
    body: JSON.stringify(userData),
    redirect: "follow",
  };

  fetch("https://c1670python.pythonanywhere.com/auth/register", requestOptions)
    .then((response) => response.json())
    .then((data) => {
      // Mostrar mensaje en un alert
      alert(data.message);
      // Redireccionar al usuario al login
      window.location.href = "/";
    })
    .catch((error) => {
      // Mostrar el error en el DOM
      const errorContainer = document.getElementById("error-container");
      errorContainer.textContent = error.message;
      console.error("Error:", error);
    });
};

// Validacion de Variables
document
  .getElementById("registroForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const nombre = document.getElementById("nombre").value.trim();
    const apellido = document.getElementById("apellido").value.trim();
    const email = document.getElementById("email").value.trim();
    const telefono = document.getElementById("telefono").value.trim();
    const password = document.getElementById("password").value;
    const password2 = document.getElementById("password2").value;

    if (
      !nombre ||
      !apellido ||
      !email ||
      !telefono ||
      !password ||
      !password2
    ) {
      alert("Por favor, complete todos los campos.");
      return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      alert("Por favor, ingrese una dirección de correo electrónico válida.");
      return;
    }

    if (password !== password2) {
      alert("Las contraseñas no coinciden.");
      return;
    }

    const userData = {
      email,
      password,
      nombre,
      apellido,
      telefono,
    };
    console.log(userData);
    register(userData);
  });
