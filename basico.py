#---------HOLA MUNDO EN PYTHON---------
#Bienvenido. Este proyecto de programación se centra en explicar los fundamentos básicos de Python. A lo largo de los distintos archivos encontrará código ampliamente documentado por medio de anotaciones, lo que facilitará la comprensión de cada línea de código. El objetivo es proporcionar una base sólida para aquellos que están comenzando a aprender Python, así como para aquellos que desean reforzar sus conocimientos en este lenguaje de programación. 
#Este es un programa básico en Python que muestra cómo imprimir un mensaje en la consola.
#Para crear este archivo se utilizó un comando de terminal: New-Item "basico.py". Este comando crea un nuevo archivo con el nombre indicado en el directorio donde está ubicada la terminal. 

#La función de Python que permite imprimir un mensaje en la consola es "print()". Esta función toma como argumento el mensaje que se desea mostrar y lo muestra en la salida estándar (consola).

print("¡Hola, mundo!")  # Esta línea de código imprime el mensaje "¡Hola, mundo!" en la consola.

#Podemos ejecutar el archivo por medio de la consola utilizando el comando "python basico.py".

#---------INDENTACIÓN---------
#En Python es importante el termino "indentación", que se refiere a un espacio en blanco al inicio de una línea de código. La indentación es la forma en que se organizan los bloques de código en Python. Mediante ella, el lenguaje reconoce que ciertas líneas de código pertenecen a una misma estructura, como un bucle o un condicional. 
#Brevemente, una estructura condicional es un bloque de código que, por medio de la evaluación de un enunciado, permite controlar el flujo de ejecución de un programa, escogiendo entre una opción u otra, según sea verdadero o falso el enunciado evaluado. Su sintaxis utiliza la palabra reservada "if" seguida de la condición a evaluar. 
#Por ejemplo:

if 5 > 3: 
    print("Cinco es mayor que tres.")  # Esta línea de código se ejecutará si la condición es verdadera, y como lo es, siempre se ejecutará.

#Como vemos, la línea de código que se encuentra dentro del bloque "if" está indentada, lo que indica que pertenece a ese bloque.

#---------ASIGNACIÓN DE VARIABLES---------
x = "Esta es una variable de tipo string."
print(x)

#Las variables en Python permiten la sobreescritura y son case-sensitive.
#El case convencional en Python es el snake_case. 
#No es correcto comenzar con un número, ni con un símbolo. Tampoco se puede utilizar guiones medios o espacios en el nombre de una variable.

#Por convención se utiliza variables en mayúsculas para definir constantes y variables que comienzan en guión bajo para definir variables privadas.

#Es posible definir varias variables en una sola línea de código, separándolas por comas. Por ejemplo:
a, b, c = "Hola", "Mundo", "Python"
print(a, b, c)

#También es posible asignar el mismo valor a varias variables en una sola línea de código. Por ejemplo:
x = y = z = "¡Hola a todos!"
print(x, y, z)

#---------TIPOS DE DATOS PRIMITIVOS Y ESTRUCTURAS---------
#En Python existen distintos tipos de datos. Algunos de los más comunes son:
#- Enteros (int)
#- Flotantes (float)
#- Cadenas de texto (str)
#- Booleanos (bool)

#Para saber el tipo de dato de una variable, se puede utilizar la función type().
print(type(x))  # Imprime el tipo de dato de la variable x, que es str (string).
print(type(5))  # Imprime el tipo de dato del número 5, que es int (integer).
print(type(5.0))  # Imprime el tipo de dato del número 5.0, que es float.
print(type(True))  # Imprime el tipo de dato del valor True, que es bool (boolean).

#También existen estructuras de datos como listas y tuplas: 
#- Listas (list): Son colecciones ordenadas y mutables de elementos. Se definen utilizando corchetes [].
#- Tuplas (tuple): Son colecciones ordenadas e inmutables de elementos. Se definen utilizando paréntesis ().

lista = [1, 2, 3, 4, 5]  # Esta es una lista de números enteros.
tupla = (1, 2, 3, 4, 5)  # Esta es una tupla de números enteros.

#Otra estructura son los diccionarios (dict), que son colecciones de pares clave-valor. Se definen utilizando llaves {}.

diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}  # Este es un diccionario con información de una persona.

#Los conjuntos (set) son colecciones no ordenadas de elementos únicos. Se definen utilizando llaves {} o la función set().

conjunto = {1, 2, 3, 4, 5}  # Este es un conjunto de números enteros.
#Los elementos repetidos serán ignorados.

#---------CASTEO DE NUMEROS Y ALEATORIEDAD---------
num = 5  # Esta es una variable de tipo entero (int).
num_flotante = float(num)  # Esta línea de código convierte el número entero a un número flotante (float).

num2 = 3.14  # Esta es una variable de tipo flotante (float).
num2_entero = int(num2)  # Esta línea de código convierte el número flotante a un número entero (int). El resultado será 3, ya que se trunca la parte decimal.

#En el caso de que querramos generar numeros aleatorios, debemos importar el módulo random, que es parte de la biblioteca estándar de Python. Este módulo proporciona funciones para generar números aleatorios.
import random
print(random.randint(1, 10))  # Esta línea de código genera un número entero aleatorio entre 1 y 10 (inclusive).

#---------MÉTODOS DE CADENAS DE TEXTO---------
#En Python, las cadenas de texto tienen varios métodos útiles para manipularlas. Algunos de los más comunes son:
#- upper(): Convierte todos los caracteres de la cadena a mayúsculas.
#- lower(): Convierte todos los caracteres de la cadena a minúsculas.
#- strip(): Elimina los espacios en blanco al inicio y al final de la cadena.
#- replace(): Reemplaza una subcadena por otra.
#- len(): Devuelve la longitud de la cadena.
#- split(): Divide la cadena en una lista de subcadenas utilizando un separador específico (por defecto, el espacio).

cadena = "Hola Mundo"
print(cadena.upper())  # Imprime "HOLA MUNDO"
print(cadena.lower())  # Imprime "hola mundo"
print(cadena.strip())  # Imprime "Hola Mundo" (sin espacios en blanco al inicio ni al final)
print(cadena.replace("Mundo", "Python"))  # Imprime "Hola Python"
print(len(cadena))  # Imprime la longitud de la cadena, que es 10 (incluyendo el espacio).
print(cadena.split())  # Imprime una lista de subcadenas, que en este caso será ["Hola", "Mundo"].

#Tanbién podemos saber si una cadena contiene una subcadena utilizando el operador "in". Por ejemplo:
print("Mundo" in cadena)  # Imprime True, ya que "Mundo" está presente en la cadena "Hola Mundo". Esta sintaxis es case-sensitive.
#También se puede usar en forma contraria para saber si una cadena no contiene una subcadena utilizando el operador "not in". Por ejemplo:
print("Python" not in cadena)

#Las cadenas de textos son estructuras indexadas, comenzando desde el cero. Para acceder a un carácter específico de una cadena, se puede utilizar la sintaxis de corchetes [] con el índice del carácter deseado. Por ejemplo:
print(cadena[0])  # Imprime "H", que es el primer carácter de la cadena.

#Utilizando los índices también podemos acceder a un rango de caracteres utilizando la sintaxis de slicing. Por ejemplo:
print(cadena[0:4])  # Imprime "Hola", que son los caracteres desde el índice 0 hasta el índice 3 (el índice 4 no se incluye).

#---------CONDICIONES DE VERACIDAD---------
#En Python, una condición es verdadera si su valor es True, y falsa si su valor es False.
#Los valores que se consideran falsos son:
#- False
#- None
#- 0
#- ""
#- []
#- ()
#- set()
#Cualquier otro valor se considera verdadero.

print(bool(False))  # Imprime False
print(bool(None))  # Imprime False
print(bool(0))  # Imprime False
print(bool(""))  # Imprime False

print(bool(True))  # Imprime True
print(bool(1))  # Imprime True
print(bool("Hola"))  # Imprime True

#Podemos saber si un dato es instancia de un determinado tipo de dato utilizando la función isinstance(). Por ejemplo:
print(isinstance(cadena, str))  # Imprime True, ya que la variable cadena es una instancia de la clase str (string).

#---------DATO NONE---------
#El dato None es un tipo de dato especial en Python que representa la ausencia de valor o la falta de un valor. Ejemplo:
variable = None  

