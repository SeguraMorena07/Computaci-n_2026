#Mostrar en pantalla los resultados de calcular las siguientes 
#expresiones (estas expresiones se encuentran escritas matemáticamente,
#y debería reescribirlas en notación de computadora previamente; cada 
#vez que encuentre en la expresión una letra minúscula, debe considerar 
#que ese dato lo debe ingresar el usuario): 5a + 10b _ 


a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
x = float(input("Ingrese el valor de x: "))
y = float(input("Ingrese el valor de y: "))
n = float(input("Ingrese el valor de n: "))

expresion1 = 5 * a + 10 * b
expresion2 = b ** 2
expresion3 = 2 * x - y
expresion4 = (2 * n - 1) / (2 * n - 1)


print("El resultado de 5a + 10b es:", expresion1)
print("El resultado de b² es:", expresion2)
print("El resultado de 2x - y es:", expresion3)
print("El resultado de (2n - 1) / (2n - 1) es:", expresion4)


