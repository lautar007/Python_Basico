#Se conoce como modularización a la práctica de dividir un programa en partes más pequeñas y manejables, llamadas módulos o funciones. Esto permite organizar el código de manera más clara, facilitar su mantenimiento y reutilización.

#---------FUNCIONES---------#
#Una función es un bloque de código que realiza una tarea específica y puede ser reutilizado en diferentes partes del programa. Se define utilizando la palabra reservada "def" seguida del nombre de la función y paréntesis que pueden contener parámetros. Por ejemplo:

def sumar(a, b):
    return a + b  # La función devuelve la suma de los dos parámetros

#Para llamar a una función, simplemente escribimos su nombre seguido de paréntesis con los argumentos correspondientes. Por ejemplo:

print(sumar(3, 5))  # Imprime el resultado de la función sumar con los argumentos 3 y 5 (8)

#Las funciones también pueden tener parámetros opcionales con valores predeterminados. Por ejemplo:
def saludar(nombre="Lautaro"):
    print(f"Hola, {nombre}!")  # La función saluda a la persona cuyo nombre se le pase como argumento, o a "Lautaro" si no se proporciona ningún argumento

saludar()  # Imprime "Hola, Lautaro!" ya que no se proporciona ningún argumento
saludar("María")  # Imprime "Hola, María!" ya que se proporciona el argumento "María".

#La palabra reservada "return" se utiliza para devolver un valor desde una función. Si no se especifica un valor de retorno, la función devolverá "None" por defecto. Además, esta palabra concluye la ejecución de la función, por lo que cualquier código después de "return" no se ejecutará.

#La ejecución de la función requiere que se le pasen los argumentos necesarios, a menos que tengan valores predeterminados. Si se llama a una función sin proporcionar los argumentos requeridos, se generará un error.


#---------FUNCIONES LAMBDA---------#
#Las funciones lambda, también conocidas como funciones anónimas, son funciones pequeñas y sin nombre que se pueden definir en una sola línea de código. Se utilizan principalmente para operaciones simples y se definen utilizando la palabra reservada "lambda". Por ejemplo:

suma = lambda x, y: x + y  # Define una función lambda que suma dos números. El formato general de una función lambda es "lambda argumentos: expresión". En este caso, "x" y "y" son los argumentos, y "x + y" es la expresión que se evalúa y se devuelve como resultado de la función lambda.
print(suma(3, 5))  # Imprime el resultado de la función lambda con los argumentos 3 y 5 (8)

#Podemos utilizar las funciones convencionales combinadas con las funciones lambda para realizar fábricas de funciones. Por ejemplo: Supongamos que quisieramos definir una función que duplique un valor, otra que triplique y otra que lo cuadriplique. Podríamos hacerlo de la siguiente manera:

def producto(n):
    return lambda x: x * n  # La función producto devuelve una función lambda que multiplica su argumento "x" por el valor "n" que se le pasó a la función producto.

duplicar = producto(2)  # Crea una función lambda que duplica un valor
triplicar = producto(3)  # Crea una función lambda que triplica un valor
cuadriplicar = producto(4)  # Crea una función lambda que cuadriplica un valor

print(duplicar(5))  # Imprime el resultado de la función lambda que duplica el valor 5 (10)
print(triplicar(5))  # Imprime el resultado de la función lambda que triplica el valor 5 (15)
print(cuadriplicar(5))  # Imprime el resultado de la función lambda que cuadriplica el valor 5 (20)

#---------MODULARIZACIÓN DE ARCHIVOS---------#
#En Python, es posible organizar el código en diferentes archivos para mejorar la modularización y la reutilización. Para utilizar funciones o variables definidas en otro archivo, se puede importar ese archivo utilizando la palabra reservada "import". Por ejemplo, si tenemos un archivo llamado "operaciones.py" con funciones matemáticas, podemos importarlo en otro archivo llamado "modularizacion.py" de la siguiente manera:

from operaciones import sumar, restar, multiplicar, dividir  # Importa las funciones sumar, restar, multiplicar y dividir desde el archivo operaciones.py

#Ahora podremos utilizar cualquier de las funciones en este nuevo archivo. Por ejemplo:
print(sumar(3, 7))  # Imprime el resultado de la función sumar con los argumentos 3 y 7 (10)
print(restar(10, 3))  # Imprime el resultado de la función restar con los argumentos 10 y 3 (7)
print(multiplicar(4, 5))  # Imprime el resultado de la función multiplicar con los argumentos 4 y 5 (20)
print(dividir(20, 4))  # Imprime el resultado de la función dividir con los argumentos 20 y 4 (5.0)

