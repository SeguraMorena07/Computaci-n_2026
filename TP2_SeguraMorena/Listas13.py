# Dada una lista de números, ingresada por el usuario o inventada por usted, cree otra 
#lista con la cantidad de dígitos de cada numero de la misma.

numeros = [23, 7, 34, 22, 3, 96, 77, 2, 81, 41, 38, 8]

cant_digitos = []

for n in numeros:
    cant_digitos.append(len(str(abs(n)))) 

print("Lista original:", numeros)
print("Cantidad de dígitos de cada número:", cant_digitos)
