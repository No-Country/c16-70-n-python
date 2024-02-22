function obtenerYMostrarToken() {
  const token = sessionStorage.getItem("token");

  if (!token) {
      window.location.href = "/Frontend/Home%20Page/Index.html";
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
      .then(response => response.json())
      .then(data => {
          console.log(data);
          if (data.role === "clie") {
              window.location.href = "/Frontend/ruta-para-clientes";
          } else if (data.role === "prov") {
              window.location.href = "/Frontend/ruta-para-proveedores";
            } else if (data.role === "admin") {
              window.location.href = "/Frontend/admin-panel";
          } else {
              console.log("Rol desconocido");
              
              window.location.href = "/Frontend/Home%20Page/Index.html";
          }
      })
      .catch(error => console.log('error', error));
}

window.onload = () => {
  obtenerYMostrarToken();
};
