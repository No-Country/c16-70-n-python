import { apiUrlServer } from "../js/config.js";

const form = document.querySelector('.form-update-user');
form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const id = sessionStorage.getItem('userid');
    console.log("identificador",id)
    const auth = sessionStorage.getItem('token');
    const data = {
        firtname: form['first-name'].value,
        lastname: form['last-name'].value,
        // email: form['email'].value,
        // phone: form['phone'].value,
        // status: form['status'].value,
        // dateIncription: form['date-incription'].value,
        // dateSuspension: form['date-suspension'].value
        
    };
    console.log("aqui_data",data)

    const response = await fetch(apiUrlServer + `admin/paciente/10`, {
        method: 'PUT',
        headers: {
            'Authorization': auth,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
        mode: 'cors',
        cache: 'default'
    });
    console.log("aqui_response",response)

    if (response.ok) {
        const json = await response.json();
        console.log(json);
    } else {
        const json = await response.json();
        console.error(json);
    }
});

