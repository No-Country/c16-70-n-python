import obtenerDatosAPIUserProfile from './fetchDataUserProfile.js';
import renderUserProfile from './renderUserProfile.js';

console.log("aqui_id", sessionStorage.getItem("userid"))
const userId = sessionStorage.getItem("userid");
function main() {
    console.log("aqui_id", userId)
  obtenerDatosAPIUserProfile(userId)
    .then(datos => {
      renderUserProfile(datos);
    })
    .catch(error => console.error('Error:', error));
}
main()