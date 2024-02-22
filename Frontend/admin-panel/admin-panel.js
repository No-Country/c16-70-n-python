const paginationPrev = document.getElementById('pagination-prev');
const paginationNext = document.getElementById('pagination-next');

let currentPage = 1;
const limitPerPage = 10;

paginationPrev.addEventListener('click', () => {
  if (currentPage > 1) {
    currentPage--;
    obtenerDatosAPI(currentPage, limitPerPage)
      .then(renderUserCards)
      .catch(error => console.error('Error:', error));
  }
});

paginationNext.addEventListener('click', () => {
  currentPage++;
  obtenerDatosAPI(currentPage, limitPerPage)
    .then(renderUserCards)
    .catch(error => console.error('Error:', error));
});

async function obtenerDatosAPI(page, limit) {
  const apiUrl = `http://localhost:3000/users?_page=${page}&_per_page=${limit}`;
  

  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    console.log("aqui",data);
    return data;
  } catch (error) {
    return console.error('Error:', error);
  }
}
function cleanUserCards() {
  const container = document.getElementById('table-container');
  let child = container.lastElementChild;
  while (child !== document.getElementById('table-person-template')) {
    container.removeChild(child);
    child = container.lastElementChild;
  }
}
function renderUserCards(data) {
  console.log(data);
  cleanUserCards();
  const container = document.getElementById('table-container');
  const template = document.getElementById('table-person-template').content;
  const paginationPrev = document.getElementById('pagination-prev');
  const paginationNext = document.getElementById('pagination-next');
  
  data.data.forEach(user => {
    const userCard = document.importNode(template, true);
    if (user.profileImgUrl == undefined) {
        userCard.querySelector('.user img').src = 'images/profile_8.jpg';
    } else {
        userCard.querySelector('.user img').src = user.profileImgUrl;
    }
    userCard.querySelector('.user-info strong').textContent = user.name;
    userCard.querySelector('.user-info small').textContent = user.email;
    userCard.querySelector('.role p').textContent = "Admin";
    userCard.querySelector('.count-type p').textContent = user.accountType;
    userCard.querySelector('.status p').textContent = user.status;
    userCard.querySelector('.date-incription p').textContent = user.registrationDate;
    container.appendChild(userCard);
  });
  paginationPrev.classList.toggle('hidden', data.prev <= 0);
  paginationNext.classList.toggle('hidden', data.next == null);
}





function main() {
  obtenerDatosAPI(currentPage, limitPerPage)
    .then(datos => {
      renderUserCards(datos);
    })
    .catch(error => console.error('Error:', error));
}

//switch between active and inactive
document.addEventListener('DOMContentLoaded', () => {
  const navSelection = document.querySelector('.nav-selection');
  navSelection.addEventListener('click', (event) => {
    const target = event.target;
    if (target.classList.contains('nav-selection--inactive')) {
      const active = navSelection.querySelector('.nav-selection--active');
      active.classList.replace('nav-selection--active', 'nav-selection--inactive');
      target.classList.replace('nav-selection--inactive', 'nav-selection--active');
    }
  });
});





main()
