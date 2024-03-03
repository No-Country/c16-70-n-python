import deleteSeevicesApi from "./fetchDeleteService.js"

export default function deleteServices () {
  const deleteButton = document.querySelectorAll(".delete")
  console.log(deleteButton.length)
  deleteButton.forEach(button => {
    button.addEventListener("click", () => {
      console.dir(button.dataset.id)
      deleteSeevicesApi(button.dataset.id)
      .then(() => {
        location.reload()
      })
    })
  })
}

