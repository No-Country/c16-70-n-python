const editButton = document.querySelector(".edit")
const editCard = document.querySelector(".card-turn-info p")

function activarEdicion() {
  editCard.contentEditable = 'true';
}

function desactivarEdicion() {
  editcard.contentEditable = 'false';
}

export function editCardService() {
  const editButton = document.querySelectorAll(".edit")
  const editCard = document.querySelectorAll(".card-turn-info strong")
  
  editButton.forEach(button => {
    button.addEventListener("click", () =>{
      if(editCard.contentEditable === 'true') {
        desactivarEdicion()
      } else {
        activarEdicion()
      }
    })
  })
 

  editableCard.addEventListener('blur', function() {
    desactivarEdicion();
  });

}