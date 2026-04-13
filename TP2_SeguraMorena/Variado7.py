#Numero Invertido: Se requiere mostrar en pantalla un numero invertido de 6 cifras, al que 
#fuera ingresado por teclado. (Ejemplo: en pantalla se verá: “El numero ingresado es 140975, 
#invertido es: 579041”)

number = input("Ingrese un número de 6 cifras: ")

if len(number) == 6 and number.isdigit():
    invertido = number[::-1] 
    print(f"El número ingresado es {number}, invertido es: {invertido}")
else:
    print("Debe ingresar exactamente un número de 6 cifras.")

