#Dada la siguiente lista de valores numéricos [56, 7, 34, 19, 3, 1, 76, 2, 81, 4, 2, 8] 
#muestre en pantalla solo los elementos de la misma que están ubicados en posiciones pares, 
#como 0, 2, 4, etc (¿Como puede determinar si un nro es par o no? ¿Deberá escribir cada print 
#de a uno, o deberá considerar realizar un recorrido por la lista, usando un bucle?)

numbers = [56, 7, 34, 19, 3, 1, 76, 2, 81, 4, 2, 8]
for i in range(len(numbers)):
    if i % 2 == 0:  
        print(numbers[i])
    
#Al usar el operador modulo (%) con 2, podemos determinar si un número es par o impar. 
# Si el resultado es 0, el número es par; si el resultado es 1, el número es impar. 
# En este caso, estamos verificando si el índice 'i' es par para imprimir solo los 
# elementos ubicados en posiciones pares de la lista.   

#Lo eficiente es usar un bucle que recorra la lista y aplique la condición para no
#tener que escribir un print para cada elemento.

