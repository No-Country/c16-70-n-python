function login(username, password) {
  return fetch("api/data.json")
    .then((response) => response.json())
    .then((data) => {
      const usuarios = data.users;
      return usuarios.find(
        (user) => user.username === username && user.password === password
      );
    })
    .catch((error) => console.error("Error:", error));
}

document
  .getElementById("loginForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    
    login(username, password).then((usuarioAutenticado) => {
      if (usuarioAutenticado) {
        alert("Inicio de sesión exitoso");
        
      } else {
        alert("Credenciales incorrectas. Por favor, inténtalo de nuevo.");
      }
    });
  });
