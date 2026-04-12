#Pida 10 nombres de películas al usuario. Guárdelos en una lista. Luego pida al usuario 
#que ingrese un numero n del 1 al 10. Controle que n este en el rango correcto, es decir 
#entre 1 y 10. Muestre en pantalla cual es la película n-esima. Por ejemplo, si el usuario 
#me ingresa 1, debo mostrar la primer película de la lista.

movies = []
for i in range(10):
    movie = input("Ingrese el nombre de una película: ")
    movies.append(movie)
while True:
    n = int(input("Ingrese un número del 1 al 10: "))
    if 1 <= n <= 10:
        print(f"La película número {n} es: {movies[n-1]}")
        break
    else:
        print("Número inválido. Por favor, ingrese un número entre 1 y 10.")

