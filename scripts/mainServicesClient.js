import obtenerServiciosClientAPI from "./fetchServiceClient.js";
import renderCardsService from "./renderCardServicesClient.js"

function main() {
  obtenerServiciosClientAPI()
  .then(datos => {
    renderCardsService(datos);
  })
  .catch(error => console.error('Error:', error));
}


main()