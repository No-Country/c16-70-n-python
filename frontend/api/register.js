function register(username, password, empresa, email) {
  //Esto es un ejemplo
    if (username, password) {
        console.log(username, password)
        alert("Registro exitoso");
        window.location.href = "welcome.html";
    }
}

document
  .getElementById("registroForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const empresa = document.getElementById("empresa").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    register(username, password, empresa, email);
  });
