# Importamos la clase Producto


# Clase Inventario
# Se encarga de gestionar todos los productos
class Inventario:
    def __init__(self):
        # Lista que almacena los productos del inventario
        self.productos = []
    # Método para agregar un nuevo producto
    def agregar_producto(self, producto):
        # Validamos que el ID no esté repetido
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: El ID del producto ya existe.")
                return

        # Si el ID es único, se agrega el producto
        self.productos.append(producto)
        print("Producto agregado correctamente.")

    # Método para eliminar un producto por su ID
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado correctamente.")
                return

        # Si no se encuentra el producto
        print(" Producto no encontrado.")

    # Método para actualizar cantidad y/o precio de un producto
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                # Actualiza solo los valores enviados
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)

                print(" Producto actualizado correctamente.")
                return

        print(" Producto no encontrado.")

    # Método para buscar productos por nombre (coincidencias parciales)
    def buscar_por_nombre(self, nombre):
        resultados = []

        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                resultados.append(p)

        return resultados

    def buscar_por_id(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                return p
        return None

    # Método para mostrar todos los productos del inventario
    def listar_productos(self):
        if not self.productos:
            print(" El inventario está vacío.")
        else:
            print("\n LISTA DE PRODUCTOS:")
            for p in self.productos:
                print(p)