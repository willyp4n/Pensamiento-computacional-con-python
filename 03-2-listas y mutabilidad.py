"""Listas y mutabilidad

Las listas son secuencias de objetos, pero a diferencia de las tuplas y rangos, sí son mutables. Es posible iterar con ellas, y cuando modificas una lista, pueden existir efectos secundarios (side effects).

Para modificar una lista podemos:

Asignar vía índice (my_lista[0] = 5)
Utilizar los métodos de la lista (append, pop, remove, insert, etc.)"""

"""Vamos a generar nuestra primera lista"""
my_list = [1, 2, 3]

"""Para acceder al primer índice lo haremos de la siguiente forma"""
my_list[0]
1

########################################################

"""Si queremos utilizar la notación de slices (dividir) definimos los
índices en los que dividiremos nuestra lista."""

"""Aquí llamaremos desde el 2do indice hasta el final."""
my_list[1:]
[2, 3]

########################################################

"""Para agregar un item a nuestra lista lo haremos con la funcion append
my_list.append(4)"""

"""Ahora la lista tendra 4 objetos."""
print(my_list)
[1, 2, 3, 4]

########################################################

"""Para modificar un elemento podemos hacerlo
referenciando su índice"""
my_list[0] = 'a'
print(my_list)
['a', 2, 3, 5]

########################################################

"""El método pop eliminara el último elemento de nuestra lista"""
my_list.pop()
4

print(my_list)
['a', 2, 3]

########################################################

"""Cuando una variable hace referencía a una lista
significa que apunta al mismo espacio en memoria,
esto significa que si cambia la lista se vera reflejado
en todas sus referencias, esto es un side effect"""

"""Creamos la lista a"""
a = [1, 2, 3]

"""Creamos la lista b que hara referencía a la lista a"""
b = a

"""Si imprimimos las listas seran iguales"""
a
[1, 2, 3]

b
[1, 2, 3]

"""Si agrego un objeto a la lista a también se
vera reflejado en b"""
a.append(4)

a
[1, 2, 3, 4]

b
[1, 2, 3, 4]

"""Por esto debes tener mucho ojo al modificar las listas."""




"""Clonación

Casi siempre es mejor clonar una lista en vez de mutarla, esto nos ayuda a disminuir el riesgo de pérdida de la información. 
Para clonar una lista podemos utilizar rebanadas (slices) o la función list."""

"""Crearemos una lista a"""
a = [1, 2, 3]

"""Con la variable b clonaremos la lista a"""
b = list(a)

"""Si removemos el último elemento de a
no se vera reflejado en b"""
a.pop()
3

"""Veamos los elementos de a"""
a
[1,2]

"""Y los elementos de b"""
b
[1, 2, 3]




""" List comprehension

Es una forma concisa de aplicar operaciones a los valores de una secuencia. 
También se pueden aplicar condiciones para filtrar."""

"""Vamos a crear una lista con una operacion de range"""
my_list = list(range(10))


"""Si revisamos que contiene veremos que tiene todos
los numeros desde el 0 al 9"""
my_list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

###########################################################

"""Ahora aplicaremos un list comprehension en donde
vamos a multiplicar * 2 cada uno de los elementos"""
double = [i * 2for i in my_list]


"""Y si revisamos los elementos de la lista veremos"""
double
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

###########################################################

"""Otro ejemplo de list compregension puede ser
solo tomar los numeros pares de nuestra lista"""
pares = [i for i in my_list if i % 2 == 0]


"""Y si revisamos los elementos de la lista veremos"""
pares
[0, 2, 4, 6, 8]