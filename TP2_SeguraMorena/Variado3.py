#Suma de Números Positivos y Negativos: Se requiere un programa que permita el ingreso de 
#10 números y al finalizar muestre en pantalla la cantidad números positivos y por otra parte 
#la cantidad de números negativos que fueron ingresados.

positive_count = 0
negative_count = 0

for _ in range(10):
    num = float(input("Ingrese un número: "))
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1

print(f"Cantidad de números positivos: {positive_count}")
print(f"Cantidad de números negativos: {negative_count}")

