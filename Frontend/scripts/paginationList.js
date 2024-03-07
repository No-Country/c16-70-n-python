// import obtenerDatosAPI from './fetchData.js';
// import renderUserCards from './renderList.js';
// import stateRole from './selectionObjetState.js';



// export function paginationPrevie(currentPage, limitPerPage) {
    
//     const paginationPrev = document.getElementById('pagination-prev');
//     paginationPrev.addEventListener('click', () => {
//         console.log("click_paginacion_prerv", currentPage)
//         if (currentPage > 1) {
//             console.log("aqui_paginacion",currentPage)
//             currentPage--;
//             obtenerDatosAPI(currentPage, stateRole.role)
//             .then(renderUserCards)
//           .catch(error => console.error('Error:', error));
//       }
//     });
// }

// export function paginationNexti(currentPage, limitPerPage) {
//     const paginationNext = document.getElementById('pagination-next');
//     console.log("click_paginacion_next", currentPage)
//     paginationNext.addEventListener('click', () => {
//       console.log("click_paginacion_next", currentPage)
//       currentPage++;
//       obtenerDatosAPI(currentPage, limitPerPage, stateRole.role)
//         .then(renderUserCards)
//         .catch(error => console.error('Error:', error));
//     });
    
// }

// Variables
// const baseURL = 'http://127.0.0.1/admin/pacientes';
// let currentPage = 1;

// // Obtener datos iniciales
// fetchPages();

// // Funciones
// async function fetchPages(urlbase, currentPage) {

//   const url = `${urlbase}?page=${currentPage}`;
  
//   const response = await fetch(url);
//   response.then(data => {
//     return data.json();
//   })
//   .then(data => {
//     renderUserCards(data);
//   })
  
//   // mostrar respuesta en dataContainer 
  
// }

// function goToPage(pageNum) {

//   currentPage = pageNum;
  
//   fetchPages();
  
//   // actualizar numbering 
  
// }

// export function paginationPrevie(currentPage) {
//     const paginationPrev = document.getElementById('pagination-prev');
//     paginationPrev.addEventListener('click', () => {
//         if (currentPage > 1) {
//             goToPage(currentPage - 1);
//         }
//     });
// }



// export function paginationNexti(currentPage) {
//     const paginationNext = document.getElementById('pagination-next');
//     paginationNext.addEventListener('click', () => {
//         goToPage(currentPage + 1);
//     });
// }

export function paginationPrevie(currentPage) {
    const paginationPrev = document.getElementById('pagination-prev');
    paginationPrev.addEventListener('click', () => {
      console.log("click_paginacion_prerv", currentPage)
        currentPage--;
        // if (currentPage > 1) {
        //     ('http://127.0.0.1/admin/pacientes', currentPage - 1);
        // }
    });
}

export function paginationNexti(currentPage) {
    const paginationNext = document.getElementById('pagination-next');
    paginationNext.addEventListener('click', () => {
      console.log("click_paginacion_next", currentPage)
        currentPage++;
        // fetchPages('http://127.0.0.1/admin/pacientes', currentPage + 1);
    });
}

