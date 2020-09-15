def run():
    objetivo = int(input("escoge un numero: "))
    epsilon = 0.001
    paso = epsilon**2
    respuesta = 0.0
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta**2 <= objetivo: #la segunda condición simpelemente nos proteje contra numeros negativos
        respuesta += paso # respuesta = respuesta + paso
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f"no se encontro la raiz cuadrada de {objetivo}")
    else:
        print(f"la raiz cuadrada de {objetivo} es {respuesta}") 



if __name__ == "__main__":
    run()