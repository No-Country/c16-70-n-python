import selectionServices from "./selectionService.js"
import editCardService from "./editServices.js"
function capitalizarPrimeraLetra(texto) {
  return texto.charAt(0).toUpperCase() + texto.slice(1); 
}
function cleanUserCards() {
    const container = document.getElementById('table-container');
    let child = container.lastElementChild;
    while (child !== document.getElementById('table-person-template')) {
      container.removeChild(child);
      child = container.lastElementChild;
    }
  }

export  default function renderCardsService(data) {
    cleanUserCards();
    console.log("service_data:",data);
    const container = document.getElementById('table-container');
    const template = document.getElementById('table-person-template').content;
    const paginationPrev = document.getElementById('pagination-prev');
    const paginationNext = document.getElementById('pagination-next');
    
    
    data.forEach(services => {
      console.log("data_service",data)
      const userCard = document.importNode(template, true);
      // userCard.querySelector('.card-turn-info h3').textContent = "Servicio " + services.id
      
      userCard.querySelector('.card-turn-info strong').textContent = capitalizarPrimeraLetra(services.name);
      // userCard.querySelector('.card-turn-info strong').contentEditable = "false"
      
      userCard.querySelector('.selection').dataset.id = services.id;
      
      container.appendChild(userCard);
    });
    
    selectionServices()
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