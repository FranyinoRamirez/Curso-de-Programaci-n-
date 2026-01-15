import pywhatkit

# 1. Configura el número (con + y código de país) y el mensaje
telefono = "" \
""
mensaje = mensaje = """Estimado/a cliente/usuario,
Lamentamos informarle que los servicios que usted requiere no se encuentran disponibles en estos momentos.
Agradecemos mucho su comprensión y le pedimos, por favor, esperar al próximo ciclo de servicio o contactarnos nuevamente más adelante para que podamos ofrecerle la asistencia que necesita.
Valoramos su interés y estamos a su disposición para ayudarle tan pronto como la disponibilidad de los servicios sea restablecida. @Yino_Wrld"""
print("Preparando el envío... No toques el teclado ni el mouse.")

pywhatkit.sendwhatmsg_instantly(telefono, mensaje, wait_time=15, tab_close=True)

print("Proceso terminado.")