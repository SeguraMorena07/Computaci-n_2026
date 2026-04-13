#Tirar ahora, 2500 veces un dado de 6 caras. Mostrar el promedio de esas tiradas. 
#Comparar con el promedio del ejercicio anterior. ¿Nota una diferencia sustancial habiendo 
#cambiado la cantidad de tiradas?

import random

spinces = [random.randint(1, 6) for _ in range(2500)]

average = sum(spinces) / len(spinces)

print("Promedio de las 2500 tiradas:", round(average, 2))

#Con 2500 tiradas, la diferencia se reduce y el promedio se acerca mucho a 3.54.
