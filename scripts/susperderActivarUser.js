import { apiUrlServer } from "../js/config.js";
import fetchDataAll from "./fetchDataAll.js";

export const suspenderUsuario = () => {
    const data = {suspender : "True"}
    const Url = apiUrlServer + `/admin/paciente/` + sessionStorage.getItem('userid');
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

export const activarUsuario = () => {
    console.log("aqui_click_suspender")  
    const data = {suspender : "False"}   
    console.log("aqui_form_data|",data)
    const Url = apiUrlServer + `/admin/paciente/` + sessionStorage.getItem('userid');

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



