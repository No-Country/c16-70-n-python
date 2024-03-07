import {putTurnClient} from "./putTurnClientApi.js"
export default function selectionServices () {
  const selectionButton = document.querySelectorAll(".selection")
  selectionButton.forEach(button => {
    button.addEventListener("click", () => {
      sessionStorage.setItem("service_id", button.dataset.id)
      // sessionStorage.setItem("service_description", button.parentElement.parentElement.parentElement.children[0].textContent.trim().replace(/\s+/g, ' '))

      
      putTurnClient().then(() => {
        window.location.href = "/frontend/cliente-panel/cliente-panel-principal.html"
      })
      
     
    })
  })
}

