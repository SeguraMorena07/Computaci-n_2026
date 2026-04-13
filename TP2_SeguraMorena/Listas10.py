# El usuario deberá poder ingresar varios nombres completos (ejemplo: ”Luis Perez”). 
#El programa deberá luego, colocar los nombres en una lista y los apellidos en otra.

full_names = []
surnames = []   
amount = int(input("¿Cuántos nombres completos desea ingresar? "))

for i in range(amount):
    complete = input(f"Ingrese el nombre completo {i+1}: ")
    parts = complete.split(" ", 1)     
    
    if len(parts) == 2:
        full_names.append(parts[0])
        surnames.append(parts[1])
    else:
        print("Debe ingresar al menos nombre y apellido.")

print("\nLista de nombres:", full_names)
print("Lista de apellidos:", surnames)
