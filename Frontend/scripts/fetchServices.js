import fetchDataAll from "./fetchDataAll.js";
// import {renderUserCards} from './renderList.js';
// import {obtenerDatosAPI} from './fetchData.js';
import { apiUrlServer } from '../js/config.js';


export default async function obtenerServiciosAPI() {
    const apiUrl = apiUrlServer + 'admin/servicios?page=1';

    const headers = {
        'Authorization': 'Bearer ' + sessionStorage.getItem('token'),
        'Content-Type': 'application/json',  
         
    }

    return fetchDataAll(apiUrl, headers)
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        })

    }