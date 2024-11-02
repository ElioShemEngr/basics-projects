import pywhatkit as kit

# Número de teléfono en formato internacional sin el signo "+"
phone_number = "+51950857659"  # Ejemplo: +5215512345678 para un número en México

# Mensaje a enviar
message = "Hola, este es un mensaje de prueba desde Python usando pywhatkit!"

# Hora de envío (24 horas)
hour = 13  # Hora de envío (ej. 15 para las 3 PM)
minute = 23  # Minuto de envío

# Enviar el mensaje
kit.sendwhatmsg(phone_number, message, hour, minute)