// export default async function obtenerDatosAPI(page, limit, role="") {
//     const apiUrl = `http://localhost:5000/admin/pacientes?role=${role}&_page=${page}`;
    
  
//     try {
//       const response = await fetch(apiUrl);
//       const data = await response.json();
//       console.log("aqui",data);
//       return data;
//     } catch (error) {
//       return console.error('Error:', error);
//     }
//   }

export default async function obtenerDatosAPI(page, limit, role="") {
  const apiUrl = `http://localhost:5000/admin/pacientes?role=${role}&_page=${page}`;
  
  try {
      // const token = sessionStorage.getItem("token"); 
      const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwicm9sZSI6IkFkbWluIiwiZXhwIjoxNzA4OTU2NzAzfQ.U_ziqSAes0kgqQyl96Jc3ClOmp6wPDPBFc0Vwsps7fY"
      console.log("aqui token",token);// Obtener el token del almacenamiento local
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
      console.log("aqui", data);
      return data;
  } catch (error) {
      console.error('Error:', error);
      return null; // Manejo de errores
  }
}
