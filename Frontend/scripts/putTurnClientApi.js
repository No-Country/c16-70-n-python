import fetchDataAll from "./fetchDataAll.js";
// import {renderUserCards} from './renderList.js';
// import {obtenerDatosAPI} from './fetchData.js';
import { apiUrlServer } from '../js/config.js';


export const putTurnClient = () => {
    const data = {
        id_servicio : sessionStorage.getItem('service_id'),
        descriptionturn: sessionStorage.getItem('service_description')
    }
    const Url = apiUrlServer + `/user/turno/asignar/` + sessionStorage.getItem('turn_id');
    const headers = {
    'Authorization': 'Bearer ' + sessionStorage.getItem('token'),
    'Content-Type': 'application/json', 
}

return fetchDataAll(Url, headers, "PUT", data)
.then((data) => {
    console.log("aqui_data_fetch",data)
    })
    .catch(error => {
        console.error('Error:', error);
    })
}