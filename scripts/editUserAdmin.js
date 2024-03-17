import { apiUrlServer } from "../js/config.js";
import fetchDataAll from "./fetchDataAll.js";
import obtenerDatosAPIUserProfileForAdmin from "./fetchDataUserProfileForAdmin.js";


document.addEventListener('DOMContentLoaded', () => {
    console.log("aqui");
    obtenerDatosAPIUserProfileForAdmin(sessionStorage.getItem("userid")).then(datos => {
        console.log("date-get", datos)
        document.getElementById('first-name').value = datos.first_name;
        document.getElementById('last-name').value = datos.last_name;
        document.getElementById('email').value = datos.email;
        document.getElementById('phone').value = datos.phone;
        // document.getElementById('status').value = data.status;
        // document.getElementById('date-incription').value = data.register_date;
        // document.getElementById('date-suspension').value = data.data_suspension;

    })
})


const form = document.querySelector('.form-update-user');
form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const data = {
        firtname: form['first-name'].value,
        lastname: form['last-name'].value,
        email: form.email.value,
        phone: form.phone.value,
    };
    
    // const data = {
    //     firt_name: document.getElementById('first-name').value =,
    //     last_name: document.getElementById('last-name').value,
    //     email: document.getElementById('email').value,
    //     phone: document.getElementById('phone').value,
        // status: document.getElementById('status').value,
        // dateIncription: document.getElementById('date-incription').value,
        // dateSuspension: document.getElementById('date-suspension').value
    //}
    
    console.log("aqui_form_data|",data)
    
    const Url = apiUrlServer + `/admin/paciente/` + sessionStorage.getItem('userid');
    //const Url = apiUrlServer + `user/put`;

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
    }).then(() => {
         window.location.href = "../admin-panel/admin-panel-detail-user.html"
        // console.log("aqui_data-despues", data)
    })
    
})

// fetchDataAll(endpoint, headers, "PUT", formData)
//   .then(data => {
//     console.log('Usuario actualizado:', data) 
//   })
//   .catch(err => {
//     console.error('Error al actualizar', err)
//   })


