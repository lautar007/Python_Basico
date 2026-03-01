#En este archivo definiremos las funciones para manejar el archivo de texto que se utilizará para almacenar la lista de compras. Estas funciones serán utilizadas en el archivo main.py para realizar las acciones correspondientes según la opción seleccionada por el usuario.

def agregar_producto(producto):
    try: 
        with open("lista_compras.txt", "a") as archivo: #Abrimos el archivo en modo de escritura (append) para agregar el producto al final del archivo.
            archivo.write(producto + "\n") #Escribimos el producto en el archivo seguido de un salto de línea.
    except Exception as e:
        print(f"Error al agregar el producto: {e}")

def mostrar_lista():
    try:
        with open("lista_compras.txt", "r") as archivo: #Abrimos el archivo en modo de lectura para mostrar la lista de compras.
            productos = archivo.readlines() #Leemos todas las líneas del archivo y las almacenamos en una lista.
            if not productos:
                print("La lista de compras está vacía.")
            else:
                print("Lista de compras:")
                for idx, producto in enumerate(productos, start=1):
                    print(f"{idx}. {producto.strip()}") #Mostramos cada producto con su número correspondiente, eliminando el salto de línea.
    except FileNotFoundError:
        print("Error: El archivo de la lista de compras no existe.")
    except Exception as e:
        print(f"Error al mostrar la lista de compras: {e}")


def modificar_producto(producto, nuevo_producto):
    try:
        with open("lista_compras.txt", "r") as archivo:
            lineas = [linea.strip() for linea in archivo.readlines()] #Leemos todas las líneas del archivo y las almacenamos en una lista, eliminando los saltos de línea.
            #Si el producto a modificar no se encuentra en la lista, se muestra un mensaje de error.
            if producto.lower() not in [linea.lower() for linea in lineas]:
                raise ValueError("Producto no encontrado en la lista. Intente de nuevo o ingrese un nuevo producto.")
            
        with open("lista_compras.txt", "w") as archivo:
            for linea in lineas:
                if linea.lower() == producto.lower():
                    archivo.write(nuevo_producto + "\n")
                else:
                    archivo.write(linea + "\n")
    except FileNotFoundError:
        print("Error: El archivo de la lista de compras no existe.")
    except Exception as e:
        print(f"Error al modificar el producto: {e}")

def eliminar_producto(producto):
    try:
        with open("lista_compras.txt", "r") as archivo:
            lineas = [linea.strip() for linea in archivo.readlines()] #Leemos todas las líneas del archivo y las almacenamos en una lista, eliminando los saltos de línea.
            #Si el producto a modificar no se encuentra en la lista, se muestra un mensaje de error.
            if producto.lower() not in [linea.lower() for linea in lineas] :
                raise ValueError("Producto no encontrado en la lista. Intente de nuevo.")
        with open("lista_compras.txt", "w") as archivo:
            for linea in lineas:
                if linea.lower() != producto.lower():
                    archivo.write(linea + "\n")
    except FileNotFoundError:
        print("Error: El archivo de la lista de compras no existe.")
    except Exception as e:
        print(f"Error al eliminar el producto: {e}")
