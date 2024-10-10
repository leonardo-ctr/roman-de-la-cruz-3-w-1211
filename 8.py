print(" ")
print(" 8- Definir una función (), que tome tres números como argumentos y devuelva el mayor de ellos.")
print(" ")
print(" Roman De la Cruz Leonardo antonio,(8),1211,3-w")
print(" ")  # Define una línea en blanco
#define
def nums(num1, num2, num3):
    # Devuelve el mayor de los tres números
    return max(num1, num2, num3)
print(" ")  # Define una línea en blanco
# Solicitar al usuario que ingrese tres números
numero1 = float(input("Ingresa el primer número: "))   
numero2 = float(input("Ingresa el segundo número: "))  
numero3 = float(input("Ingresa el tercer número: "))  
print(" ")  # Define una línea en blanco
# Calcular el mayor de los tres números
mayor = nums(numero1, numero2, numero3)
# Imprime el resultado
print(f"El mayor de los tres números es: {mayor}")
print(" ")  # Define una línea en blanco

