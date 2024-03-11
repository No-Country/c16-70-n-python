import obtenerDatosAPIUserProfile from "./fetchDataUserProfile.js";
//import renderUserProfile from './renderUserProfile.js';
import { apiUrlServer } from "../js/config.js";

//console.log("aqui_id", sessionStorage.getItem("userid"))
//const userId = sessionStorage.getItem("userid");
const token = sessionStorage.getItem("token");

async function main() {
  try {
    const myHeaders = new Headers();
    myHeaders.append("Authorization", "Bearer " + token);

    const requestOptions = {
      method: "GET",
      headers: myHeaders,
      redirect: "follow",
    };

    const response = await fetch(`${apiUrlServer}user/get`, requestOptions);
    //const data = await response.text();
    const data = await response.json();
    // Obtener referencias a los elementos del DOM
    console.log(data);
    const userNameElement = document.getElementById("user-name");
    const userEmailElement = document.querySelector(".user-email p");
    const phoneNumberElement = document.querySelector(".phone-number p");
    const registerDateElement = document.querySelector(".date-incription p");
    const userImageElement = document.querySelector(".user img");

    // Actualizar los elementos con los datos recibidos
    userNameElement.textContent = data.firstname + " " + data.lastname;
    userEmailElement.textContent = data.email;
    phoneNumberElement.textContent = data.phone;
    registerDateElement.textContent = data.register_date;

    if (data.profile_image) {
      userImageElement.src = apiUrlServer + "static/" + data.profile_image;
    } else {
      userImageElement.src = apiUrlServer + "static/imgs/" + data.profile_image; // Ruta de la imagen por defecto
    }
  } catch (error) {
    console.error(error);
  }
}
main();
