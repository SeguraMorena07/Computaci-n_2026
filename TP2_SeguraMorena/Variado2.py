#Cuenta Regresiva: Se requiere un programa que permita el ingreso de un numero positivo y 
#muestre en pantalla la cuenta regresiva desde el numero ingresado hasta llegar a 0. Realizar 
#diferentes versiones del programa, utilizando en cada una, una estructura de bucle diferente 
#de las que tiene disponibles en Python.

# Versión utilizando un bucle for
num = int(input("Ingrese un número positivo para la cuenta regresiva: "))
for i in range(num, 0, -1):
    print(i)    
print("¡Cuenta regresiva finalizada!")

# Versión utilizando un bucle while
num = int(input("Ingrese un número positivo para la cuenta regresiva: "))
while num > 0:
    print(num)
    num -= 1
print("¡Cuenta regresiva finalizada!")

