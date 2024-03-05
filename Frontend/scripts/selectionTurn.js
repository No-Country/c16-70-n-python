export default function selectionTurn () {
  const selectionButton = document.querySelectorAll(".selection")
  selectionButton.forEach(button => {
    button.addEventListener("click", () => {
      console.log("id_turn",button.dataset.id)
      sessionStorage.setItem("turn_id", button.dataset.id)
      window.location.href = "/frontend/cliente-panel/panel-servicios.html"
     
    })
  })
}

