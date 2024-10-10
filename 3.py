print("3- Dar un entero positivo y resuelva su factorial.")
print(" Roman De la Cruz Leonardo antonio,(3),1211,3-w")
print(" ")#define una linea en blanco
#define
def calcular_factorial(n):   
    # Verifica si el número es negativo
    if n < 0:
        return "tiene que ser positivo el valor y entero."
    # El factorial de 0 y 1 es 1
    if n == 0 or n == 1:
        return 1
    # Llama a la función para calcular el factorial
    return n * calcular_factorial(n - 1)
# Solicita al usuario que ingrese un número
numero = int(input("Ingresa un número entero no negativo: "))
# muestra el resultado
print(f"El factorial de {numero} es {calcular_factorial(numero)}")