import obtenerDatosAPI from './fetchData.js';
import renderUserCards from './renderList.js';
import switchActiveInactive from './botonSelectionList.js';
import obtenerTurnosAssignedAPI from './fetchTurnAssigned.js';
import { renderCardsTurnActive } from './renderCardsTurnActive.js';
import {paginationPrevie} from './paginationList.js';
import {paginationNexti} from './paginationList.js';
import { apiUrlServer } from '../js/config.js';

const token = sessionStorage.getItem("token");

// 
let currentPage=1;
// 

async function fetchPages(apiUrlServer, currentPage, token) {

  try {
    const myHeaders = new Headers();
    myHeaders.append("Authorization", `Bearer ${token}`);
    const requestOptions = {
      method: "GET",
      headers: myHeaders,
      redirect: "follow"
    };
    const response = await fetch(`${apiUrlServer}?page=${currentPage}`, requestOptions);
    const data = await response.json();
    renderUserCards(data, currentPage);
  } catch (error) {
    //console.error('Error:', error);
  }
}

function handlePaginationClick(offset) {
  currentPage += offset;
  fetchPages(apiUrlServer+'admin/pacientes', currentPage, token);
}

function main() {
  obtenerDatosAPI(apiUrlServer, currentPage, token)
    .then(datos => {
      renderUserCards(datos);
    })
    .catch(error => console.error('Error:', error));
}

function initializePagination() {
  const paginationPrev = document.getElementById('pagination-prev');
  const paginationNext = document.getElementById('pagination-next');

  paginationPrev.addEventListener('click', () => handlePaginationClick(-1));
  paginationNext.addEventListener('click', () => handlePaginationClick(1));
}

initializePagination();

main()

// function main() {
//   obtenerDatosAPI()
//   .then(datos => {
//     renderUserCards(datos);
//   })
//   .catch(error => console.error('Error:', error));
// }



// paginationPrevie(currentPage);
// paginationNexti(currentPage);
// switchActiveInactive();


// main()
