print(" ")
print("6- Capturar dirección de email. Desplegar mensaje si la dirección es válida o no, siendo que una función lo revisar por tener la @ solo así es valida")
print(" Roman De la Cruz Leonardo antonio,(6),1211,3-w")
print(" ")  # Línea en blanco
print("Roman De la Cruz Leonardo Antonio, número")
def es_email_valido(email):
    # Verifica si hay un '@' en la dirección de email
    return '@' in email
print(" ")  # Línea en blanco
# ingresa el correo
email_usuario = input("Ingresa tu correo: ")
print(" ")  # Línea en blanco
# Comprobar si el email es válido
if es_email_valido(email_usuario):
    #imprime si es valido
    print("¡Email válido!")
    print(" ")  # Línea en blanco
else:
    #imprime si no es valido
    print("Email no válido.")
    print(" ")  # Línea en blanco
