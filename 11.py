print(" ")
print("11-  Que saque la distancia dirigida entre dos puntos")
print(" ")
print(" Roman De la Cruz Leonardo antonio,(11),1211,3-w")
print(" ")
import math  # Importar la librería matemática
# Función para calcular la distancia entre dos puntos
def distancia_dirigida(punto1, punto2):
    a, b = punto1  # Coordenadas del primer punto
    c, d = punto2  # Coordenadas del segundo punto
    return math.sqrt((c - a) ** 2 + (d - b) ** 2)
print(" ")  # DEFINE UNA LÍNEA EN BLANCO
# Solicita valores
a = float(input("Ingresa el  punto a: "))  
b = float(input("Ingresa el punto b: "))  
c = float(input("Ingresa el punto c: "))  
d = float(input("Ingresa el punto d: "))  
# Crear tuplas para los puntos
punto_a = (a, b)
punto_b = (c, d)
# Calcular la distancia
distancia = distancia_dirigida(punto_a, punto_b)
# Imprime el resultado
print(f"La distancia entre los puntos {punto_a} y {punto_b} es: {distancia:.2f}")
print(" ")  # DEFINE UNA LÍNEA EN BLANCO

