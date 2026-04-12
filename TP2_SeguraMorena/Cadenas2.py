#Se le permitirá al usuario ingresar una frase. Se mostrarán en pantalla solamente las 
#letras en posiciones pares de la misma.

phrase = input("Ingrese una frase: ")
for i in range(len(phrase)):
    if i % 2 == 0:  
        print(phrase[i])

