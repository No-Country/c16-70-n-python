function obtenerYMostrarToken() {
  const token = sessionStorage.getItem("token");

  if (!token) {
      window.location.href = "http://127.0.0.1:5500/frontend/";
      return;
  }

  var myHeaders = new Headers();
  myHeaders.append("Authorization", "Bearer " + token);

  var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      redirect: 'follow'
  };

  fetch("http://127.0.0.1:5000/rol", requestOptions)
      .then(response => response.text())
      .then(result => {
          console.log(result);
          if (result === "cliente") {
              window.location.href = "http://127.0.0.1:5500/frontend/ruta-para-clientes";
          } else if (result === "proveedor") {
              window.location.href = "http://127.0.0.1:5500/frontend/ruta-para-proveedores";
          } else {
              console.log("Rol desconocido");
              
              window.location.href = "http://127.0.0.1:5500/frontend/";
          }
      })
      .catch(error => console.log('error', error));
}

window.onload = () => {
  obtenerYMostrarToken();
};
