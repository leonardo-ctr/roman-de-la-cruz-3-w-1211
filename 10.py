print(" ")
print(" 10- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.")
print(" ")
print(" Roman De la Cruz Leonardo antonio,(10),1211,3-w")
print(" ")
#define
def es_vocal(caracter):
    print(" ")  # DEFINE UNA LÍNEA EN BLANCO
    # Convertir el carácter a minúsculas
    return caracter.lower() in 'aeiou'
print(" ")  # DEFINE UNA LÍNEA EN BLANCO
# Solicita que ingrese un carácter
caracter = input("Ingresa un carácter: ")  # Entrada de un carácter
# comprobar el caracter
if len(caracter) == 1:
    resultado = es_vocal(caracter)
    #muestra resultado
    print(f"¿'{caracter}' no es vocal {resultado}")  
else:
    #imprime si hay error
    print("Por favor, ingresa solo un carácter.")  
    print(" ")
