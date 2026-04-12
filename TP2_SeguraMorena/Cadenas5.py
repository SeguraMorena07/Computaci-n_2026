#Permita al usuario ingresar el nombre de un archivo, genere un nuevo nombre donde los 
#espacios sean reemplazados por guion bajo y la extensión por numerales.

filename = input("Ingrese el nombre del archivo: ")
parts = filename.split(".")
if len(parts) > 1:
    name = parts[0].replace(" ", "_")  
    extension = "#" * len(parts[-1])     
    new_name = name + "." + extension
else:
    new_name = filename.replace(" ", "_") #Si no hay extensuion, solo reemplazamos espacios

print("Nuevo nombre generado:", new_name)

