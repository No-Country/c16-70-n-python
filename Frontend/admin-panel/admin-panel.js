function obtenerDatosAPI() {
  const apiUrl = 'http://localhost:3000/users';

  return fetch(apiUrl)
    .then(response => response.json())
    .catch(error => console.error('Error:', error));
}

function renderUserCards(data) {
  const container = document.getElementById('table-container');
  const template = document.getElementById('table-person-template').content;

  data.forEach(user => {
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
}

function main() {
  obtenerDatosAPI()
    .then(datos => {
      renderUserCards(datos);
    })
    .catch(error => console.error('Error:', error));
}


document.addEventListener('DOMContentLoaded', () => {
  const navSelection = document.querySelector('.nav-selection');

  navSelection.addEventListener('click', (event) => {
    const target = event.target;
    console.log(target.classList.contains('nav-selection--active'))
    console.log(target.classList.contains('nav-selection--inactive'))
    if (target.classList.contains('nav-selection--inactive')) {
      const active = navSelection.querySelector('.nav-selection--active');
      active.classList.replace('nav-selection--active', 'nav-selection--inactive');
      target.classList.replace('nav-selection--inactive', 'nav-selection--active');
    }
  });
});

main()