#Crear dos listas del mismo tamaño, y luego armar una tercera lista, a la cual primero se 
#le agregue el primer elemento de la lista 1, luego el primer elemento de la lista 2. Luego 
#se le agregue el segundo elemento de la lista 1, luego el segundo elemento de la lista 2, 
#y así sucesivamente.

list_1 = ["campera", "tapado", "stilettos"]
list_2 = ["abrida", "formal", "elegantes"]
combined_list = []
for i in range(len(list_1)):
    combined_list.append(list_1[i])
    combined_list.append(list_2[i])
print(combined_list)

