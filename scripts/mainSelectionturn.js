import obtenerTurnosAPI from "./fetchTurnAvalible.js";
import renderCardsTurn from "./renderCardTurn.js"

function main() {
  obtenerTurnosAPI()
  .then(datos => {
    renderCardsTurn(datos);
  })
  .catch(error => console.error('Error:', error));
}


main()