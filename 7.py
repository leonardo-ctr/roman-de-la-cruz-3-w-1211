print(" ")
print("7- Función que de un string, regrese la longitud de la última palabra. Las palabras tienen separación por uno o más espacios.")
print(" Roman De la Cruz Leonardo antonio,(7),1211,3-w")
print(" ")  # DEFINE UNA LÍNEA EN BLANCO
#define
def longitud_ultima_palabra(texto):
    # divide las palabras
    palabras = texto.strip().split()
    # Verificar si hay palabras
    if palabras:
        # Devolver la longitud de la última palabra
        return len(palabras[-1])  
    return 0  # Si no hay palabras, devolver 0
print(" ")  # DEFINE UNA LÍNEA EN BLANCO
# solicita el texto
texto = input("Ingresa una frase: ")  # Entrada de texto
print(" ")  # DEFINE UNA LÍNEA EN BLANCO
# Calcular la longitud de la última palabra
longitud = longitud_ultima_palabra(texto)  # variable
print(" ")  # DEFINE UNA LÍNEA EN BLANCO
# Imprimeel resultado
print(f"La longitud de la última palabra es: {longitud}")
print(" ")  # DEFINE UNA LÍNEA EN BLANCO
