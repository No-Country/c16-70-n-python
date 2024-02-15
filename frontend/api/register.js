function register(username, email, password, password2, role ) {
  //Esto es un ejemplo
  //validacion
  if (password !== password2){
    return console.log('Error el password no Coinciden ')
  }
  if (username, email, password, password2, role) {
      console.log(username, email, password, password2, role)
      alert("Registro exitoso");
      window.location.href = "welcome.html";
  }
}

document
  .getElementById("registroForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const password2 = document.getElementById("password2").value;
    const role = document.getElementById("role").value;

    register(username, password, password2, email, role);
  });
