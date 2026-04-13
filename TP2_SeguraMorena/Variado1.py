#Pedirle al usuario la cantidad de notas que desea ingresar. Luego pedir cada nota, y 
#guardarlas.

notes = []
num_notes = int(input("¿Cuántas notas desea ingresar? "))
for i in range(num_notes):
    note = float(input(f"Ingrese la nota {i+1}: "))
    notes.append(note)
    
print("Notas ingresadas:", notes)   

