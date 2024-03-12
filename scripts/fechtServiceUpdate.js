import fetchDataAll from "./fetchDataAll.js";
import { apiUrlServer } from '../js/config.js';
// actuazado 030324-0234pm

export const updateService = (id,text) => {
    const data = {name : text}
    const Url = apiUrlServer + `admin/servicios/` + id
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