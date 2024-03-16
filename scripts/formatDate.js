export default function formatearFecha(fechaISO) {
    if (fechaISO == null){
      return "Paciente Activo"
    }
    var fecha = new Date(fechaISO);
    var dia = fecha.getDate();
    var mes = fecha.getMonth() + 1;
    var año = fecha.getFullYear();
    return dia + ' ' + obtenerNombreMes(mes) + ' ' + año;
  }
  
  // Función para obtener el nombre del mes
  function obtenerNombreMes(numeroMes) {
    var meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ];
    return meses[numeroMes - 1];
  }