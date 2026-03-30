#Realizar un programa que lea dos números enteros desde teclado e informe en pantalla cuál
#de los dos números es el mayor. Si son iguales debe informar en pantalla lo siguiente: “Los
#números leídos son iguales”

number_1 = int(input("Ingrese el primer número entero: "))
number_2 = int(input("Ingrese el segundo número entero: "))

if number_1 > number_2:
    print("El valor mayor es:", number_1)
elif number_2 > number_1:
    print("El valor mayor es:", number_2)
else:
    print("Los números leídos son iguales")

