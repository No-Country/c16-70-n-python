import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading



class EnviarCorreo():
    def send_notify(self,datos):
        """_summary_

        Args:
            datos (list): [fecha,horario,usuario,correo]
        """
        cuerpo = f"Se ingreso una reserva en Agendify: \n Fecha: {datos[0]} \n Horario: {datos[1]} \n usuario: {datos[2]}"
        correo = datos[3]
        t = threading.Thread(target=self.enviar_correo, name="enviar_correo",args=(cuerpo,correo))
        t.start()


    def enviar_correo(self,cuerpo,correo):
        servidor_smtp = 'smtp.gmail.com'
        puerto_smtp = 587

        remitente = 'correo@correoqueenvia.com'
        contraseña = 'contraseñadelcorreo'

        mensaje = MIMEMultipart()
        mensaje['From'] = remitente
        mensaje['To'] = correo
        mensaje['Subject'] = 'Nueva Reseva'

        mensaje.attach(MIMEText(cuerpo, 'plain'))

        # Inicio conexion
        with smtplib.SMTP(servidor_smtp, puerto_smtp) as servidor:
            servidor.starttls()

            #me logeo
            servidor.login(remitente, contraseña)

            #envio correo
            servidor.send_message(mensaje)

        print("Correo electrónico enviado exitosamente.")


prueba = EnviarCorreo()
datos = ["2024-02-21","09:00","fernandosg","fer.gab.sua@gmail.com"]
prueba.send_notify(datos)
