import fetchDataAll from "./fetchDataAll.js";
// import {renderUserCards} from './renderList.js';
// import {obtenerDatosAPI} from './fetchData.js';
import { apiUrlServer } from '../js/config.js';


const form = document.getElementById('form-add-service');
form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const data = {
        name: document.getElementById('name').value,
    }

    const apiUrl = apiUrlServer + 'admin/servicios';


    const headers = {
        'Authorization': 'Bearer ' + sessionStorage.getItem('token'),
        'Content-Type': 'application/json',

    }


    fetchDataAll(apiUrl, headers, "POST", data)
        .then(data => {
                console.log(data);
                console.log(data.message);
                console.log(data.status);
                if (data) {
                    alert(data.message);
                }
                location.reload();
        })
        .catch(error => {
            console.error('Error:', error);
        })
})




    