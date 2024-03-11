//import deleteServices from "./deleteServices.js"
import selectionTurn from "./selectionTurn.js";
import { apiUrlServer } from "../js/config.js";
const token = sessionStorage.getItem("token");

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

export default function renderCardsTurn(data) {
  cleanUserCards();
  console.log("service_data:", data);
  const container = document.getElementById("table-container");
  const template = document.getElementById("table-person-template").content;
  const paginationPrev = document.getElementById("pagination-prev");
  const paginationNext = document.getElementById("pagination-next");

  data.forEach((turn, index) => {
    console.log("data_service", data);
    const userCard = document.importNode(template, true);
    // userCard.querySelector('.card-turn-info h3').textContent = "Servicio " + services.id
    userCard.querySelector(".card-turn-info h3").textContent =
      "Turno #" + turn.idturn;

    userCard.querySelector(".turn-start p").textContent = turn.turn_start;
    userCard.querySelector(".turn-date small").textContent = turn.assigmentturn;

    userCard.querySelector(".selection").dataset.id = turn.idturn;
    
    const btnSelect = userCard.querySelector(".btn-select");
    
    btnSelect.dataset.id = turn.idturn;
    btnSelect.addEventListener("click", () => {
      console.log("ID del turno:", btnSelect.dataset.id);

      // Construir la URL de la solicitud Fetch
      const url = `${apiUrlServer}user/turno/asignar/${btnSelect.dataset.id}`;

      // Realizar la solicitud Fetch
      fetch(url, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          Authorization:
            "Bearer " + token,
        },
        body: JSON.stringify({
          id_servicio: 2, /// Por Defecto el servicio 2 seria consulta
        }),
      })
        .then((response) => response.text())
        .then((result) => console.log(result))
        .catch((error) => console.error(error));
    });

    container.appendChild(userCard);
  });

  // Agregar event listener al botón btn-select
  // const selectButtons = document.querySelectorAll(".btn-select");
  // selectButtons.forEach((button) => {
  //   button.addEventListener("click", function () {
  //     const turnId = this.dataset.turnId;
  //     // Construir la URL de la solicitud Fetch
  //     const url = `URL_DEL_BACKEND/${turnId}`;
  //     // Realizar la solicitud Fetch
  //     fetch(url)
  //       .then((response) => {
  //         if (!response.ok) {
  //           throw new Error("Network response was not ok");
  //         }
  //         return response.json();
  //       })
  //       .then((data) => {
  //         // Manejar la respuesta según sea necesario
  //         console.log("Fetch successful:", data);
  //         // Aquí puedes realizar alguna acción adicional con los datos recibidos
  //       })
  //       .catch((error) => {
  //         console.error("There was a problem with the fetch operation:", error);
  //       });
  //   });
  // });

  selectionTurn();
  //editCardService()
  // paginationPrev.classList.toggle('hidden', currentPage = 1); // ! checar el control de la paginacion
  // paginationNext.classList.toggle('hidden', currentPage == 1);

  // const update = document.querySelectorAll(".edit");
  //  console.log("update", update);

  //update.forEach(update => {
  //   update.addEventListener('click', () => {
  //   console.log("aquie identificador");
  //   console.log(update.dataset.id);
  //   sessionStorage.setItem("userid", update.dataset.id);
  //  })
  // })
}