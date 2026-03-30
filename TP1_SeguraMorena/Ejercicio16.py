#Realizar un programa que permita al usuario ingresar un número y determine si es positivo
#o negativo.

number = float(input("Ingrese un número: "))

if number > 0:
    print("El número es positivo")
elif number < 0:
    print("El número es negativo")
else:
    print("El número es cero")

