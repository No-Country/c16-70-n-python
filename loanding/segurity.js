import { apiUrlServer } from "/js/config.js";
async function obtenerYMostrarToken() {
    const token = sessionStorage.getItem("token");
  
    if (!token) {
        window.location.href = "/index.html";
        return;
    }
  
    var myHeaders = new Headers();
    myHeaders.append("Authorization", "Bearer " + token);
  
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        redirect: 'follow'
    };
  
    await fetch(apiUrlServer + "/auth/rol", requestOptions)
        .then(response => response.json())
        .then(data => {
            if (data.role === "Paciente") {
                window.location.href = "/cliente-panel/cliente-panel-principal.html";
            } else if (data.role == "Admin") {
                window.location.href = "/admin-panel/admin-panel-all-users.html";
            } else {
                console.log("Rol desconocido");
  
                window.location.href = "/index.html";
            }
        })
        .catch(error => console.log('error', error));
  }
  
  window.onload = () => {
    obtenerYMostrarToken();
  };