import { apiUrlServer } from "../js/config.js";
import fetchDataAll from "./fetchDataAll.js";
import obtenerDatosAPIUserProfile from "./fetchDataUserProfile.js";

window.onload = () => {
    obtenerDatosAPIUserProfile().
    then(data => {
        document.getElementById('first-name').value = data.firt_name;
        document.getElementById('last-name').value = data.last_name;
        document.getElementById('email').value = data.email;
        document.getElementById('phone').value = data.phone;
        
    })
}

const form = document.querySelector('.form-update-user');
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const data = {
        firtname: document.getElementById('first-name').value,
        lastname: document.getElementById('last-name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        // status: document.getElementById('status').value,
        // dateIncription: document.getElementById('date-incription').value,
        // dateSuspension: document.getElementById('date-suspension').value
    }
    
    console.log("aqui_form_data|",data)
    
    // const Url = apiUrlServer + `/admin/paciente/` + sessionStorage.getItem('userid');
    const Url = apiUrlServer + `user/put`;

const headers = {
    'Authorization': 'Bearer ' + sessionStorage.getItem('token'),
    'Content-Type': 'application/json',
    
}

fetchDataAll(Url, headers, "PUT", data)
.then((data) => {
    console.log("aqui_data_fetch",data)
    })
    .catch(error => {
        console.error('Error:', error);
    })
    
})

// fetchDataAll(endpoint, headers, "PUT", formData)
//   .then(data => {
//     console.log('Usuario actualizado:', data) 
//   })
//   .catch(err => {
//     console.error('Error al actualizar', err)
//   })


