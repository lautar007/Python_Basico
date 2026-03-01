#En este archivo veremos distintas estructuras de datos.

#---------LISTAS---------#
#Las listas son una estructura de datos que permite almacenar una colección de elementos ordenados y mutables. Se definen utilizando corchetes [] y los elementos se separan por comas. Por ejemplo:
mi_lista = [1, 2, 3, "hola", [4, 5], True]
#Las listas pueden contener cualquier tipo de dato, incluso otras listas (listas anidadas). Sin embargo, convencionalmente, se recomienda que los elementos de una lista sean del mismo tipo.
#Las listas permiten elementos duplicados. 
#Las posiciones del orden de las listas comienzan desde 0. 

print(mi_lista[0])  # Imprime el primer elemento de la lista (1)

#Podemos conocer la cantidad de elementos de una lista utilizando la función len():
print(len(mi_lista))  # Imprime la cantidad de elementos en la lista (6)

#Podemos buscar un elemento específico en la lista utilizando el operador "in":
print(3 in mi_lista)  # Imprime True, ya que el número 3 está en la lista. Esto se puede utilizar junto con estructuras condicionales.

#Los métodos de listas más comunes son:
mi_lista.append("nuevo elemento")  # Agrega un nuevo elemento al final de la lista
mi_lista.insert(2, "elemento en posición 2")  # Inserta un elemento en la posición 2 (índice 2)
mi_lista.remove(2)  # Elimina el primer elemento con el valor 2 de la lista.
mi_lista.pop()  # Elimina y devuelve el último elemento de la lista
mi_lista.pop(1)  # Elimina y devuelve el elemento en la posición 1 (índice 1)
#mi_lista.sort()  # Ordena los elementos de la lista (solo funciona si los elementos son del mismo tipo y son comparables)
mi_lista.reverse()  # Invierte el orden de los elementos en la lista

print(mi_lista)

#Para unir dos listas en una sola, podemos utilizar el operador "+" o el método "extend()":

otra_lista = [6, 7, 8]
lista_unida = mi_lista + otra_lista  # Utilizando el operador "+"
print(lista_unida)

mi_lista.extend(otra_lista)  # Utilizando el método "extend()"
print(mi_lista)

#Mientras que la concatenación guarda los elementos de ambas listas en una nueva lista, el método "extend()" agrega los elementos de la segunda lista a la primera lista existente.

#---------TUPLAS---------#
#Las tuplas son una estructura de datos similar a las listas, pero son inmutables, lo que significa que no se pueden modificar después de su creación. Se definen utilizando paréntesis () y los elementos se separan por comas. Por ejemplo:

mi_tupla = (1, 2, 3, "hola", [4, 5], True)
#Al igual que las listas, las tuplas pueden contener cualquier tipo de dato. Sin embargo, al ser inmutables, no se pueden modificar sus elementos después de su creación.
#Las tuplas también permiten elementos duplicados.

#Se maneja de forma similar a las listas, con índices comenzando desde 0, y se pueden utilizar los mismos métodos de acceso y búsqueda. Sin embargo, no se pueden utilizar métodos que modifiquen la tupla, como "append()", "insert()", "remove()", "pop()", "sort()" o "reverse()".

#Las tuplas pueden desempaquetarse, lo que significa que podemos asignar los elementos de una tupla a variables individuales. Por ejemplo:
a, b, c, d, e, f = mi_tupla
print(a)  # Imprime el primer elemento de la tupla (1)
print(d)  # Imprime el cuarto elemento de la tupla ("hola")

#Hay que tener en cuenta que se necesitan tantas variables como elementos tenga la tupla para desempaquetarla correctamente.

#Para modificar una tupla, es necesario convertirla a una lista, realizar las modificaciones necesarias y luego convertirla nuevamente a una tupla. Por ejemplo:

mi_tupla = (1, 2, 3)
mi_lista = list(mi_tupla)  # Convertir la tupla a una lista
mi_lista.append(4)  # Modificar la lista
mi_tupla = tuple(mi_lista)  # Convertir la lista nuevamente a una tupla
print(mi_tupla)  # Imprime la tupla modificada (1, 2, 3, 4)

#Esto sin embargo, no es recomendable ya que la naturaleza de la tupla es que sea inmutable.

