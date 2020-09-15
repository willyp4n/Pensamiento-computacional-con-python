#Manejo de excepciones
# Los manejos de excepciones son muy comunes en la programación, no tienen nada de excepcional. 
# Las excepciones de Python normalmente se relacionan con errores de semántica, también podemos crear 
# nuestras propias excepciones, pero cuando una excepción no se maneja (unhandled exception), el programa
# termina en error.

# Las excepciones se manejan con los keywords: try, except, finally. Se pueden utilizar también para 
# ramificar programas.

# No deben manejarse de manera silenciosa (por ejemplo, con print statements). 
# Para crear tu propia excepción utiliza el keyword raise.

"""Creamos una función en donde cada elemento de 
una lista es dividida por un divisor definido"""
def divide_elementos_de_lista(lista, divisor):
    """El programa intentara realizar la división"""
    try:
        return [i / divisor for i in lista]  # list comprenhension
    

    
    except ZeroDivisionError as e:
        print(e)
        return lista

    """En caso de error de tipo ZeroDivisionError que
    significa error al dividir en cero, el programa  ejecutara la instrucción instrucción anterior"""

lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))