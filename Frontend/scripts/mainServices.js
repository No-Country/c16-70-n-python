import obtenerServiciosAPI from "./fetchServices.js";
import renderCardsService from "./renderCardsServices.js"
import deleteServices from './deleteServices.js';
function main() {
  obtenerServiciosAPI()
  .then(datos => {
    renderCardsService(datos);
  })
  .catch(error => console.error('Error:', error));
}


main()