#---------CONJUSTOS | SETS---------#
#Los conjuntos, también conocidos como sets, son una estructura de datos que permite almacenar una colección de elementos únicos y no ordenados. Se definen utilizando llaves {} o la función set(). Por ejemplo:
mi_conjunto = {1, 2, 3, "hola", (4, 5), True}
#Los conjuntos no permiten elementos duplicados, por lo que si intentamos agregar un elemento que ya existe en el conjunto, no se agregará nuevamente.
#Los conjuntos no mantienen un orden específico de los elementos, por lo que no se pueden acceder a los elementos por su posición como en las listas o tuplas.
#Los conjuntos son mutables, lo que significa que se pueden modificar después de su creación, pero no se pueden modificar los elementos individuales, ya que no tienen un orden específico.

#Es posible utilizar métodos que modifiquen el conjunto, como "add()", "remove()", "discard()", "pop()", "clear()", entre otros.
#También podemos sumar elementos o concatenar colecciones utilizando el operador "|":
otro_conjunto = {3, 4, 5}
conjunto_unido = mi_conjunto | otro_conjunto  # Utilizando el operador "|"
print(conjunto_unido)

#O también con el método .update():
mi_conjunto.update(otro_conjunto)  # Utilizando el método "update()"
print(mi_conjunto)

#Los conjuntos también permiten realizar operaciones lógicas de unión, intersección, diferencia y diferencia simétrica utilizando los operadores "&", "-", y "^" respectivamente. Por ejemplo:

conjunto_unido = mi_conjunto.union(otro_conjunto)  # Utilizando el método "union()"
print(conjunto_unido)

conjunto_interseccion = mi_conjunto & otro_conjunto  # Intersección
print(conjunto_interseccion)

conjunto_diferencia = mi_conjunto - otro_conjunto  # Diferencia
print(conjunto_diferencia)

conjunto_simetrica = mi_conjunto ^ otro_conjunto  # Diferencia simétrica
print(conjunto_simetrica)


#Todas las colecciones de datos, como listas, tuplas y conjuntos, pueden ser utilizadas en bucles for para iterar sobre sus elementos.


#---------DICCIONARIOS---------#
#Los diccionarios son una estructura de datos que permite almacenar pares de clave-valor. Se definen utilizando llaves {} y los elementos se separan por comas. Por ejemplo:

mi_diccionario = {
    "nombre": "Juan", 
    "edad": 30, 
    "ciudad": "Madrid"
    }

#Los diccionarios permiten almacenar cualquier tipo de dato como valor, y las claves deben ser  inmutables, como cadenas de texto, números o tuplas. No se permiten claves duplicadas, por lo que si intentamos agregar una clave que ya existe en el diccionario, se sobrescribirá el valor asociado a esa clave.
#Los valores de las claves pueden ser accedidos utilizando la clave correspondiente. Por ejemplo:

print(mi_diccionario["nombre"])  # Imprime el valor asociado a la clave "nombre" ("Juan")

#Podemos obtener las claves, los valores o los pares clave-valor de un diccionario utilizando los métodos "keys()", "values()" y "items()" respectivamente.

#Podemos saber que existe una clave en el diccionario utilizando el operador "in". Esto es case-sensitive.

#Para modificar el valor de una clave, simplemente asignamos un nuevo valor a esa clave. Por ejemplo:

mi_diccionario["edad"] = 25  # Modifica el valor asociado a la clave "edad"

#Podemos agregar un nuevo par clave-valor al diccionario asignando un valor a una nueva clave. Por ejemplo:

mi_diccionario["profesión"] = "Ingeniero"  # Agrega un nuevo par clave-valor al diccionario

#O también utilizando el método "update()":

mi_diccionario.update({"profesión": "Ingeniero"}) 

print(mi_diccionario)

#Para eliminar un par clave-valor del diccionario, podemos utilizar el método "pop()" o la palabra reservada "del". Por ejemplo:

mi_diccionario.pop("ciudad")  # Elimina el par clave-valor asociado a la clave "ciudad"

del mi_diccionario["edad"]  # Elimina el par clave-valor asociado a la clave "edad"

#Los diccionarios pueden utilizarse en un bucle for para iterar sobre sus claves, valores o pares clave-valor utilizando los métodos mencionados anteriormente: keys(), values() y items().
#Ejemplo recorriendo valores:

for valor in mi_diccionario.values():
    print(valor)  # Imprime cada valor del diccionario

#Los diccionarios también pueden ser anidados, es decir, pueden contener otros diccionarios como valores. Esto permite crear estructuras de datos más complejas y organizadas. Por ejemplo:
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "dirección": {
        "calle": "Calle Principal",
        "ciudad": "Madrid",
        "código postal": "28001"
    }
}
print(mi_diccionario["dirección"]["ciudad"])  # Imprime el valor asociado a la clave "ciudad" dentro del diccionario anidado "dirección" ("Madrid")