#Se le pedirá al usuario una frase. Se mostraran en pantalla, una palabra por linea de la 
#misma. *no usar listas en este ejercicio.

phrase = input("Ingrese una frase: ")
word = ""
for character in phrase:
    if character == " ":
        print(word)   
        word = ""     
    else:
        word += character

if word:
    print(word) 
