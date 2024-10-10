print(" ")
print("9- Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamentetodos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4])debería devolver 24")
print(" ")
print(" Roman De la Cruz Leonardo antonio,(9),1211,3-w")
print(" ")
#define
def sumar(lista):
    # Operaciones
    total = 0
    for numero in lista:
        total += numero
    return total
#define
def multiplicar(lista):
    # Operaciones
    total = 1
    for numero in lista:
        total *= numero
    return total
print(" ")  # Define una línea en blanco
# Solicitar al usuario que ingrese números separados por comas
#solciita valores
entrada = input("Ingresa números separados por comas: ")  
#convierte en lista
numeros = [float(num) for num in entrada.split(",")]  
print(" ")  # Define una línea en blanco
# Calcular la suma y multiplicación de la lista
#resultados
resultado_suma = sumar(numeros)  
resultado_multiplicacion = multiplicar(numeros)  
# Imprimie los resultados
print(f"La suma de la lista es: {resultado_suma}")
print(f"La multiplicación de la lista es: {resultado_multiplicacion}")
print(" ")  # Define una línea en blanco

