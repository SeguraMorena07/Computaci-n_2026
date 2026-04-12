#Permita al usuario ingresar una frase. Cambie las letras a por 4 y las letras e 
# por 3.

phrase = input("Ingrese una frase: ")
modified_phrase = phrase.replace('a', '4').replace('e', '3')
print("Frase modificada:", modified_phrase)
