import obtenerDatosAPI from './fetchData.js';
import renderUserCards from './renderList.js';
import stateRole from './selectionObjetState.js';

export function paginationPrevie(currentPage, limitPerPage) {
    
    const paginationPrev = document.getElementById('pagination-prev');
    paginationPrev.addEventListener('click', () => {
        if (currentPage > 1) {
            currentPage--;
            obtenerDatosAPI(currentPage, limitPerPage, stateRole.role)
            .then(renderUserCards)
          .catch(error => console.error('Error:', error));
      }
    });
}

export function paginationNexti(currentPage, limitPerPage) {
    const paginationNext = document.getElementById('pagination-next');
    paginationNext.addEventListener('click', () => {
      currentPage++;
      obtenerDatosAPI(currentPage, limitPerPage, stateRole.role)
        .then(renderUserCards)
        .catch(error => console.error('Error:', error));
    });
    
}
