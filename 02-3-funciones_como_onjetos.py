def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero) 
        resultados.append(resultado)
    

nums =[1, 2, 3, 4]

aplicar_operacion(multiplicar_por_dos, nums)
