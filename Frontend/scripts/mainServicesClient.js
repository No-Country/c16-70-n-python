import obtenerServiciosAPI from "./fetchServices.js";
import renderCardsService from "./renderCardServicesClient.js"

function main() {
  obtenerServiciosAPI()
  .then(datos => {
    renderCardsService(datos);
  })
  .catch(error => console.error('Error:', error));
}


main()