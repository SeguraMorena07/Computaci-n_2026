# Leer dos números y determinar cuál de ellos es el mayor, mostrando por pantalla “El
#valor mayor es:” y el correspondiente número.

number_1 = float(input("Ingrese el primer número: "))
number_2 = float(input("Ingrese el segundo número: "))

# Determinar cuál es mayor
if number_1 > number_2:
    print("El valor mayor es:", number_1)
elif number_2 > number_1:
    print("El valor mayor es:", number_2)
else:
    print("Los dos números son iguales")

