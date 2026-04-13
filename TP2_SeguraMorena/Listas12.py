# Pedir al usuario una frase. Determinar de al menos dos modos diferentes (con y sin listas) 
#la cantidad de palabras que hay en dicha frase.

# Método sin listas
phrase = input("Ingrese una frase: ")
words = phrase.split()
cantidad = len(words)
print("Cantidad de palabras (con listas):", cantidad)

# Método con listas
phrase = input("Ingrese una frase: ")

counter = 0
in_word = False

for character in phrase:
    if character != " " and not in_word:
        counter += 1
        in_word = True
    elif character == " ":
        in_word = False

print("Cantidad de palabras (sin listas):", counter)   
