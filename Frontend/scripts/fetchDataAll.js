export default async function fetchDataAll(url, headers, method = "GET", datos = null) {
  console.log("aqui_funcion_parametros", url, headers, method, datos);

  try {
      const response = await fetch(url, {
          headers: headers,
          method: method,
          body: datos ? JSON.stringify(datos) : null
      })
        console.log("aqui_esponse_dentro_funcion", response)

      if (!response.ok) {
          throw new Error('Error en la solicitud');
      }

      const data = await response.json();
      console.log("aqui_data-dentro_funcion", data);
      return data;
  } catch (error) {
      console.error('Error:', error);
      return null;
  }
}
