# Realizar un programa que permita ingresar dos palabras, y determine si tienen la misma
#longitud o no. Mostrar un mensaje en pantalla en cada caso. Misma longitud, una menor, o
#una mayor.

word_1 = input("Ingrese la primera palabra: ")
word_2 = input("Ingrese la segunda palabra: ")

if len(word_1) == len(word_2):
    print("Las palabras tienen la misma longitud")
elif len(word_1) > len(word_2):
    print("La primera palabra es más larga")
else:
    print("La segunda palabra es más larga")

