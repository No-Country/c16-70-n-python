//import deleteServices from "./deleteServices.js";

import selectionTurn from "./selectionTurn.js";
import { apiUrlServer } from "../js/config.js";

function formatDateTime(dateTimeString) {
  const dateTime = new Date(dateTimeString);
  const formattedDate = `${dateTime.getDate()}/${
    dateTime.getMonth() + 1
  }/${dateTime.getFullYear()}`;
  const formattedTime = `${("0" + dateTime.getHours()).slice(-2)}:${(
    "0" + dateTime.getMinutes()
  ).slice(-2)}`;
  return `${formattedDate} ${formattedTime}`;
}

function capitalizarPrimeraLetra(texto) {
  return texto.charAt(0).toUpperCase() + texto.slice(1);
}

function cleanUserCards() {
  const container = document.getElementById("table-container");
  let child = container.lastElementChild;
  while (child !== document.getElementById("table-person-template")) {
    container.removeChild(child);
    child = container.lastElementChild;
  }
}

//
export function renderCardsTurnAssigned(data) {
  cleanUserCards();
  console.log("service_data:", data);
  const container = document.getElementById("table-container");
  const template = document.getElementById("table-person-template").content;
  const paginationPrev = document.getElementById("pagination-prev");
  const paginationNext = document.getElementById("pagination-next");

  data.forEach((turn) => {
    const userCard = document.importNode(template, true);
    userCard.querySelector(".card-turn-info h3").textContent =
      "Turno " + turn.id;
    userCard.querySelector(".turn-service p").textContent =
      turn.service_info.service_description;
    userCard.querySelector(".turn-start p").textContent = turn.start_turn;
    userCard.querySelector(".turn-date small").textContent =
      turn.date_assignment;
    userCard.querySelector(".selection").dataset.id = turn.id;

    // Botones
    const viewButton = userCard.querySelector(".btn-view");
    viewButton.addEventListener("click", () => {
      // Lógica para ver detalles del turno
      mostrarDetallesTurno(turn.id);
    });

    // Funcion para ver el turno Individualmente :

    function mostrarDetallesTurno(turnoId) {
      const token = sessionStorage.getItem("token");
      const apiUrl = apiUrlServer + `admin/turnos/${turnoId}`;
      const myHeaders = new Headers();
      myHeaders.append("Authorization", "Bearer " + token);
      const requestOptions = {
        method: "GET",
        headers: myHeaders,
        redirect: "follow",
      };

      // Crear un div para el fondo oscuro
      const darkBackground = document.createElement("div");
      darkBackground.classList.add("dark-background");

      // Crear un div para la tarjeta de detalles
      const detailsCard = document.createElement("div");
      detailsCard.classList.add("details-card");

      // Realizar la solicitud Fetch para obtener los detalles del turno
      fetch(apiUrl, requestOptions)
        .then((response) => {
          if (!response.ok) {
            throw new Error("Error al obtener detalles del turno");
          }
          return response.json();
        })
        .then((turnoDetalles) => {
          // Formatear la fecha de inicio y de fin
          const formattedStartTime = formatDateTime(turnoDetalles.start_time);
          const formattedEndTime = formatDateTime(turnoDetalles.end_time);
          const availability = turnoDetalles.assigned ? "Disponible" : "No";

          // Construir la estructura HTML para mostrar los detalles del turno y del paciente
          const detailsHTML = `
        
        <br/>
        <p>Turno : ${turnoDetalles.id}</p>
        <br/>
        <p>Nombre: ${turnoDetalles.name || "No Disponible"}</p>
        <p>Descripción: ${turnoDetalles.description || "No Disponible"}</p>
        <p>Inicio: ${turnoDetalles.start_time}</p>
        <p>Fin: ${turnoDetalles.end_time}</p>
        <p>Disponibilidad: ${availability}</p>
        <br/>
        <p>Información del paciente:</p>
          <spam>Nombre: ${turnoDetalles.patient_info.first_name} ${
            turnoDetalles.patient_info.last_name
          }</spam>
          <br/>
          <br/>
          <img src="${
            apiUrlServer + "static/" + turnoDetalles.patient_info.img
          }" alt="Imagen del paciente">
        
      `;

          // Agregar el contenido HTML a la tarjeta de detalles
          detailsCard.innerHTML = detailsHTML;

          // Agregar la tarjeta de detalles al cuerpo del documento
          document.body.appendChild(darkBackground);
          document.body.appendChild(detailsCard);
        })
        .catch((error) => {
          console.error("Error:", error);
        });

      // Agregar evento para cerrar la tarjeta de detalles
      darkBackground.addEventListener("click", () => {
        document.body.removeChild(darkBackground);
        document.body.removeChild(detailsCard);
      });
    }

    const editButton = userCard.querySelector(".btn-edit");
    editButton.addEventListener("click", () => {
      // Lógica para editar el turno
    });

    const deleteButton = userCard.querySelector(".btn-delete");
    deleteButton.addEventListener("click", () => {
      const token = sessionStorage.getItem("token");

      const turnoId = turn.id; // Obtenemos el ID del turno
      const myHeaders = new Headers();
      myHeaders.append("Authorization", "Bearer " + token);

      const requestOptions = {
        method: "DELETE",
        headers: myHeaders,
        redirect: "follow",
      };

      fetch(`${apiUrlServer}admin/turnos/${turnoId}`, requestOptions)
        .then((response) => response.text())
        .then((result) => {
          console.log(result);
          window.location.reload();
          //obtenerYRenderizarTurnos();
        })
        .catch((error) => console.error(error));
    });

    container.appendChild(userCard);
  });
}

