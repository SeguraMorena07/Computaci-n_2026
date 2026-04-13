#Tirar 20 veces un dado de 6 caras. Mostrar el promedio de esas 20 tiradas.

import random
spinces = []
for i in range(20):
    spince = random.randint(1, 6)
    spinces.append(spince)

average = sum(spinces) / len(spinces)
print("Spinces:", spinces)
print("Promedio de los spinces:", round(average, 2))

