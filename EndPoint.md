# Referencia a los EndPoint

(se necesita actualizar)

## Login

- POST ( recibe los datos y debe enviar un respuesta y el tipo de Rol que es el usuario)

## Registro

- POST (recibe los datos, comprueba si no existe el usuario si no existe, genera un token que pueda almacenar el tipo de rol, escribe en la base data recordar que la password debe ser cifrada )

## Datos

Para consumir estos endpoint necesita una autorizacion
asi determina que tipo de Rol es el usuario,evitar a que los usuarios puedan ingresar con datos falsos .

Nota: debe existir algun modulo que crea id cifradas , no es obligatorio pero si recomendado.

- GET ( si este endpoint recibe algun datos de autorizacion entonces puede llegar a ser POST )

- PUT ( Posibilidad de Acualizar datos)

- DELETE ( Borrar cuenta )

## Registro Poveedor

- GET ( puede consultar estos Datos)
- POST ( EL proveedor debe registrar el tipo de servicio)
- PUT ( Debe tener la posibilidad de modificar estos datos)
- DELETE ( Puede Eliminar si Realizo un Mal Registro de servicio)

## Solicitud de Cita (Cliente)

- GET  (los cliente podran ver sus citas)
- POST (los usuarios pueden crear sus citas)
- PUT  (los usuarios pueden actualiza, siempre y cuando este disponible el servicio, date[fecha deberia de ser unica] ).
- DELETE (Borrar Cita).
