#Desarrollar un programa que permita al usuario ingresar una serie de números, sumar todos 
#los pares y al terminar mostrar dicha suma. Si se ingresó algún impar, mostrar un mensaje 
#“Se ingresaron impares”. Para finalizar el ingreso, indicar la cantidad de números a 
#ingresar al principio del programa, o interrumpir la carga cuando se ingrese el número 99.


addition_peers = 0
exists_odd = False

amount = int(input("¿Cuántos números desea ingresar? (o ingrese 0 para usar el 99 como fin): "))

if amount > 0:
    for i in range(amount):
        number = int(input(f"Ingrese el número {i+1}: "))
        if number % 2 == 0:
            addition_peers += number
        else:
            exists_odd = True
else:
    while True:
        number = int(input("Ingrese un número (99 para terminar): "))
        if number == 99:
            break
        if number % 2 == 0:
            addition_peers += number
        else:
            exists_odd = True

print("\nLa suma de los números pares es:", addition_peers)
if exists_odd:
    print("Se ingresaron impares.")

