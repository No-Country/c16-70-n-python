# Agendify

## Documentación de Módulos para Proyecto Agendify

### 1. aniso8601==9.0.1
- **Función**: Este módulo proporciona funcionalidades para analizar y manipular fechas y tiempos en formato ISO 8601.
  
### 2. attrs==23.1.0
- **Función**: `attrs` es una librería para definir atributos fuertemente tipados en clases de Python, simplificando el manejo de atributos y la inicialización de objetos.

### 3. blinker==1.7.0
- **Función**: `blinker` implementa un sistema de señales (signals) para Python, permitiendo a los objetos comunicarse de manera débilmente acoplada.

### 4. click==8.1.7
- **Función**: `click` es una biblioteca para crear interfaces de línea de comandos con un enfoque en la legibilidad y la simplicidad.

### 5. Flask==2.3.3
- **Función**: Flask es un framework web ligero para Python que facilita la creación de aplicaciones web rápidas y flexibles.

### 6. flask-restx==1.2.0
- **Función**: `flask-restx` es una extensión de Flask que agrega soporte para la creación rápida de APIs RESTful con documentación automática.

### 7. Flask-SQLAlchemy==3.1.1
- **Función**: `Flask-SQLAlchemy` integra la funcionalidad del ORM SQLAlchemy en aplicaciones Flask, facilitando la interacción con bases de datos relacionales.

### 8. greenlet==3.0.1
- **Función**: `greenlet` es una biblioteca que proporciona concurrencia ligera para Python, permitiendo la ejecución de múltiples funciones de forma concurrente.

### 9. importlib-resources==6.1.1
- **Función**: `importlib-resources` proporciona utilidades para trabajar con recursos embebidos en paquetes Python, permitiendo el acceso a archivos y datos dentro de paquetes.

### 10. itsdangerous==2.1.2
- **Función**: `itsdangerous` proporciona herramientas para manejar la seguridad de datos en Flask, como la firma y la verificación de tokens.

### 11. Jinja2==3.1.2
- **Función**: `Jinja2` es un motor de plantillas para Python que permite la creación de contenido dinámico en aplicaciones web Flask.

### 12. jsonschema==4.17.3
- **Función**: `jsonschema` es una biblioteca para validar esquemas de JSON, útil para validar datos recibidos en solicitudes HTTP en APIs RESTful.

### 13. MarkupSafe==2.1.3
- **Función**: `MarkupSafe` es una biblioteca que proporciona funcionalidades para escapar y marcar texto seguro contra ataques XSS en aplicaciones web Flask.

### 14. PyJWT==2.8.0
- **Función**: `PyJWT` permite codificar y decodificar JSON Web Tokens (JWT), utilizados para autenticación en APIs RESTful.

### 15. PyMySQL==1.1.0
- **Función**: `PyMySQL` es un controlador MySQL para Python, que permite la conexión y manipulación de bases de datos MySQL desde aplicaciones Flask.

### 16. pyrsistent==0.20.0
- **Función**: `pyrsistent` es una biblioteca que proporciona estructuras de datos persistentes e inmutables para Python, útiles para mantener estados de manera segura en aplicaciones web.

### 17. python-dotenv==1.0.1
- **Función**: `python-dotenv` carga variables de entorno desde archivos `.env` en aplicaciones Flask, facilitando la configuración y el manejo de variables sensibles.

### 18. pytz==2023.3.post1
- **Función**: `pytz` proporciona utilidades para trabajar con zonas horarias en Python, permitiendo la conversión y manipulación de fechas y horas en diferentes zonas horarias.

### 19. SQLAlchemy==2.0.23
- **Función**: `SQLAlchemy` es una biblioteca ORM para Python que facilita la interacción con bases de datos relacionales, proporcionando una abstracción sobre SQL.

### 20. typing_extensions==4.8.0
- **Función**: `typing_extensions` proporciona extensiones para el módulo `typing` de Python, incluyendo soporte para anotaciones de tipo más avanzadas.

### 21. Werkzeug==2.3.8
- **Función**: `Werkzeug` es una biblioteca WSGI para Python, utilizada internamente por Flask para manejar solicitudes HTTP.

### API REST
- **Descripción**: Este proyecto utiliza Flask para crear una API RESTful, que proporciona endpoints para interactuar con recursos a través de HTTP.
  
### Configuración y Uso
- Para iniciar el entorno virtual:

  ```bash
  python3 -m venv .venv
  . .venv/bin/activate

Para agregar un nuevo módulo instalado al requirements.txt

```bash
pip freeze > requirements.txt

```
Para instalar todos los requerimientos listados en requirements.txt:

```bash
pip install -r requirements.txt
```