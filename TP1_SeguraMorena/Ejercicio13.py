#Realizar un programa que permita al usuario ingresar una palabra si la longitud de la palabra
#es mayor a 5 muestre en pantalla cuantos caracteres en total tiene la misma.

palabra = input("Ingrese una palabra: ")

if len(palabra) > 5:
    print("La palabra tiene", len(palabra), "caracteres en total")

