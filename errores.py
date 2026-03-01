#---------MANEJO DE ERRORES CON TRY-EXCEPT---------#
#En Python, el manejo de errores se realiza utilizando bloques de código "try-except". El bloque "try" contiene el código que se desea ejecutar, mientras que el bloque "except" maneja las excepciones o errores que puedan ocurrir durante la ejecución del bloque "try". Por ejemplo:

try:
    resultado = 10 / 0  # Esto generará un error de división por cero   
except ZeroDivisionError:  # Captura el error específico de división por cero
    print("Error: No se puede dividir por cero.")  # Imprime un mensaje de error personalizado

#Esto sirve para evitar que el programa se detenga abruptamente debido a un error, y en su lugar, permite ejecutar un código de contingencia para manejar el error de manera controlada. También es posible capturar múltiples tipos de errores utilizando varios bloques "except". Otra aplicación es para controlar que no se llamen variables que no han sido definidas, lo cual generaría un error de "NameError".

try:
    print(variable_no_definida)  # Esto generará un error de "NameError" ya que la variable no ha sido definida
except NameError:  # Captura el error específico de "NameError"
    print("Error: La variable no ha sido definida.")  # Imprime un mensaje de error personalizado
finally:
    print("Este bloque de código se ejecutará siempre, independientemente de si ocurrió un error o no.")  # El bloque "finally" se ejecuta siempre, incluso si se produjo un error o si se manejó correctamente en el bloque "except". Es útil para realizar tareas de limpieza o liberar recursos, como cerrar archivos o conexiones a bases de datos.



