#Permitir ingresar al usuario un numero de un digito. Controlando se haya ingresado dicho 
#número de no más de 1 digito de longitud, pasarlo a letras y mostrarlo en pantalla. 
# (Ejemplo: Si ingresa 3, se verá como resultado” tres”).

number = input("Ingrese un número de un dígito: ")
if len(number) == 1 and number.isdigit():
    digit_to_word = {
        '0': 'cero',
        '1': 'uno',
        '2': 'dos',
        '3': 'tres',
        '4': 'cuatro',
        '5': 'cinco',
        '6': 'seis',
        '7': 'siete',
        '8': 'ocho',
        '9': 'nueve'
    }
    word = digit_to_word[number]
    print(f"El número {number} se escribe: '{word}'.")

