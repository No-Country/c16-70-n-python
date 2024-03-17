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
function cleanUserCardsInactive() {
  const container = document.getElementById('table-container-inactive');
  let child = container.lastElementChild;
  while (child !== document.getElementById('table-client-template-turn-inactive')) {
    container.removeChild(child);
    child = container.lastElementChild;
  }
}


export function renderCardsTurnActive(data) {
    cleanUserCards();
    console.log("service_data:",data);
    const container = document.getElementById('table-container-active');
    const template = document.getElementById('table-client-template-turn-active').content;
    // const paginationPrev = document.getElementById('pagination-prev');
    // const paginationNext = document.getElementById('pagination-next');
    console.log("data_service", Object.keys(data).length)
    // console.log("data_service",data[0].assigmentturn)
    if (Object.keys(data).length == 1){
      const userCard = document.importNode(template, true);
      userCard.querySelector('.card-turn-info h3').textContent = "No hay turnos activos"
      userCard.querySelector('.turn-start').classList.add("hidden");
      userCard.querySelector('.turn-date').classList.add("hidden")
      userCard.querySelector('.card-turn-img').classList.add("hidden")
      container.appendChild(userCard);
    } else {
      data.forEach((turn,index) => {
        console.log("data_service",data)
        const userCard = document.importNode(template, true);
        userCard.querySelector('.card-turn-info h3').textContent = "Turno #" + turn.idturn
        userCard.querySelector('.turn-service p').textContent = "Nombre de servicio"
        userCard.querySelector('.turn-start p').textContent = turn.turn_start
        userCard.querySelector('.turn-date small').textContent = turn.assigmentturn
        // userCard.querySelector('.selection').dataset.id = turn.id;
        container.appendChild(userCard);
      });
    }
      
      
    
   
    
      // releaseTurn()
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

  export  function renderCardsTurnInactive(data) {
    cleanUserCardsInactive();
    console.log("service_data:",data);
    const container = document.getElementById('table-container-inactive');
    const template = document.getElementById('table-client-template-turn-inactive').content;
    // const paginationPrev = document.getElementById('pagination-prev');
    // const paginationNext = document.getElementById('pagination-next');
    console.log("data_service",data)
    // console.log("data_service",data[0].assigmentturn)
    if(Object.keys(data).length == 1){
      const userCard = document.importNode(template, true);
      userCard.querySelector('.card-turn-info h3').textContent = "Sin historial"
      userCard.querySelector('.turn-start').classList.add("hidden");
      userCard.querySelector('.turn-date').classList.add("hidden")
      userCard.querySelector('.card-turn-img').classList.add("hidden")
      container.appendChild(userCard);
    }else{
      data.forEach((turn,index) => {
        console.log("data_service",data)
        const userCard = document.importNode(template, true);
        userCard.querySelector('.card-turn-info h3').textContent = "Turno #" + turn.idturn
        userCard.querySelector('.turn-service p').textContent = "Nombre de servicio"
        userCard.querySelector('.turn-start p').textContent = turn.turn_finish
        userCard.querySelector('.turn-date small').textContent = turn.assigmentturn
        container.appendChild(userCard);
      });
    }

      
    
   
    
   //selectionTurn()
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