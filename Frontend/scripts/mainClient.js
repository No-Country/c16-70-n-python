import obtenerTurnosClientAPI from "./fetchTurnClientActive.js";
import renderCardsTurnActive from "./renderCardsTurnActive.js";

function main() {
  obtenerTurnosClientAPI()
  .then(datos => {
    renderCardsTurnActive(datos);
  })
  .catch(error => console.error('Error:', error));
}


main()