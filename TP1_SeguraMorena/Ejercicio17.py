#Realizar un programa que permita al usuario ingresar 3 números, ordenarlos y mostrarlos
#luego en pantalla de menor a mayor.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

numeros = [num1, num2, num3]

numeros_ordenados = sorted(numeros)

print("Los números ordenados de menor a mayor son:", numeros_ordenados)

