#Permitir ingresar números enteros hasta que se ingrese la opción ”s” de salir. Luego mostrar 
#por pantalla los números ingresados.

numbers = []
while True:
    user_input = input("Ingrese un número entero (o 's' para salir): ")
    if user_input.lower() == 's':
        break
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Por favor, ingrese un número entero válido o 's' para salir.")

print("Números ingresados:")
for num in numbers:
    print(num)

