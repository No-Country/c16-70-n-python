### Administración
- panel_administrador_principal 
  - [x] Mostrar lista de todos los clientes
  - [x] Mostrar lista de todos los turnos
  - [x] Crear paginacion para lista de clientes y turnos
  - [x] Crear botones para seleccionar que lista se muestra(clientes, turnos)
  - [x] agregar botón borrar en cada elemento de la lista de clientes
  - [x] agregar botón borrar en cada elemento de la lista de turnos
  - [ ] agregar funcionabilidad a botón borrar para borrar elementos de la lista (clientes,  turnos)
  - [x] agregar botón actualizar a cada elemento de la lista (opcion extra) 
      
-  panel_administrador_gestión_perfil
   - [ ] agregar funcionalidad para visualizar datos de usuario 
   - [ ] mostrar lista de turnos del usuario
   - [ ] agregar funcionalidad para suspender cliente
       
- panel_administrador_gestionar_servicios
   - [ ] mostrar una lista con todos los servicios
   - [ ] mostrar boton para crear nuevo servicio y redireccionar a panel_administrador_crear_servicio
        
- panel_administrador_crear_servicio
   - [ ] crear formulario para crear nuevo servicio
   - [ ] agregar funcionalidad para enviar datos al servidor

- panel_administrador_gestionar_servicio
   - [ ] mostrar lista de servicios
   - [ ] mostrar boton modificar servicio que redirecciona a panel_administrador_modificar_servicio

- panel_administrador_modificar_servicio
   - [ ] mostrar datos de servicio
   - [ ] agregar funcionalidad de borrar o actualizar servicio  

### Cliente
- panel_cliente_principal
   - [ ] mostrar lista de turnos del cliente (los más próximos)
   - [ ] agregar funcionalidad para que al hacer click sobre boton detalles del turno se redireccione a panel_cliente_gestión_turno
   - [ ] mostrar botón para redireccionar a panel_cliente_gestión_turnos
   - [ ] mostrar nombre de cliente en la parte superior izquierda con foto de perfill
   - [ ] mostrar botón cerrar sesión
   - [ ] agregar funcionalidad a botón cerrar sesión para cerrar sesión de cliente
   - [ ] agregar boton seleccionar un turno y redirecionar a panel_servicios_principal
   
 - panel_cliente_gestion_perfil
   - [ ] mostrar todos los datos del cliente
   - [ ] Mostra botón editar perfil
   - [ ] agregar funcionalidad al botón editar perfil para permitir al usuario modificar sus datos
   - [ ] mostrar botón actualizar para enviar los datos al servidor
   - [ ] agregar funcionalidad para que botón actualizar envié los datos actualizados al servidor
   - [ ] Mostrar botón suspender cuenta
   - [ ] agregar funcionalidad para mostrar un mensaje. Está seguro que desea suspender su cuenta?
   - [ ] agregar funcionalidad para que al aceptar el mensaje la cuenta sea colocada en estado de suspención y el login y el usuario no sean validos
    
 - panel_cliente_gestion_turno
    - [ ] mostrar detalles del turno
    - [ ] agregar botón abandonar_turno
    - [ ] agregar funcionalidad a botón abandonar_turno para que muestre un mensaje. Está seguro de abandonar este turno
    - [ ] agregar funcionalidad para que al aceptar el mensaje el turno cambie de tomado a disponible y dejé la lista de turnos del cliente.
    
  - panel_cliente_gestion_turnos
    - [ ] mostrar una lista con todos los turnos del cliente
    - [ ] agregar funcionalidad para que al hacer click sobre ver mas en un turno se redireccione a panel_cliente_gestion_turno
    - [ ] agregar botón activos
    - [ ] agregar botón terminados
    - [ ] agregar funcionalidad al botón activos para mostrar todos los turnos activos
    - [ ] agregar funcionalidad al botón terminados para mostrar todos los turnos terminados
    - [ ] agregar paginación a la lista de todos los turnos
    - [ ] agregar paginación a la lista de turnos activos
    - [ ] agregar paginación a la lista de turnos terminados

### servicio
  - panel_servicio_principal
    - [ ] mostrar lista de servicios principales
    - [ ] agregar boton selecionar turno a cada servicio
    - [ ] agregar funcionalidad a boton seleccionar turno para redireccionar a Panel_turno_principal

### turno
  - panel_turno_principal
    - [ ] mostrar calendario con turnos disponibles y tomados
    - [ ] agregar funcionalidad para que se agrege turno al cliente
    
### Endpoints de la API

- `/api/clientes`
  - GET: Obtener lista de clientes

- `/api/clientes/<id>`
  - GET: Obtener detalles de un cliente
  - PUT: Actualizar información de un cliente
  - DELETE: Eliminar un cliente

- `/api/turnos`
  - GET: Obtener lista de turnos
  - POST: Crear un nuevo turno

- `/api/turnos/<id>`
  - GET: Obtener detalles de un turno
  - PUT: Actualizar información de un turno
  - DELETE: Eliminar un turno

- `/api/servicio`
  - GET: Obtener lista de servicios
  - POST: Crear un nuevo servicio

