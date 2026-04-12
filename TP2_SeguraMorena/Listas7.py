#Pedir el nombre al usuario, y corroborar si ese nombre existe entre los nombres de usuarios 
#validos guardados en una lista.

valid_usernames = ["moresegura07", "tobias23", "ciro27"]
username = input("Ingrese su nombre de usuario: ")
if username in valid_usernames:
    print("Nombre de usuario válido.")
else:
    print("Nombre de usuario no válido.")   
