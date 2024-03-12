import {updateService} from "./fechtServiceUpdate.js"

// actualizados hoy 030324-0234pm

export default function editCardService() {
  const editButton = document.querySelectorAll(".edit")
  const editCard = document.querySelectorAll(".card-turn-info strong")
  
  function activarEdicion(index) {
    console.log(editCard)
    editCard[index].contentEditable = 'true';
    editCard[index].focus()
    
  }
  function desactivarEdicion(index) {
    editCard[index].contentEditable = 'false';
  }

  let idCard
  
  editButton.forEach((button, index) => {
    button.addEventListener("click", () =>{
      console.log("click en botón")
      console.log(button)
      idCard = index
      console.log("id",idCard)
      activarEdicion(idCard)
      
      
    })
  })
 
  editCard.forEach(card => {
    card.addEventListener('blur', async(e) => {
      console.log("pierde foco")
      desactivarEdicion(idCard)
      let textService = card.textContent
      console.log(textService)
      await updateService(idCard,textService) // ! falta el enpoint para actualizar
      console.log("servicio actualizado")
      
    })
  })
  

}