//import deleteServices from "./deleteServices.js"
import selectionTurn from "./selectionTurn.js"
function capitalizarPrimeraLetra(texto) {
  return texto.charAt(0).toUpperCase() + texto.slice(1); 
}
function cleanUserCards() {
    const container = document.getElementById('table-container-active');
    let child = container.lastElementChild;
    while (child !== document.getElementById('table-client-template-turn-active')) {
      container.removeChild(child);
      child = container.lastElementChild;
    }
  }

export  default function renderCardsTurnActive(data) {
    cleanUserCards();
    console.log("service_data:",data);
    const container = document.getElementById('table-container-active');
    const template = document.getElementById('table-client-template-turn-active').content;
    const paginationPrev = document.getElementById('pagination-prev');
    const paginationNext = document.getElementById('pagination-next');
    
    
    data.forEach((turn,index) => {
      console.log("data_service",data)
      const userCard = document.importNode(template, true);
      // userCard.querySelector('.card-turn-info h3').textContent = "Servicio " + services.id
      userCard.querySelector('.card-turn-info h3').textContent = "Turno #" + (index+1)
      userCard.querySelector('.turn-start p').textContent = turn.turn_start
      userCard.querySelector('.turn-date small').textContent = turn.assigmentturn
      userCard.querySelector('.turn-service p').textContent = "teste"
      userCard.querySelector('.turn-start p').textContent = turn.turn_start
      userCard.querySelector('.turn-date small').textContent = turn.assigmentturn
      
    //   userCard.querySelector('.selection').dataset.id = turn.idturn;
      
      container.appendChild(userCard);
    });
    
   selectionTurn()
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