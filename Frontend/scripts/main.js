import obtenerDatosAPI from './fetchData.js';
import renderUserCards from './renderList.js';
import switchActiveInactive from './botonSelectionList.js';
import {paginationPrevie} from './paginationList.js';
import {paginationNexti} from './paginationList.js';

let currentPage = 1;
const limitPerPage = 10;

function main() {
  obtenerDatosAPI(currentPage, limitPerPage)
    .then(datos => {
      renderUserCards(datos);
    })
    .catch(error => console.error('Error:', error));
}

paginationPrevie(currentPage, limitPerPage);
paginationNexti(currentPage, limitPerPage);
switchActiveInactive();
main()
