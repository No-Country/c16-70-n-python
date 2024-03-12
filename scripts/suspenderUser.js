import { apiUrlServer } from "../js/config.js";

export async function updateSuspensionRecord(id) {
    const updateSuspensionData = {
        data_suspension: '2023-05-01'
    }

    const token = sessionStorage.getItem("token");

    if (!token) {
        window.location.href = "/frontend/";
        return;
    }
//     const myHeaders = new Headers();
//   myHeaders.append("Content-Type", "application/json");

    var myHeaders = new Headers();
    myHeaders.append("Authorization", "Bearer " + token);
    myHeaders.append("Content-Type", "application/json");
  
    var requestOptions = {
        method: 'PUT',
        headers: myHeaders,
        body: JSON.stringify(updateSuspensionData),
        redirect: 'follow'
    };

    const url = apiUrlServer + `/admin/paciente/${id}`;

    await fetch(url, requestOptions)
        .then(res => res.json())
        .then(data => {
            console.log('Actualizado con éxito', data);
        })
        .catch(error => {
            console.error('Error al actualizar', error);
        });
}// ! la funcion se ejecuta cuando se hace click en el boton de suspender pero no actualiza la base de datos



