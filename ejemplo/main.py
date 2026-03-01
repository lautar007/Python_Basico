#En este archivo tendremos la funcionalidad principal de un programa de ejemplo para implementar lo visto en el proyecto.

#Este programa se encargará de generar, ecribir, leer y modificar un archivo de texto en la que se guardará una lista de productos que se necesitan adquirir. Es decir, una aplicación de listas de compras. 
#El programa tendrá un menú de opciones para que el usuario pueda elegir qué acción desea realizar. Las opciones serán:
# 1. Agregar un producto a la lista de compras.
# 2. Mostrar la lista de compras.
# 3. Modificar un producto de la lista de compras.
# 4. Eliminar un producto de la lista de compras.
# 5. Salir del programa.

from func_de_lista import agregar_producto, mostrar_lista, modificar_producto, eliminar_producto

def main():

    while True: #Bucle infinito para mostrar el menú de opciones hasta que el usuario decida salir.
        print("\n--- Aplicación de Lista de Compras ---", "Bienvenido")
        print("Menú de opciones:")
        print("1. Agregar un producto a la lista de compras.")
        print("2. Mostrar la lista de compras.")
        print("3. Modificar un producto de la lista de compras.")
        print("4. Eliminar un producto de la lista de compras.")
        print("5. Salir del programa.")

        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            producto = input("Ingrese el nombre del producto que desea agregar: ")
            #Aquí se podría agregar código para escribir el producto en un archivo de texto.
            try:
                agregar_producto(producto)
            except Exception as e:
                print(f"Error al agregar el producto: {e}")
            else:
                print(f"Producto '{producto}' agregado a la lista de compras.")
            
            input("Presione Enter para continuar...") #Pausa para que el usuario pueda leer el mensaje antes de mostrar el menú nuevamente.

        elif opcion == "2":
            mostrar_lista()
            input("Presione Enter para continuar...")
               
        elif opcion == "3":
            producto = input("Ingrese el nombre del producto que desea modificar: ")
            nuevo_producto = input("Ingrese el nuevo nombre del producto: ")
            try:
                modificar_producto(producto, nuevo_producto)
            except Exception as e:
                print(f"Error al modificar el producto: {e}")
            else:
                print(f"Producto '{producto}' modificado a '{nuevo_producto}' en la lista de compras.")
            input("Presione Enter para continuar...")


        elif opcion == "4":
            producto = input("Ingrese el nombre del producto que desea eliminar: ")
            try:
                eliminar_producto(producto)
            except Exception as e:
                print(f"Error al eliminar el producto: {e}")
            else:
                print(f"Producto '{producto}' eliminado de la lista de compras.")
            input("Presione Enter para continuar...")
            
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 5.")
            input("Presione Enter para continuar...") 

main()