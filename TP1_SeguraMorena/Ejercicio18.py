#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si
#el divisor es cero el programa debe mostrar un mensaje de error.

dividendo = float(input("Ingrese el número dividendo: "))
divisor = float(input("Ingrese el número divisor: "))

if divisor == 0:
    print("Error: no se puede dividir por cero")
else:
    resultado = dividendo / divisor
    print("El resultado de la división es:", resultado)

