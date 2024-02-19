const register = (userData) => {
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
  
    const requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: JSON.stringify(userData),
      redirect: 'follow'
    };
  
    fetch(`http://127.0.0.1:5000/register`, requestOptions)
      .then(response => response.json())
      .then(data => {
        // Mostrar mensaje en un alert
        alert(data.message);
      })
      .catch(error => {
        // Mostrar el error en el DOM
        const errorContainer = document.getElementById('error-container');
        errorContainer.textContent = error.message;
        console.error('Error:', error);
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
      const direccion = document.getElementById("direccion").value.trim();
      const password = document.getElementById("password").value;
      const password2 = document.getElementById("password2").value;
      const role = document.getElementById("role").value;
  
      if (
        !nombre ||
        !apellido ||
        !email ||
        !telefono ||
        !direccion ||
        !password ||
        !password2 ||
        !role
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
        role,
        nombre,
        apellido,
        telefono,
        direccion
      };
      register(userData);
    });