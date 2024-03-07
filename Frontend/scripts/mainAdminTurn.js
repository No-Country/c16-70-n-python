import obtenerTurnosAssignedAPI from './fetchTurnAssigned.js';
import {renderCardsTurnAssigned} from './renderCardsTurnAssigned.js';
function main() {
    obtenerTurnosAssignedAPI()
    .then(datos => {
      renderCardsTurnAssigned(datos);
    })
    .catch(error => console.error('Error:', error));
  }

  main()