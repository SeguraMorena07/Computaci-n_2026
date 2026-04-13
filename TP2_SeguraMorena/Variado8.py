#Pedirle al usuario dos números positivos, a y b. Controlar que a < b. Mostrar en pantalla 
#los números del intervalo cerrado [a, b] La computadora deberá ahora seleccionar al azar un 
#numero de ese intervalo. Y el usuario deberá adivinar cual número ha sido seleccionado por 
#la computadora, obteniendo un mensaje de éxito en caso de acertar. El usuario solo tendrá 10 
#vidas (número de intentos) y en caso de no acertar, deberá obtener un mensaje de pucha.

import random

a = int(input("Ingrese el número a (positivo): "))
b = int(input("Ingrese el número b (positivo, mayor que a): "))

if a >= b or a <= 0 or b <= 0:
    print("Error: asegúrese de que a < b y ambos sean positivos.")
else:
    print(f"Números en el intervalo [{a}, {b}]:")
    for i in range(a, b + 1):
        print(i, end=" ")
    print("\n")

    secret = random.randint(a, b)

    lifes = 10
    succes = False

    while lifes > 0:
        intento = int(input(f"Adivine el número (vidas restantes: {lifes}): "))
        if intento == secret:
            print("¡Éxito! Adivinaste el número.")
            succes = True
            break
        else:
            print("No es ese número...")
            lifes -= 1

    if not succes:
        print("Pucha... no lograste adivinar el número. Era:", secret)
