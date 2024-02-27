function cleanUserCards() {
    const container = document.getElementById('table-container');
    let child = container.lastElementChild;
    while (child !== document.getElementById('table-person-template')) {
      container.removeChild(child);
      child = container.lastElementChild;
    }
  }
  export default function renderUserCards(data) {
    cleanUserCards();
    const container = document.getElementById('table-container');
    const template = document.getElementById('table-person-template').content;
    const paginationPrev = document.getElementById('pagination-prev');
    const paginationNext = document.getElementById('pagination-next');
    
    data.forEach(user => {
      const userCard = document.importNode(template, true);
      if (user.profileImgUrl == undefined) {
          userCard.querySelector('.user img').src = 'images/profile_8.jpg';
      } else {
          userCard.querySelector('.user img').src = user.profileImgUrl;
      }
      userCard.querySelector('.user-info strong').textContent = user.firt_name + " " + user.last_name;
      userCard.querySelector('.user-info small').textContent = user.email;
      userCard.querySelector('.role p').textContent = user.role;
      userCard.querySelector('.count-type p').textContent = user.accountType;
      userCard.querySelector('.status p').textContent = user.status;
      userCard.querySelector('.date-incription p').textContent = user.registrationDate;
      container.appendChild(userCard);
    });
    paginationPrev.classList.toggle('hidden', data.prev <= 0);
    paginationNext.classList.toggle('hidden', data.next == null);
  }