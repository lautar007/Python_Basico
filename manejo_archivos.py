#---------LECTURA Y ESCRITURA DE ARCHIVOS EN PYTHON---------#
#En Python, es posible leer y escribir archivos utilizando funciones integradas. Para abrir un archivo, se utiliza la función "open()", que toma como argumento el nombre del archivo y el modo de apertura (lectura, escritura, etc.). Para tener mayor control sobre estas operaciones es recomendable usar bloques try-except para manejar posibles errores, como que el archivo no exista o que no se tengan permisos para acceder a él.

try:
    archivo = open("texto.txt", "r")  # Abre el archivo "archivo.txt" en modo de lectura ("r")
    contenido = archivo.read()  # Lee el contenido del archivo y lo almacena en la variable "contenido"
    print(contenido)  # Imprime el contenido del archivo
except FileNotFoundError:  # Captura el error específico de "FileNotFoundError" si el archivo no existe
    print("Error: El archivo no existe.")  # Imprime un mensaje de error personalizado

#Los modos que se pueden utilizar para abrir un archivo son:
#- "r": Modo de lectura (read). Es el modo predeterminado. Permite leer el contenido del archivo, pero no modificarlo. Si el archivo no existe, se generará un error.
#- "w": Modo de escritura (write). Permite escribir en el archivo. Si el archivo ya existe, se sobrescribirá su contenido. Si el archivo no existe, se creará uno nuevo.
#- "a": Modo de anexado (append). Permite agregar contenido al final del archivo sin sobrescribirlo. Si el archivo no existe, se creará uno nuevo.
#- "x": Modo de creación exclusiva (exclusive creation). Permite crear un nuevo archivo. Si el archivo ya existe, se generará un error.

#Esto permite controlas las acciones que se pueden realizar sobre el archivo y evitar errores no deseados. Además, es importante cerrar el archivo después de haber terminado de trabajar con él utilizando el método "close()". Sin embargo, una forma más segura y recomendada de manejar archivos es utilizando la declaración "with", que garantiza que el archivo se cierre automáticamente después de su uso, incluso si ocurre un error durante la manipulación del archivo. Por ejemplo:

try:
    with open("texto.txt", "r") as archivo:  # Abre el archivo "archivo.txt" en modo de lectura ("r") utilizando la declaración "with"
        contenido = archivo.read()  # Lee el contenido del archivo y lo almacena en la variable "contenido"
        print(contenido)  # Imprime el contenido del archivo    
except FileNotFoundError:  # Captura el error específico de "FileNotFoundError" si el archivo no existe
    print("Error: El archivo no existe.")  # Imprime un mensaje de error personalizado

#Por defecto la función open maneja el archivo de texto en formato unicode, pero también es posible especificar el formato utilizando el parámetro "encoding". Por ejemplo, para abrir un archivo en formato UTF-8, se puede hacer de la siguiente manera:

try:
    with open("texto.txt", "r", encoding="utf-8") as archivo:  # Abre el archivo "archivo.txt" en modo de lectura ("r") con codificación UTF-8 utilizando la declaración "with"
        contenido = archivo.read()  # Lee el contenido del archivo y lo almacena en la variable "contenido"
        print(contenido)  # Imprime el contenido del archivo    
except FileNotFoundError:  # Captura el error específico de "FileNotFoundError" si el archivo no existe
    print("Error: El archivo no existe.")  # Imprime un mensaje de error personalizado
    
#Esto es importante sobre todo en idiomas que tienen acentos, como el español. 


#Ejemplo de escritura: 
try:
    with open("nuevo_archivo.txt", "w") as archivo:  # Abre el archivo "nuevo_archivo.txt" en modo de escritura ("w") utilizando la declaración "with"
        archivo.write("Hola, este es un nuevo contenido para el archivo.")  # Escribe el texto "Hola, este es un nuevo contenido para el archivo." en el archivo.
except Exception as e:  # Captura cualquier tipo de error que pueda ocurrir durante la escritura del archivo
    print(f"Error: {e}")  # Imprime un mensaje de error personalizado con la descripción del error capturado    

#Es importante aclarar que este código sobrescribirá el contenido del archivo "nuevo_archivo.txt" si este ya existe. Si se desea agregar contenido al final del archivo sin sobrescribirlo, se debe utilizar el modo de apertura "a" en lugar de "w". Por ejemplo:
try:
    with open("nuevo_archivo.txt", "a") as archivo:  # Abre el archivo "nuevo_archivo.txt" en modo de anexado ("a") utilizando la declaración "with"
        archivo.write("\nEste es un nuevo contenido agregado al final del archivo.")  # Agrega el texto "\nEste es un nuevo contenido agregado al final del archivo." al final del archivo. El carácter "\n" se utiliza para agregar una nueva línea antes del nuevo contenido.
except Exception as e:  # Captura cualquier tipo de error que pueda ocurrir durante la escritura del archivo
    print(f"Error: {e}")  # Imprime un mensaje de error personalizado con la descripción del error capturado.


