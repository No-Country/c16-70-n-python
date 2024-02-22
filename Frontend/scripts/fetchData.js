export default async function obtenerDatosAPI(page, limit, role="") {
    const apiUrl = `http://localhost:3000/users?role=${role}&_page=${page}&_per_page=${limit}`;
    
    
  
    try {
      const response = await fetch(apiUrl);
      const data = await response.json();
      console.log("aqui",data);
      return data;
    } catch (error) {
      return console.error('Error:', error);
    }
  }

