# Importación de las clases necesarias desde los módulos del proyecto
from modelos.producto import Producto
from servicios.inventario import Inventario


# Función que muestra el menú principal del sistema
def mostrar_menu():
    print("SISTEMA DE GESTIÓN DE INVENTARIOS")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Listar inventario")
    print("6. Salir")


def main():
    # Creación del objeto Inventario
    # Este objeto gestionará todos los productos del sistema
    inventario = Inventario()

    # Bucle principal del programa
    # Permite que el menú se muestre hasta que el usuario decida salir
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        #  AÑADIR PRODUCTO
        if opcion == "1":
            # Solicitud de datos básicos del producto
            id_producto = input("Ingrese ID del producto: ").strip()
            nombre = input("Ingrese nombre del producto: ").strip()

            # Validación de campos obligatorios
            if not id_producto or not nombre:
                print(" El ID y el nombre no pueden estar vacíos.")
                continue

            # Validación de cantidad y precio
            try:
                cantidad = int(input("Ingrese cantidad: "))
                if cantidad < 0:
                    print(" La cantidad no puede ser negativa.")
                    continue

                precio = float(input("Ingrese precio: "))
                if precio <= 0:
                    print(" El precio debe ser mayor que cero.")
                    continue
            except ValueError:
                # Captura errores cuando el usuario ingresa valores no numéricos
                print(" Error: Ingrese valores numéricos válidos.")
                continue

            # Creación del objeto Producto
            producto = Producto(id_producto, nombre, cantidad, precio)

            # Se agrega el producto al inventario
            inventario.agregar_producto(producto)

        # ELIMINAR PRODUCTO
        elif opcion == "2":
            # Solicitud del ID del producto a eliminar
            id_producto = input("Ingrese ID del producto a eliminar: ").strip()

            # Validación del ID
            if not id_producto:
                print(" El ID no puede estar vacío.")
                continue

            # Llamada al método de eliminación
            inventario.eliminar_producto(id_producto)

        # ACTUALIZAR PRODUCTO
        elif opcion == "3":
            # Solicitud del ID del producto a actualizar
            id_producto = input("Ingrese ID del producto a actualizar: ").strip()

            if not id_producto:
                print(" El ID no puede estar vacío.")
                continue

            # El usuario puede actualizar uno o ambos valores
            cantidad = input("Nueva cantidad (Enter para no cambiar): ").strip()
            precio = input("Nuevo precio (Enter para no cambiar): ").strip()

            try:
                # Conversión condicional de los datos
                nueva_cantidad = int(cantidad) if cantidad else None
                if nueva_cantidad is not None and nueva_cantidad < 0:
                    print(" La cantidad no puede ser negativa.")
                    continue

                nuevo_precio = float(precio) if precio else None
                if nuevo_precio is not None and nuevo_precio <= 0:
                    print(" El precio debe ser mayor que cero.")
                    continue
            except ValueError:
                print(" Error: Ingrese valores numéricos válidos.")
                continue

            # Actualización del producto en el inventario
            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        # BUSCAR PRODUCTO
        elif opcion == "4":
            dato = input("Ingrese ID o nombre a buscar: ").strip()

            if not dato:
                print("El campo no puede estar vacío.")
                continue

            # Primero intenta buscar por ID
            producto = inventario.buscar_por_id(dato)
            if producto:
                print(producto)
            else:
                # Si no existe el ID, busca por nombre
                resultados = inventario.buscar_por_nombre(dato)
                if resultados:
                    for p in resultados:
                        print(p)
                else:
                    print("No se encontraron productos.")

        # LISTAR INVENTARIO
        elif opcion == "5":
            # Muestra todos los productos registrados
            inventario.listar_productos()

        # SALIR DEL SISTEMA
        elif opcion == "6":
            # Finaliza la ejecución del programa
            print(" Saliendo del sistema...")
            break

        # OPCIÓN INVÁLIDA
        else:
            # Control de opciones no válidas
            print(" Opción inválida. Intente nuevamente.")


# Punto de entrada del programa
# Garantiza que el archivo se ejecute correctamente como programa principal
if __name__ == "__main__":
    main()