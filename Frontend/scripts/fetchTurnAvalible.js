import fetchDataAll from "./fetchDataAll.js";
// import {renderUserCards} from './renderList.js';
// import {obtenerDatosAPI} from './fetchData.js';
import { apiUrlServer } from '../js/config.js';


export default async function obtenerTurnosAPI() {
    const apiUrl = apiUrlServer + 'user/turnos';

    const headers = {
        'Authorization': 'Bearer ' + sessionStorage.getItem('token'),
        'Content-Type': 'application/json',  
         
    }
    let datos
    const data = await fetchDataAll(apiUrl, headers)
        .then(data => {
            datos= data;
        })
        .catch(error => {
            console.error('Error:', error);
        })
    console.log("constate_datos:",datos)
    return datos

    }