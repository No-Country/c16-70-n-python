import obtenerDatosAPI from "./fetchData.js";
import renderUserCards from './renderList.js';
import stateRole from "./selectionObjetState.js";
//switch between active and inactive
export default function switchActiveInactive() {
  document.addEventListener('DOMContentLoaded', () => {
    const navSelection = document.querySelector('.nav-selection');
    navSelection.addEventListener('click', (event) => {
      const target = event.target;
      if (target.classList.contains('nav-selection--inactive')) {
        const active = navSelection.querySelector('.nav-selection--active');
        active.classList.replace('nav-selection--active', 'nav-selection--inactive');
        target.classList.replace('nav-selection--inactive', 'nav-selection--active');
        console.log(target.textContent);
        if (target.textContent === 'Clientes') {
          stateRole.role = "cliente";
          obtenerDatosAPI(1, 10, "cliente").then(data =>{renderUserCards(data)});
        }
        if (target.textContent === 'Proveedores') {
          stateRole.role = "proveedor";
          obtenerDatosAPI(1, "proveedor").then(data =>{renderUserCards(data)});
        }
        if (target.textContent === 'Todos') {
          stateRole.role = "";
          obtenerDatosAPI(1, 10).then(data =>{renderUserCards(data)});
        }
      }
    });
  });
}
