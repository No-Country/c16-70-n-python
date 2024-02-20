### Administración
- panel administrador principal 
  - [x] Mostrar lista de todos los usuarios
  - [ ] Mostrar lista de todos los clientes
  - [ ] Mostrar lista de todos los proveedores
  - [x] Crear paginacion para lista de todos
  - [x] Crear botones para seleccionar que lista se muestra(todos, clientes, proveedores)
  - [ ] crear paginacion para lista de clientes
  - [ ] crear paginacion para lista de proveedores 
  - [x] agregar botón borrar en cada elemento de la lista
  - [ ] agregar funcionabilidad a botón borrar para borrar elemento de la lista
  - [x] agregar botón actualizar a cada elemento de la lista
  - [ ] agregar funcionabilidad a botón actualizar para redirigir a pantalla de gestión de perfil con los datos del usuario seleccionado 
  - [x] agregar responsividad
  - extra
    - buscador indexado y filtros
-  panel administrador gestión de perfil
   - [ ] agregar funcionalidad para editar usuario
   - [ ] agregar funcionalidad para borrar usuario 
   - [ ] mostrar datos del usuario seleccionado (foto de perfil, nombre, ...)
   - [ ] agregar responsividad 
   - extra
     - mostrar lista de turnos del usuario (si es cliente o proveedor)

### Cliente
- panel_cliente_principal
   - [ ] mostrar lista de turnos del cliente (los más próximos)
   - [ ] agregar funcionalidad para que al hacer click sobre el turno se redireccione a panel_cliente_gestión_turno
   - [ ] mostrar botón para redireccionar a panel_cliente_gestión_turnos
   - [ ] mostrar nombre de cliente en la parte superior izquierda con foto de perfill
   - [ ] mostrar botón cerrar sesión
   - [ ] agregar funcionalidad a botón cerrar sesión para cerrar sesión de cliente
   - [ ] mostrar lista de proveedores destacados 
   - [ ] agregar funcionalidad para que al hacer click sobre un proveedor se redireccione al panel_cliente_detalle_proveedor 
   - [ ] mostrar botón para redireccionar panel_cliente_seleccionar_proveedor 
   
 - panel_cliente_gestion_perfil
   - [ ] mostrar todos los datos del cliente
   - [ ] Mostra botón editar perfil
   - [ ] agregar funcionalidad al botón editar perfil para permitir al usuario modificar sus datos
   - [ ] mostrar botón actualizar
   - [ ] agregar funcionalidad para que botón actualizar envié los datos actualizados al servidor
   - [ ] Mostrarbotón suspender cuenta
   - [ ] agregar funcionalidad para mostrar un mensaje. Está seguro que desea suspender su cuenta?
   - [ ] agregar funcionalidad para que al aceptar el mensaje la cuenta sea colocada en estado de suspención y el login y el usuario no sean validos
   
-  panel_cliente_seleccionar_proveedor
   - [ ] mostrar lista para seleccionar servicio 
   - [ ] agregar funcionalidad para mostrar proveedores según servicio 
   - [ ] mostrar botón todos
   - [ ] agregar funcionabilidad para que al hacer click sobre botón todos se muestren todos los proveedores
   - [ ] agregar paginación a lista de todos los proveedores
   - [ ] agregar paginación a lista de proveedores según el servicio seleccionado 
   - [ ] agregar funcionalidad para al hacer click sobre un proveedor se redireccione a panel_cliente_detalle_proveedor
   
