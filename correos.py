from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# MIME > Multipurpose Internet Mail Extensions
from smtplib import SMTP # Simple Mail Transfer Protocol

def enviarCorreo():
    mensaje = MIMEMultipart()
    # Titulo del correo
    mensaje['Subject'] = 'Olvidaste la password'
    # Emisor del correo
    mensaje['From'] = 'perccatrejorafael@gmail.com'
    # Destinatario del correo
    mensaje['To'] = 'raffotrejo@gmail.com'

    # Cuerpo del correo
    body = 'Hola, buenos días. Al parecer has olvidado tu contrasena, te sugerimos que la cambies en el siguiente link'

    texto = MIMEText(body, 'plain')

    mensaje.attach(texto)

    # Inicio la conexion con mi cuenta de GMAIL
    conexion = SMTP('smtp.gmail.com', 587)
    
    conexion.starttls()

    # me autentico con mis credenciales
    conexion.login('perccatrejorafael@gmail.com', 'bkwedultcwikhybp')

    # envio el correo hacia los destinatarios
    conexion.sendmail(from_addr='perccatrejorafael@gmail.com', to_addrs='raffotrejo@gmail.com', msg=mensaje.as_string())

    # finalizo la conexion con el servidor de correos
    conexion.quit()

    print('Email enviado exitosamente')

enviarCorreo()