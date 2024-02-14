import mysql.connector
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

class ConexionMySQL:
    """
    Clase para manejar la conexión a una base de datos MySQL.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de ConexionMySQL.
        """
        self.host = os.getenv("MYSQLHOST")         # Host de la base de datos
        self.usuario = os.getenv("MYSQLUSER")      # Usuario de la base de datos
        self.contraseña = os.getenv("MYSQLPASSWORD")  # Contraseña de la base de datos
        self.base_datos = os.getenv("MYSQLDATABASE")  # Nombre de la base de datos
        self.puerto = os.getenv("MYSQLPORT")       # Puerto de conexión a la base de datos
        self.conexion = None

    def conectar(self):
        """
        Establece una conexión a la base de datos MySQL.
        """
        try:
            self.conexion = mysql.connector.connect(
                host=self.host,
                user=self.usuario,
                password=self.contraseña,
                database=self.base_datos,
                port=self.puerto,
                autocommit=True
            )
            print("Conexión exitosa a la base de datos")
        except mysql.connector.Error as err:
            print("Error al conectar a la base de datos:", err)

    def ejecutar_consulta(self, consulta, datos=None):
        """
        Ejecuta una consulta SQL en la base de datos.

        Args:
            consulta (str): La consulta SQL a ejecutar.
            datos (tuple): Los datos opcionales para la consulta (por defecto es None).

        Returns:
            tuple: Los resultados de la consulta.
        """
        self.conectar()
        print(datos)
        if self.conexion.is_connected():
            cursor = self.conexion.cursor()
            if datos:
                print("llego hasta aca?")
                cursor.execute(consulta, datos)

            else:
                cursor.execute(consulta)

            filas = cursor.fetchall()
            cursor.close()
            return filas
        self.cerrar_conexion()


    def cerrar_conexion(self):
        """
        Cierra la conexión a la base de datos.
        """
        if self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada")


class Usuario(ConexionMySQL):
    """
    Clase para manejar operaciones relacionadas con usuarios en la base de datos MySQL.
    Hereda de ConexionMySQL.
    """

    def crear_user(self,usu_txt_username,usu_pass_pass, usu_txt_typeprofile):
        """
        Crea un nuevo usuario en la base de datos.

        Parameters:
        - usu_txt_username (str): El nombre de usuario del nuevo usuario.
        - usu_pass_pass (str): La contraseña del nuevo usuario.
        - usu_txt_typeprofile (str): El tipo de perfil del nuevo usuario.

        Returns:
        None

        Description:
        Este método permite crear un nuevo usuario en la base de datos. Toma tres argumentos: el nombre de usuario,
        la contraseña y el tipo de perfil del nuevo usuario. Luego construye una consulta SQL de inserción que inserta
        estos valores en la tabla 'LoginUser' de la base de datos 'railway'. Una vez construida la consulta, la ejecuta
        utilizando el método 'ejecutar_consulta' de la clase 'ConexionMySQL'.

        Example:
        usuario = Usuario()
        usuario.crear_user("juan", "password123", 1)

        Notes:
        - Los parámetros 'usu_txt_username', 'usu_pass_pass' y 'usu_txt_typeprofile' deben proporcionarse en el orden correcto.
        - El parámetro 'usu_txt_typeprofile' debe ser un entero que represente el tipo de perfil del usuario según la
        estructura de la base de datos.
        """

        consulta = """INSERT INTO `railway`.`LoginUser` (`usu_txt_username`, `usu_pass_pass`, `usu_txt_typeprofile`) VALUES (%s, %s, %s);"""
        datos = (usu_txt_username, usu_pass_pass, usu_txt_typeprofile)
        self.ejecutar_consulta(consulta,datos)


    def modificar_user(self):
        """
        Modifica un usuario existente en la base de datos.
        """
        pass

    def baja_user(self):
        """
        Da de baja a un usuario existente en la base de datos.
        """
        pass

    def consulta_user(self):
        """
        Consulta todos los usuarios en la tabla LoginUser.

        Returns:
            tuple: Los resultados de la consulta.
        """

        resultados = self.ejecutar_consulta("SELECT * FROM LoginUser")

        return resultados




# Ejemplo de uso
user = Usuario()
user.crear_user("pepepe","pass",2)

"""resultados = user.consulta_user()



for fila in resultados:
    print(fila)
    
user = Usuario()
resultados = user.consulta_user()

for fila in resultados:
    print(fila)
"""