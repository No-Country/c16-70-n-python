import { apiUrlServer } from "../js/config.js";

export default async function obtenerDatosAPI(page, role="") {
  const apiUrl = apiUrlServer + `/admin/pacientes?role=${role}&_page=${page}`;
  //console.log("aqui", apiUrl);
  
  try {
    const token = sessionStorage.getItem("token"); 
      //console.log("aqui token",token);// Obtener el token del almacenamiento local
      const headers = {
          'Authorization': `Bearer ${token}` // Formatear el token como "Bearer token"
      };

      const response = await fetch(apiUrl, {
          headers: headers // Agregar los encabezados a la solicitud fetch
      });

      if (!response.ok) {
          throw new Error('Error en la solicitud');
      }

      const data = await response.json();
    //   console.log("aqui", data);
      return data;
  } catch (error) {
      console.error('Error:', error);
      return null; // Manejo de errores
  }
}

