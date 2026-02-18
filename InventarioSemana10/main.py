
# Programa principal
# Maneja la interfaz de usuario en consola


from modelos.producto import Producto
from servicios.inventario import Inventario

def mostrar_menu():
    """
    Muestra el menú principal del sistema.
    """
    print("SISTEMA DE INVENTARIO")
    print("1. Agregar producto")
    print("2. Actualizar producto")
    print("3. Eliminar producto")
    print("4. Mostrar productos")
    print("5. Salir")

def main():
    """
    Función principal que controla el flujo del programa.
    """
    inventario = Inventario()  # Se carga el inventario desde el archivo

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                codigo = input("Código: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))  # Puede generar ValueError
                precio = float(input("Precio: "))

                producto = Producto(codigo, nombre, cantidad, precio)
                inventario.agregar_producto(producto)

            elif opcion == "2":
                codigo = input("Código del producto: ")
                cantidad = int(input("Nueva cantidad: "))
                precio = float(input("Nuevo precio: "))
                inventario.actualizar_producto(codigo, cantidad, precio)

            elif opcion == "3":
                codigo = input("Código del producto: ")
                inventario.eliminar_producto(codigo)

            elif opcion == "4":
                inventario.mostrar_productos()

            elif opcion == "5":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida.")

        except ValueError:
            # Maneja errores cuando el usuario ingresa texto en lugar de número
            print("Error: Debe ingresar valores numéricos válidos.")

        except Exception as e:
            # Captura cualquier error inesperado
            print("Error inesperado:", e)

# Punto de entrada del programa
if __name__ == "__main__":
    main()
