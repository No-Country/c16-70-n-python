import obtenerDatosAPI from './fetchData.js';
import renderUserCards from './renderList.js';
import switchActiveInactive from './botonSelectionList.js';
import obtenerTurnosAssignedAPI from './fetchTurnAssigned.js';
import { renderCardsTurnActive } from './renderCardsTurnActive.js';
import {paginationPrevie} from './paginationList.js';
import {paginationNexti} from './paginationList.js';


function main() {
  obtenerDatosAPI()
  .then(datos => {
    renderUserCards(datos);
  })
  .catch(error => console.error('Error:', error));
}



// paginationPrevie(currentPage);
// paginationNexti(currentPage);
switchActiveInactive();


main()
