import { apiUrl } from "../js/config.js";

const login = (email, password) => {
  console.log("aqui",apiUrl);
  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  const requestOptions = {
    method: "POST",
    headers: myHeaders,
    body: JSON.stringify({ email, password }),
    redirect: "follow",
  };

  fetch(apiUrl + "/auth/login", requestOptions)
    .then((response) => {
      if (!response.ok) {
        throw new Error(
          "Error al iniciar sesión. Por favor, verifique sus credenciales."
        );
      }
      return response.json();
    })
    .then((data) => {
      if (data.token) {
        sessionStorage.setItem("token", data.token);
        window.location.href = "/Frontend/loanding/index.html";
      } else if (data.message) {
        showMessage(data.message);
      } else {
        throw new Error("Respuesta no válida del servidor.");
      }
    })
    .catch((error) => {
      showError(error.message);
    });
};

const showMessage = (message) => {
  const messageContainer = document.getElementById("message-container");
  messageContainer.textContent = message;
};

const showError = (message) => {
  const errorContainer = document.getElementById("error-container");
  errorContainer.textContent = message;
};

document
  .getElementById("loginForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");
    const email = emailInput.value.trim();
    const password = passwordInput.value.trim();

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      showError(
        "Por favor, ingrese una dirección de correo electrónico válida."
      );
      return;
    }

    if (!password) {
      showError("Por favor, ingrese su contraseña.");
      return;
    }

    login(email, password);
  });
