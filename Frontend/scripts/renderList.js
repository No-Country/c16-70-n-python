import { apiUrlServer } from "../js/config.js";

function formatearFecha(fechaISO) {
  var fecha = new Date(fechaISO);
  var dia = fecha.getDate();
  var mes = fecha.getMonth() + 1;
  var año = fecha.getFullYear();
  return dia + " " + obtenerNombreMes(mes) + " " + año;
}


function eliminarUsuario(id) {
  console.log(id)
  const token = sessionStorage.getItem("token");
  const myHeaders = new Headers();
  myHeaders.append("Authorization", "Bearer " + token);

  const requestOptions = {
      method: "DELETE",
      headers: myHeaders,
      redirect: "follow"
  };

  fetch(`${apiUrlServer}admin/paciente/${id}`, requestOptions)
      .then(response => {
          if (response.ok) {
              console.log("Usuario eliminado con éxito");
              // Aquí puedes realizar alguna acción adicional, como recargar la página
              // window.location.reload();
          } else {
              console.error("Error al eliminar el usuario");
          }
      })
      .catch(error => console.error(error));
}


// Función para obtener el nombre del mes
function obtenerNombreMes(numeroMes) {
  var meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
  ];
  return meses[numeroMes - 1];
}
function cleanUserCards() {
  const container = document.getElementById("table-container");
  let child = container.lastElementChild;
  while (child !== document.getElementById("table-person-template")) {
    container.removeChild(child);
    child = container.lastElementChild;
  }
}
export default function renderUserCards(data, currentPage) {
  cleanUserCards();
  const container = document.getElementById("table-container");
  const template = document.getElementById("table-person-template").content;
  const paginationPrev = document.getElementById("pagination-prev");
  const paginationNext = document.getElementById("pagination-next");

  data.forEach((user) => {
    //console.log("data_user", data);
    const userCard = document.importNode(template, true);

    let imageUrl = apiUrlServer + "static/" + user.profile_img;
    //console.log(imageUrl);
    if (!user.profile_img) {
      imageUrl = imageUrl;
    }
    userCard.querySelector(".user img").src = imageUrl;
    userCard.querySelector(".user-info strong").textContent =
      user.first_name + " " + user.last_name;
    userCard.querySelector(".user-info small").textContent = user.email;
    userCard.querySelector(".role p").textContent = user.role;
    userCard.querySelector(".count-type p").textContent = user.accountType;
    userCard.querySelector(".status p").textContent = user.status;
    userCard.querySelector(".date-incription p").textContent = formatearFecha(
      user.register_date
    );
    userCard.querySelector(".edit").dataset.id = user.id;
    userCard.querySelector(".delete").dataset.id = user.id;
    container.appendChild(userCard);
  });
  //paginationPrev.classList.toggle('hidden', currentPage = 1); // ! checar el control de la paginacion
  //paginationNext.classList.toggle('hidden', currentPage == 1);

  const update = document.querySelectorAll(".edit");
  //console.log("update", update);
  update.forEach((update) => {
    update.addEventListener("click", () => {
      console.log("aquie identificador");
      console.log(update.dataset.id);
      sessionStorage.setItem("userid", update.dataset.id);
    });
  });

  const deleteButton = userCard.querySelector(".delete");
  deleteButton.dataset.id = user.id; // Asignar el ID del usuario al botón de eliminar

  // Agregar evento de clic al botón de eliminar
  deleteButton.addEventListener("click", function (event) {
    event.preventDefault(); // Evitar comportamiento predeterminado del enlace
    const userId = this.dataset.id; // Obtener ID del usuario
    eliminarUsuario(userId); // Llamar a la función para eliminar el usuario
  });

}

// function formatearFecha(fechaISO) {
//   var fecha = new Date(fechaISO);
//   var dia = fecha.getDate();
//   var mes = fecha.getMonth() + 1;
//   var año = fecha.getFullYear();
//   return dia + ' ' + obtenerNombreMes(mes) + ' ' + año;
// }

// // Función para obtener el nombre del mes
// function obtenerNombreMes(numeroMes) {
//   var meses = [
//       "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
//       "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
//   ];
//   return meses[numeroMes - 1];
// }
// function cleanUserCards() {
//     const container = document.getElementById('table-container');
//     let child = container.lastElementChild;
//     while (child !== document.getElementById('table-person-template')) {
//       container.removeChild(child);
//       child = container.lastElementChild;
//     }
//   }
//   export default function renderUserCards(data, currentPage) {
//     cleanUserCards();
//     const container = document.getElementById('table-container');
//     const template = document.getElementById('table-person-template').content;
//     const paginationPrev = document.getElementById('pagination-prev');
//     const paginationNext = document.getElementById('pagination-next');
    
    
//     data.forEach(user => {
//       console.log("data_user",data)
//       const userCard = document.importNode(template, true);
//       if (user.profileImgUrl == undefined) {
//           userCard.querySelector('.user img').src = 'images/profile_8.jpg';
//       } else {
//           userCard.querySelector('.user img').src = user.profileImgUrl;
//       }
//       userCard.querySelector('.user-info strong').textContent = user.first_name + " " + user.last_name;
//       userCard.querySelector('.user-info small').textContent = user.email;
//       userCard.querySelector('.role p').textContent = user.role;
//       userCard.querySelector('.count-type p').textContent = user.accountType;
//       userCard.querySelector('.status p').textContent = user.status;
//       userCard.querySelector('.date-incription p').textContent = formatearFecha(user.register_date);
//       userCard.querySelector('.edit').dataset.id = user.id;
//       userCard.querySelector('.delete').dataset.id = user.id;
//       container.appendChild(userCard);
//     });
//     // paginationPrev.classList.toggle('hidden', currentPage = 1); // ! checar el control de la paginacion
//     // paginationNext.classList.toggle('hidden', currentPage == 1);

//     const update = document.querySelectorAll(".edit");
//     console.log("update", update);
//     update.forEach(update => {
//       update.addEventListener('click', () => {
//         console.log("aquie identificador");
//         console.log(update.dataset.id);
//         sessionStorage.setItem("userid", update.dataset.id);
//       })
//     })
    
//   }