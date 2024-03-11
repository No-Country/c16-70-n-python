//import deleteServices from "./deleteServices.js"
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
      "Turno #" + turn.id;
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
      mostrarDetallesTurno(turn);
    });

    function mostrarDetallesTurno(turno) {
      // Crear contenedor para la ventana emergente
      const modalContainer = document.createElement("div");
      modalContainer.classList.add("modal-container");

      // Formateas la fecha de inicio
      const formattedStartTime = formatDateTime(turn.start_turn);
      // Formateas la fecha de fin
      const formattedEndTime = formatDateTime(turn.finish_turn);

      // Crear contenedor para los detalles del turno
      const turnoDetailsContainer = document.createElement("div");
      turnoDetailsContainer.classList.add("turno-details");

      // Convertir la cadena de fecha de creación a un objeto Date y formatearla
      const creationDate = new Date(turno.creation_date);
      // Convertir la cadena de fecha de asignación a un objeto Date y formatearla
      const assignmentDate = new Date(turno.date_assignment);

      // Determinar si el turno está disponible o no
      const availability = turno.bol_assigned ? "Disponible" : "No";

      // Agregar los detalles del turno al contenedor
      const details = `
        <p>ID: ${turno.id}</p>
        <p>Nombre: ${turno.name || "N/A"}</p>
        <p>Descripción: ${turno.description || "N/A"}</p>
        <p>Inicio: ${turno.start_turn}</p>
        <p>Fin: ${turno.finish_turn}</p>
        <p>Disponibilidad: ${availability}</p>
      `;
      turnoDetailsContainer.innerHTML = details;

      // Botón para cerrar la ventana emergente
      const closeButton = document.createElement("button");
      closeButton.textContent = "X";
      closeButton.classList.add("close-button");
      closeButton.addEventListener("click", () => {
        modalContainer.remove();
      });

      // Agregar los contenedores y el botón al DOM
      modalContainer.appendChild(turnoDetailsContainer);
      modalContainer.appendChild(closeButton);
      document.body.appendChild(modalContainer);
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
          obtenerYRenderizarTurnos();
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