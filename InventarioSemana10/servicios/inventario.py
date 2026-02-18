
# Clase Inventario
# Maneja la lógica del sistema y la
# manipulación del archivo inventario.txt


from modelos.producto import Producto


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        """
        Constructor del inventario.
        - archivo: nombre del archivo donde se guardan los datos.
        - productos: diccionario donde se almacenan los productos en memoria.
        """
        self.archivo = archivo
        self.productos = {}

        # Al iniciar el programa se cargan los datos del archivo
        self.cargar_desde_archivo()


    # MÉTODO PARA CARGAR LOS PRODUCTOS DESDE EL ARCHIVO

    def cargar_desde_archivo(self):
        """
        Lee el archivo inventario.txt y reconstruye
        los productos guardados previamente.
        """

        try:
            # 'r' = modo lectura
            # with asegura que el archivo se cierre automáticamente
            with open(self.archivo, "r") as file:
                for linea in file:
                    datos = linea.strip().split(",")

                    # Verificamos que la línea tenga el formato correcto
                    if len(datos) == 4:
                        codigo, nombre, cantidad, precio = datos

                        # Se convierte cantidad y precio a su tipo correcto
                        self.productos[codigo] = Producto(
                            codigo,
                            nombre,
                            int(cantidad),
                            float(precio)
                        )

        except FileNotFoundError:
            # Si el archivo no existe, se crea automáticamente
            print("Archivo no encontrado. Se creará uno nuevo.")
            with open(self.archivo, "w") as file:
                pass  # Se crea vacío

        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")

        except Exception as e:
            # Captura cualquier otro error inesperado
            print("Error inesperado al cargar archivo:", e)


    # MÉTODO PARA GUARDAR LOS PRODUCTOS EN EL ARCHIVO

    def guardar_en_archivo(self):
        """
        Guarda todos los productos del diccionario
        en el archivo inventario.txt.

        Se usa modo 'w' (sobrescritura), lo que significa
        que primero borra el contenido anterior y luego
        escribe los datos actualizados.
        """

        try:
            # 'w' = modo escritura (sobrescribe el archivo)
            with open(self.archivo, "w") as file:
                for producto in self.productos.values():
                    file.write(str(producto) + "\n")

        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")

        except Exception as e:
            print("Error inesperado al guardar archivo:", e)


    # AGREGAR PRODUCTO

    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al inventario.
        Luego actualiza el archivo automáticamente.
        """

        if producto.codigo in self.productos:
            print("El producto ya existe.")
        else:
            self.productos[producto.codigo] = producto
            self.guardar_en_archivo()  # Se guarda en archivo
            print("Producto agregado y guardado correctamente.")


    # ACTUALIZAR PRODUCTO

    def actualizar_producto(self, codigo, cantidad, precio):
        """
        Modifica la cantidad y precio de un producto existente.
        """

        if codigo in self.productos:
            self.productos[codigo].cantidad = cantidad
            self.productos[codigo].precio = precio
            self.guardar_en_archivo()
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")


    # ELIMINAR PRODUCTO

    def eliminar_producto(self, codigo):
        """
        Elimina un producto del inventario.
        """

        if codigo in self.productos:
            del self.productos[codigo]
            self.guardar_en_archivo()
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")


    # MOSTRAR PRODUCTOS

    def mostrar_productos(self):
        """
        Muestra todos los productos almacenados
        actualmente en memoria.
        """

        if not self.productos:
            print("Inventario vacío.")
        else:
            for producto in self.productos.values():
                print(producto)
