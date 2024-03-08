import obtenerDatosAPIUserProfileForAdmin from './fetchDataUserProfileForAdmin.js';
import renderUserProfile from './renderUserProfileAdmin.js';

console.log("aqui_id", sessionStorage.getItem("userid"))
const userId = sessionStorage.getItem("userid");
function main() {
    console.log("aqui_id", userId)
  obtenerDatosAPIUserProfileForAdmin(userId)
    .then(datos => {
      renderUserProfile(datos);
    })
    .catch(error => console.error('Error:', error));
}
main()