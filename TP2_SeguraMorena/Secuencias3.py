#Pida una frase al usuario, controle que tenga una longitud total mayor a 5 caracteres. 
# Muestre en pantalla los primeros 3 caracteres de la misma.

phrase = input("Ingrese una frase: ")
if len(phrase) > 5:
    print("Los primeros tres caracteres son:", phrase[:3])
else:
    print('La frase debe tener más de 5 caracteres.')   