function deleteTurn(turnId) {
  // Realizar petición fetch para eliminar el turno con ID turnId
  fetch(`${apiUrlServer}/turnos/${turnId}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      // Aquí puedes agregar el token de autenticación si es necesario
    },
  })
    .then((response) => {
      if (response.ok) {
        // Lógica adicional si la eliminación es exitosa
        console.log("Turno eliminado exitosamente");
        window.location.reload(); // Recargar la página después de eliminar el turno
      } else {
        // Manejo de errores
        console.error("Error al eliminar el turno");
      }
    })
    .catch((error) => {
      console.error("Error de red:", error);
    });
}
// //import deleteServices from "./deleteServices.js"
// import selectionTurn from "./selectionTurn.js"
// function capitalizarPrimeraLetra(texto) {
//   return texto.charAt(0).toUpperCase() + texto.slice(1);
// }
// function cleanUserCards() {
//     const container = document.getElementById('table-container-active');
//     let child = container.lastElementChild;
//     while (child !== document.getElementById('table-client-template-turn-active')) {
//       container.removeChild(child);
//       child = container.lastElementChild;
//     }
//   }
// function cleanUserCardsInactive() {
//   const container = document.getElementById('table-container-inactive');
//   let child = container.lastElementChild;
//   while (child !== document.getElementById('table-client-template-turn-inactive')) {
//     container.removeChild(child);
//     child = container.lastElementChild;
//   }
// }

// export function renderCardsTurnActive(data) {
//     cleanUserCards();
//     console.log("service_data:",data);
//     const container = document.getElementById('table-container-active');
//     const template = document.getElementById('table-client-template-turn-active').content;
//     const paginationPrev = document.getElementById('pagination-prev');
//     const paginationNext = document.getElementById('pagination-next');
//     console.log("data_service",data)
//     console.log("data_service",data[0].assigmentturn)

//       data.forEach((turn,index) => {
//         console.log("data_service",data)
//         const userCard = document.importNode(template, true);
//         userCard.querySelector('.card-turn-info h3').textContent = "Turno #" + turn.idturn
//         userCard.querySelector('.turn-service p').textContent = "Nombre de servicio"
//         userCard.querySelector('.turn-start p').textContent = turn.turn_start
//         userCard.querySelector('.turn-date small').textContent = turn.assigmentturn
//         // userCard.querySelector('.selection').dataset.id = turn.id;
//         container.appendChild(userCard);
//       });

//       releaseTurn()
//     //editCardService()
//     // paginationPrev.classList.toggle('hidden', currentPage = 1); // ! checar el control de la paginacion
//     // paginationNext.classList.toggle('hidden', currentPage == 1);

//    // const update = document.querySelectorAll(".edit");
//   //  console.log("update", update);

//     //update.forEach(update => {
//    //   update.addEventListener('click', () => {
//      //   console.log("aquie identificador");
//      //   console.log(update.dataset.id);
//      //   sessionStorage.setItem("userid", update.dataset.id);
//     //  })
//    // })

//   }

//   export  function renderCardsTurnInactive(data) {
//     cleanUserCardsInactive();
//     console.log("service_data:",data);
//     const container = document.getElementById('table-container-inactive');
//     const template = document.getElementById('table-client-template-turn-inactive').content;
//     const paginationPrev = document.getElementById('pagination-prev');
//     const paginationNext = document.getElementById('pagination-next');
//     console.log("data_service",data)
//     console.log("data_service",data[0].assigmentturn)

//       data.forEach((turn,index) => {
//         console.log("data_service",data)
//         const userCard = document.importNode(template, true);
//         userCard.querySelector('.card-turn-info h3').textContent = "Turno #" + turn.idturn
//         userCard.querySelector('.turn-service p').textContent = "Nombre de servicio"
//         userCard.querySelector('.turn-start p').textContent = turn.turn_finish
//         userCard.querySelector('.turn-date small').textContent = turn.assigmentturn
//         container.appendChild(userCard);
//       });

//    //selectionTurn()
//     //editCardService()
//     // paginationPrev.classList.toggle('hidden', currentPage = 1); // ! checar el control de la paginacion
//     // paginationNext.classList.toggle('hidden', currentPage == 1);

//    // const update = document.querySelectorAll(".edit");
//   //  console.log("update", update);

//     //update.forEach(update => {
//    //   update.addEventListener('click', () => {
//      //   console.log("aquie identificador");
//      //   console.log(update.dataset.id);
//      //   sessionStorage.setItem("userid", update.dataset.id);
//     //  })
//    // })

//   }
