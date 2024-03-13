import { apiUrlServer } from "../js/config.js";

const token = sessionStorage.getItem("token");

let currentPage = 1;
let datos;

// formato fecha 

function formatarFecha(fecha) {
  // Crear un objeto de fecha con la cadena proporcionada
  const fechaObjeto = new Date(fecha);

  // Obtener los componentes de la fecha
  const año = fechaObjeto.getFullYear();
  const mes = ('0' + (fechaObjeto.getMonth() + 1)).slice(-2); // Agrega un cero al principio si el mes es menor que 10
  const día = ('0' + fechaObjeto.getDate()).slice(-2); // Agrega un cero al principio si el día es menor que 10

  // Devolver la fecha formateada en el formato deseado
  return `${año}-${mes}-${día}`;
}

async function fetchPages(apiUrlServer, currentPage, token) {
  try {
    const myHeaders = new Headers();
    myHeaders.append("Authorization", `Bearer ${token}`);
    const requestOptions = {
      method: "GET",
      headers: myHeaders,
      redirect: "follow",
    };
    const response = await fetch(
      `${apiUrlServer}admin/turnos/complet?page=${currentPage}`,
      requestOptions
    );
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json(); // Convertir la respuesta a JSON
    return data; // Retornar los datos
  } catch (error) {
    console.error('Error:', error);
    throw error; // Lanzar el error para manejarlo en la llamada
  }
}

function handlePaginationClick(offset) {
  currentPage += offset;
  fetchPages(apiUrlServer, currentPage, token)
    .then(datos => {
      renderTunsCards(datos);
    })
    .catch(error => console.error('Error:', error));
}

function cleanCards() {
  const container = document.getElementById("table-container");
  let child = container.lastElementChild;
  while (child !== document.getElementById("table-turn-template")) {
    container.removeChild(child);
    child = container.lastElementChild;
  }
}

export function renderTunsCards(data) {
  cleanCards();
  const container = document.getElementById("table-container");
  const template = document.getElementById("table-turn-template").content;

  // Recorrer los datos y crear una tarjeta para cada turno
  data.forEach((turno) => {
    const clone = document.importNode(template, true);

    clone.querySelector(".card-turn-info h3").textContent = "Turno " + turno.id;
    clone.querySelector(".turn-service p").textContent = turno.description
      ? turno.description
      : "Sin Descripción";
    clone.querySelector(".turn-start p").textContent = turno.start_turn
      ? turno.start_turn
      : "Hora de inicio no disponible";
      // 
    const fechaFormateada = formatarFecha(turno.date_assignment);
    
    clone.querySelector(".turn-date small").textContent = fechaFormateada;

    clone.querySelector(".selection").dataset.id = turno.id;

    container.appendChild(clone);
  });
}



function main() {
  fetchPages(apiUrlServer, currentPage, token)
    .then(datos => {
      renderTunsCards(datos);
    })
    .catch(error => console.error('Error:', error));
}

main();

function initializePagination() {
  const paginationPrev = document.getElementById("pagination-prev");
  const paginationNext = document.getElementById("pagination-next");

  paginationPrev.addEventListener("click", () => handlePaginationClick(-1));
  paginationNext.addEventListener("click", () => handlePaginationClick(1));
}

initializePagination();
