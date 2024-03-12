import { apiUrlServer } from "/js/config.js";
function formatearFecha(fechaISO) {
  var fecha = new Date(fechaISO);
  var dia = fecha.getDate();
  var mes = fecha.getMonth() + 1;
  var año = fecha.getFullYear();
  return dia + ' ' + obtenerNombreMes(mes) + ' ' + año;
}

// Función para obtener el nombre del mes
function obtenerNombreMes(numeroMes) {
  var meses = [
      "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
      "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
  ];
  return meses[numeroMes - 1];
}
function cleanUserCards() {
    const container = document.getElementById('table-container');
    let child = container.lastElementChild;
    while (child !== document.getElementById('table-person-template')) {
      container.removeChild(child);
      child = container.lastElementChild;
    }
  }
  export default function renderUserCards(data, currentPage) {
    cleanUserCards();
    const container = document.getElementById('table-container');
    const template = document.getElementById('table-person-template').content;
    const paginationPrev = document.getElementById('pagination-prev');
    const paginationNext = document.getElementById('pagination-next');
    
    
    data.forEach(user => {
      console.log("data_user",data)
      const userCard = document.importNode(template, true);
      if (user.profile_img == undefined) {
          userCard.querySelector('.user img').src = '/img/profile_8.jpg';
      } else {
          userCard.querySelector('.user img').src = apiUrlServer + "/static/" + user.profile_img          ;
      }
      userCard.querySelector('.user-info strong').textContent = user.first_name + " " + user.last_name;
      userCard.querySelector('.user-info small').textContent = user.email;
      userCard.querySelector('.role p').textContent = user.role;
      userCard.querySelector('.count-type p').textContent = user.accountType;
      userCard.querySelector('.status p').textContent = user.status;
      userCard.querySelector('.date-incription p').textContent = formatearFecha(user.register_date);
      userCard.querySelector('.edit').dataset.id = user.id;
      userCard.querySelector('.delete').dataset.id = user.id;
      container.appendChild(userCard);
    });
    // paginationPrev.classList.toggle('hidden', currentPage = 1); // ! checar el control de la paginacion
    // paginationNext.classList.toggle('hidden', currentPage == 1);

    const update = document.querySelectorAll(".edit");
    console.log("update", update);
    update.forEach(update => {
      update.addEventListener('click', () => {
        console.log("aquie identificador");
        console.log(update.dataset.id);
        sessionStorage.setItem("userid", update.dataset.id);
      })
    })
    
  }