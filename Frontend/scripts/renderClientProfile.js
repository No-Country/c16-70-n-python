function cleanUserCards() {
    const container = document.getElementById('table-container');
    let child = container.lastElementChild;
    while (child !== document.getElementById('table-person-template')) {
      container.removeChild(child);
      child = container.lastElementChild;
    }
  }
  export default function renderClienteProfile(data) {
    cleanUserCards();
    const container = document.getElementById('table-container');
    const template = document.getElementById('table-person-template').content;
    console.log("data_user",data)
    
    
      const userCard = document.importNode(template, true);
      if (data.profileImgUrl == undefined) {
          userCard.querySelector('.user img').src = 'images/profile_8.jpg';
      } else {
          userCard.querySelector('.user img').src = data.profileImgUrl;
      }
      userCard.querySelector('.user-name p').textContent = data.firt_name + " " + data.last_name;
      userCard.querySelector('.user-email p').textContent = data.email;
      userCard.querySelector('.phone-number p').textContent = data.phone;
      
      
      userCard.querySelector('.date-incription p').textContent = data.data_reister;
      userCard.querySelector('.date-suspension p').textContent = data.data_suspension
      ;
      container.appendChild(userCard);

      
      
  }
