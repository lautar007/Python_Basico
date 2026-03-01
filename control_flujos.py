#En este archivo veremos algunas estructuras que permiten controlar los flujos de ejecución de un programa, como operadores, condicionales y bucles.

#---------OPERADORES---------#
#Algunos de los operadores más comunes son:

#- Aritméticos: 
# + (suma), 
# - (resta), 
# * (multiplicación), 
# / (división), 
# % (módulo) este operador devuelve el resto de una división,  
# ** (exponenciación), 
# // (división entera) este operador devuelve la parte entera de una división.
#Los operadores matemáticos respetan la precedencia de operadores según las leyes aritméticas.

#- De comparación: 
# == (igual a), 
# != (diferente de), 
# > (mayor que), 
# < (menor que), 
# >= (mayor o igual que), 
# <= (menor o igual que).

#- Lógicos: and, or, not. Estos operadores se utilizan para combinar condiciones. 
# El operador "and" devuelve True si ambas condiciones son verdaderas, 
# el operador "or" devuelve True si al menos una de las condiciones es verdadera,
# y el operador "not()" invierte el valor de una condición (devuelve True si la condición es falsa y viceversa).

#- Asignación: 
# = (asignación simple),
# += (suma y asignación),
# -= (resta y asignación),
# *= (multiplicación y asignación),
# /= (división y asignación),
# %= (módulo y asignación),
# **= (exponenciación y asignación),
# //= (división entera y asignación).
#Estos operadores permiten realizar una operación y asignar el resultado a la variable al mismo tiempo. Por ejemplo, "x += 5" es equivalente a "x = x + 5".

#También existe una asignación conocido como "walrus operator" (operador morsa) representado por ":=", que permite asignar un valor a una variable como parte de una expresión. Por ejemplo, "if (n := len(cadena)) > 10:" asigna el valor de "len(cadena)" a la variable "n" y luego evalúa si "n" es mayor que 10.


#---------CONDICIONALES---------#
#Las estructuras condicionales permiten ejecutar diferentes bloques de código según ciertas condiciones. En Python, las estructuras condicionales más comunes son "if", "elif" y "else".

x = -1
if x > 3:
    print("x es mayor que 3")  
elif x < 3:
    print("x es menor que 3")  
else:
    print("x es igual a 3") 

#Dependiendo del valor de x, se ejecutará el bloque de código cuya condición sea verdadera.
#Esta estructura de datos, y otras también, pueden anidarse, es decir, pueden contener otras estructuras dentro de ellas.
#Es posible dejar un if vacío, en caso de que en cierta opción no querramos hacer nada, utilizando la palabra reservada "pass". Por ejemplo:

y = 5
if y > 10:
    print("y es mayor que 10")
else:   
    pass  # No se hace nada si y no es mayor que 10.

#Otra estructura condicional es match-case, que se utiliza para comparar el valor de una variable con diferentes casos posibles. Por ejemplo:

color = "rojo"
match color:
    case "rojo":
        print("El color es rojo.")
    case "azul":
        print("El color es azul.")
    case "verde":
        print("El color es verde.")
    case _:
        print("El color no es rojo, azul ni verde.")  # El caso "_" se utiliza como un caso por defecto para manejar cualquier valor que no coincida con los casos anteriores.

#---------BUCLES---------#
#Los bucles permiten ejecutar un bloque de código varias veces. En Python, los bucles más comunes son "for" y "while".

#El bucle "for" se utiliza para iterar sobre una secuencia de elementos, como una lista o una cadena de texto. Por ejemplo:

frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)  # Este bloque de código se ejecutará una vez por cada elemento en la lista "frutas", imprimiendo el nombre de cada fruta.

#El bucle "while" se utiliza para ejecutar un bloque de código mientras una condición sea verdadera. Por ejemplo:

contador = 0
while contador < 5:
    print(contador)  # Este bloque de código se ejecutará mientras el valor de "contador" sea menor que 5, imprimiendo el valor de "contador" en cada iteración.
    contador += 1  # Incrementamos el valor de "contador" en cada iteración para evitar un bucle infinito. Es fundamental tener una línea de código que modifique la condición del bucle para evitar que se ejecute indefinidamente.

#Es posible cortar una iteración antes de que termine utilizando la palabra reservada "break".
#También es posible saltar a la siguiente iteración utilizando la palabra reservada "continue".

#Los bucles también puede tener una cláusula "else" que se ejecuta cuando la condición del bucle deja de ser verdadera.

#Otra implementación del bucle for establece una cantidad de iteraciones utilizando la función range(). Por ejemplo:

for i in range(5):  # Este bloque de código se ejecutará 5 veces, con el valor de "i" tomando los valores 0, 1, 2, 3 y 4 en cada iteración.
    print(i)

#Nuevamente, estas estructuras también son anidables, es decir, pueden contener otras estructuras dentro de ellas. Es muy común anidar bucles for para recorrer matrices o listas de listas.


