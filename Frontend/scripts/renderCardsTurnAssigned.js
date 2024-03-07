//import deleteServices from "./deleteServices.js"
import selectionTurn from "./selectionTurn.js"
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

export function renderCardsTurnAssigned(data) {
    cleanUserCards();
    console.log("service_data:",data);
    const container = document.getElementById('table-container');
    const template = document.getElementById('table-person-template').content;
    const paginationPrev = document.getElementById('pagination-prev');
    const paginationNext = document.getElementById('pagination-next');
    console.log("data_service",data)
    console.log("data_service",data[0].assigmentturn)
    
      data.forEach((turn,index) => {
        console.log("data_service",data)
        const userCard = document.importNode(template, true);
        userCard.querySelector('.card-turn-info h3').textContent = "Turno #" + turn.id
        userCard.querySelector('.turn-service p').textContent = turn.service_info.service_description
        userCard.querySelector('.turn-start p').textContent = turn.start_turn
        userCard.querySelector('.turn-date small').textContent = turn.assigmentturn
        // userCard.querySelector('.selection').dataset.id = turn.id;
        container.appendChild(userCard);
      });
      
    
   
    
      //releaseTurn()
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

  