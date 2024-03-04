import obtenerDatosAPIClientProfile from '././fetchDataClientProfile.js';
import renderUserProfile from './renderUserProfile.js';

console.log("aqui_id", sessionStorage.getItem("userid"))
const userId = sessionStorage.getItem("userid");
function main() {
    console.log("aqui_id", userId)
  obtenerDatosAPIClientProfile(userId)
    .then(datos => {
      renderUserProfile(datos);
    })
    .catch(error => console.error('Error:', error));
}
main()