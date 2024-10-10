print(" ")  # Línea en blanco
print(" 5- Calcular el área de un círculo  y el volumen otra que calcule el volumen de un cilindro y utilice  primera función.")
print(" Roman De la Cruz Leonardo antonio,(5,1211,3-w")
print(" ")  # Línea en blanco
PI = 3.14159#valor de pi
#calcular el área de un círculo
#define
def calcular_area_circulo(radio):
    #operacion
    return PI * (radio ** 2)
print(" ")  # Línea en blanco
# calcular el volumen de un cilindro
#define
def calcular_volumen_cilindro(radio, altura):
    #operaciones
    area_base = calcular_area_circulo(radio) 
    volumen = area_base * altura
    return volumen
print(" ")  # Línea en blanco
# Solicita valores
radio = float(input("Ingresa el radio del círculo: "))  
altura = float(input("Ingresa la altura del cilindro: "))  
print(" ") # Línea en blanco
# Calcular el área del círculo
area = calcular_area_circulo(radio)
#muestra resultado
print(f"El área del círculo es: {area:.2f}") 
print(" ")  # Línea en blanco
volumen = calcular_volumen_cilindro(radio, altura)
#muestra resultado
print(f"El volumen del cilindro es: {volumen:.2f}") 
print(" ")  # Línea en blanco
