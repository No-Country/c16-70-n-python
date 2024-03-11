import fetchDataAll from "./fetchDataAll.js";
// import {renderUserCards} from './renderList.js';
// import {obtenerDatosAPI} from './fetchData.js';
import { apiUrlServer } from '../js/config.js';


const form = document.getElementById('form-add-service');
const messageContainer = document.getElementById('message-container');
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

    //fetchDataAll(apiUrl, headers, "POST", data)

    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error('Error en la solicitud');
        }

        const responseData = await response.json();
        console.log(responseData);
        console.log(responseData.message);
        console.log(responseData.status);

        if (responseData) {
            messageContainer.textContent = responseData.message;
        }

        //location.reload();
    } catch (error) {
        console.error('Error:', error);
    }
});