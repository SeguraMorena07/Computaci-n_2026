#El usuario deberá ingresar una frase y una letra. Determine cuantas veces esta esa 
# letra en dicha frase, mostrar por pantalla.

phrase = input("Ingrese una frase: ")
letter = input("Ingrese una letra: ")
count = phrase.count(letter)
print(f"La letra '{letter}' aparece {count} veces en la frase.")    
