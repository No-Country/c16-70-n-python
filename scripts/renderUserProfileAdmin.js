import { suspenderUsuario } from "./susperderActivarUser.js";
import { activarUsuario } from "./susperderActivarUser.js";
import { apiUrlServer } from "../js/config.js";
import formatearFecha from "./formatDate.js";

function cleanUserCards() {
    const container = document.getElementById('table-container');
    let child = container.lastElementChild;
    while (child !== document.getElementById('table-person-template')) {
      container.removeChild(child);
      child = container.lastElementChild;
    }
  }
  export default function renderUserProfile(data) {
    cleanUserCards();
    const container = document.getElementById('table-container');
    const template = document.getElementById('table-person-template').content;
    console.log("data_user",data)
    
    
      const userCard = document.importNode(template, true);
       if (data.img == undefined) {
           userCard.querySelector('.user img').src = 'img/profile_8.jpg';
       } else {
           userCard.querySelector('.user img').src = apiUrlServer + "/static/" + data.img;
       }
      userCard.querySelector('.user-name p').textContent = data.first_name + " " + data.last_name;
      userCard.querySelector('.user-email p').textContent = data.email;
      userCard.querySelector('.phone-number p').textContent = data.phone;
      userCard.querySelector('.role p').textContent = data.role;
      if (data.suspension) {
        userCard.querySelector('.status p').textContent = "Suspendido";
      } else {
        userCard.querySelector('.status p').textContent = "Activo";
      }
      userCard.querySelector('.date-incription p').textContent = formatearFecha(data.data_reister);
      userCard.querySelector('.date-suspension p').textContent = formatearFecha(data.data_suspension);
      ;
      container.appendChild(userCard);

      const susperder = document.getElementById("btn-suspender");
      susperder.addEventListener("click", async(e) => {
        console.log("suspender");
        await suspenderUsuario();
        location.reload();
      })

      const activar = document.getElementById("btn-activar");
      activar.addEventListener("click", async(e) => {
        console.log("suspender");
        await activarUsuario();
        location.reload();
      })
      
  }
