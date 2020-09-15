# lo mismo que en metodos numéricos es conocido como el metodo de la bisección
def run():
    objetivo = int(input("escoge un numero: "))
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo) #regresa el valor mas alto entre los valores dados.
    respuesta = (alto + bajo)/2
    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f"bajo= {bajo} alto= {alto} respuesta = {respuesta}")
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo)/2
    print(f"la raiz cuadrada de {objetivo} es {respuesta}")


if __name__ == "__main__":
    run()