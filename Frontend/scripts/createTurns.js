import { apiUrlServer } from "../js/config.js";



document.getElementById("form-create-turno").addEventListener("submit", function(e) {
    e.preventDefault();
    const datos = {
        fecha: document.getElementById("fecha").value,
        inicio: document.getElementById("inicio").value,
        fin: document.getElementById("fin").value,
        duracion: document.getElementById("duracion").value,
    };
    console.log("aqui",datos);
    const token = sessionStorage.getItem("token");
    const myHeaders = new Headers();
    myHeaders.append("Authorization", `Bearer ${token}`);
    myHeaders.append("Content-Type", "application/json");
    const datosEnJSON = JSON.stringify(datos);
    console.log("aqui",datosEnJSON);
    const myInit = {
        method: "POST",
        headers: myHeaders,
        body: datosEnJSON,
        mode: "cors",
        cache: "default",
    };
    fetch(apiUrlServer + "/admin/turnos", myInit)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log(error));
});
