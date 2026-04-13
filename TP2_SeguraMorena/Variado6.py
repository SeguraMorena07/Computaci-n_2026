#Permitir ingresar 10 números al usuario. Determinar y mostrar el menor y el mayor.

numbers = []
for i in range(10):
    num = float(input(f"Ingrese el número {i+1}: "))
    numbers.append(num)

print("El menor número es:", min(numbers))
print("El mayor número es:", max(numbers))

