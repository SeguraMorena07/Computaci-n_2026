#Pedirle al usuario sus 10 marcas favoritas. Mostrar una marca al azar de la lista.

import random

brands = []
for i in range(10):
    brand = input(f"Ingrese su marca favorita {i+1}: ")
    brands.append(brand)

random_brand = random.choice(brands)
print("Su marca elegida al azar es:", random_brand)

