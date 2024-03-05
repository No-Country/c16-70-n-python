import {putTurnClient} from "./putTurnClientApi.js"
export default function selectionServices () {
  const selectionButton = document.querySelectorAll(".selection")
  selectionButton.forEach(button => {
    button.addEventListener("click", () => {
      console.dir(button.dataset.id)

      
      putTurnClient()
      
     
    })
  })
}

