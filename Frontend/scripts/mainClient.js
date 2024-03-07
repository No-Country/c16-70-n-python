import {obtenerTurnosClientAPI} from "./fetchTurnClientActive.js";
import {renderCardsTurnActive} from "./renderCardsTurnActive.js";
import {obtenerTurnosHistoryClientAPI} from "./fetchTurnClientActive.js";
import {renderCardsTurnInactive} from "./renderCardsTurnActive.js";

function main() {
  obtenerTurnosClientAPI()
  .then(datos => {
    renderCardsTurnActive(datos);
  })
  .catch(error => console.error('Error:', error));
}

function main2() {
  obtenerTurnosHistoryClientAPI()
  .then(datos => {
    renderCardsTurnInactive(datos);
  })
  .catch(error => console.error('Error:', error));
}


main()
main2()