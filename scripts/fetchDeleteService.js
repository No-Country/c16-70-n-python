import fetchDataAll from "./fetchDataAll.js";
// import {renderUserCards} from './renderList.js';
// import {obtenerDatosAPI} from './fetchData.js';
import { apiUrlServer } from '../js/config.js';


export default async function deleteServicesAPI(id) {
    console.log("aqui", id)
    const apiUrl = apiUrlServer + 'admin/servicios/' + id;

    const headers = {
        'Authorization': 'Bearer ' + sessionStorage.getItem('token'),
        'Content-Type': 'application/json',  
        mode : 'cors',
         
    }
    let datos
    const data = await fetchDataAll(apiUrl, headers, "DELETE")
        .then(data => {
            datos= data;
        })
        .catch(error => {
            console.error('Error:', error);
        })
    console.log("constate_datos:",datos)
    // console.log(datos.type)
    return datos

    }