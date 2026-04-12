#Dada la siguiente lista de compras de ingredientes para preparar una torta, mostrarla en 
#pantalla, un ingrediente por línea. Luego corregir el ultimo a ”Canela en polvo” 
#[”Chocolate”, ”Huevos”, ”Manteca”, ”Crema de leche”, ”Frutillas”]

shopping_list = ["Chocolate", "Huevos", "Manteca", "Crema de leche", "Frutillas"]
print("Lista de compras:")
for ingredient in shopping_list:
    print(ingredient)
shopping_list[-1] = "Canela en polvo"
print("\nLista de compras corregida:")
for ingredient in shopping_list:
    print(ingredient)

