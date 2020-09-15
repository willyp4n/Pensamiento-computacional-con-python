def factorial(n):
    """ Calcula el factorial de n
    n > 0 int 
    return n!
    """
    print(n)
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
def run():
    n = int(input("Escribe un numero: "))
    print(factorial(n)) 


if __name__ == "__main__":
    run()