- panel_cliente_detalle_proveedor
    - [ ] mostrar detalles de proveedor
    - [ ] mostrar lista de turnos disponibles del proveedor
    - [ ] agregar botón detalle a cada turno en la lista
    - [ ] agregar botón tomar_turno a cada turno
    - [ ] agregar funcionalidad a botón detalle para que muestre en un popoup los detalles del turno
    - [ ] agregar funcionalidad al botón tomar_turno para mostrar un mensaje. Está seguro de tomar este turno
    - [ ] agregar funcionalidad para que al aceptar el turno se añada a los turnos del cliente y cambie su estado de disponible a tomado.
    
 - panel_cliente_gestion_turno
    - [ ] mostrar detalles del turno
    - [ ] agregar botón abandonar_turno
    - [ ] agregar funcionalidad a botón abandonar_turno para que muestre un mensaje. Está seguro de abandonar este turno
    - [ ] agregar funcionalidad para que al aceptar el mensaje el turno cambie de tomado a disponible y dejé la lista de turnos del cliente.
    
  - panel_cliente_gestion_turnos
    - [ ] mostrar una lista con todos los turnos del cliente
    - [ ] agregar funcionalidad para que al hacer click sobre un turno se redireccione a panel_cliente_gestion_turno
    - [ ] agregar botón activos
    - [ ] agregar botón terminados
    - [ ] agregar funcionalidad al botón activos para mostrar todos los turnos activos
    - [ ] agregar funcionalidad al botón terminados para mostrar todos los turnos terminados
    - [ ] agregar paginación a la lista de todos los turnos
    - [ ] agregar paginación a la lista de turnos activos
    - [ ] agregar paginación a la lista de turnos terminados
    
### Proveedor

- panel_proveedor_principal
  - [ ] Mostrar cantidad de turnos tomados y disponibles
  - [ ] Mostrar botón para crear nuevo turno
  - [ ] Agregar funcionalidad para que al hacer clic en el botón "crear nuevo turno" se redirija al panel_proveedor_gestion_turnos

- panel_proveedor_gestion_perfil
  - [ ] Mostrar información del proveedor (nombre, servicios, calificación, etc.)
  - [ ] Agregar botón para editar información del perfil
  - [ ] Agregar funcionalidad para actualizar la información del perfil

- panel_proveedor_gestion_turno
  - [ ] Agregar botón para marcar turno como completado
  - [ ] Agregar funcionalidad para que al marcar un turno como completado, se actualice el estado del turno y se registre en el historial del proveedor

- panel_proveedor_gestion_turnos
  - [ ] Mostrar lista de turnos disponibles
  - [ ] Agregar botón para crear nuevo turno
  - [ ] Agregar funcionalidad para crear un nuevo turno (fecha, hora, servicio, etc.)
  - [ ] Agregar paginación a la lista de turnos disponibles

- panel_proveedor_gestion_ubicaciones
  - [ ] Mostrar lista de ubicaciones registradas
  - [ ] Agregar botón para registrar nueva ubicación
  - [ ] Agregar funcionalidad para registrar una nueva ubicación

- panel_proveedor_gestion_ubicacion
  - [ ] Mostrar detalles de la ubicación seleccionada
  - [ ] Agregar botón para editar información de la ubicación
  - [ ] Agregar funcionalidad para actualizar la información de la ubicación

### Endpoints de la API

- `/api/clientes`
  - GET: Obtener lista de clientes

- `/api/clientes/<id>`
  - GET: Obtener detalles de un cliente
  - PUT: Actualizar información de un cliente
  - DELETE: Eliminar un cliente

- `/api/proveedores`
  - GET: Obtener lista de proveedores

- `/api/proveedores/<id>`
  - GET: Obtener detalles de un proveedor
  - PUT: Actualizar información de un proveedor
  - DELETE: Eliminar un proveedor

- `/api/turnos`
  - GET: Obtener lista de turnos
  - POST: Crear un nuevo turno

- `/api/turnos/<id>`
  - GET: Obtener detalles de un turno
  - PUT: Actualizar información de un turno
  - DELETE: Eliminar un turno

- `/api/categorías`
  - GET: Obtener lista de servicios
  - POST: Crear un nuevo servicio

- `/api/ubicaciones`
  - GET: Obtener lista de ubicaciones
  - POST: Crear una nueva ubicación

- `/api/ubicaciones/<id>`
  - GET: Obtener detalles de una ubicación
  - PUT: Actualizar información de una ubicación
  - DELETE: Eliminar una ubicación