import obtenerTurnosAssignedAPI from './fetchTurnAssigned.js';
import {renderCardsTurnAssigned} from './renderCardsTurnAssigned.js';
import switchActiveInactive from './botonSelectionList.js';
function main() {
    obtenerTurnosAssignedAPI()
    .then(datos => {
      renderCardsTurnAssigned(datos);
    })
    .catch(error => console.error('Error:', error));
  }

  switchActiveInactive()
  main()