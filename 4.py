print("4.- Calcular total de una factura luego del IVA. primero obtener la cantidad sin IVA luego el porcentaje de IVA a aplicar, por ultimo devolver el total de la factura")
print(" ")  # Define una línea en blanco
print(" Roman De la Cruz Leonardo antonio,(4),1211,3-w")
print(" ")  # DEFINE UNA LÍNEA EN BLANCO
def calcular_total_factura(cantidad_sin_iva, porcentaje_iva):
    # Calcular el IVA
    iva = cantidad_sin_iva * (porcentaje_iva / 100)
    # Calcular el total
    total = cantidad_sin_iva + iva
    return total

print(" ")  # DEFINE UNA LÍNEA EN BLANCO

# Solicitar al usuario que ingrese la cantidad sin IVA
cantidad_sin_iva = float(input("Ingresa la cantidad sin IVA: "))  
# Solicitar al usuario que ingrese el porcentaje de IVA
porcentaje_iva = float(input("Ingresa el porcentaje de IVA: "))  
# Calcula el total de la factura
total_factura = calcular_total_factura(cantidad_sin_iva, porcentaje_iva)
# Imprime el resultado
print(f"El total de la factura es: {total_factura:.2f}")
print(" ")  # DEFINE UNA LÍNEA EN BLANCO
