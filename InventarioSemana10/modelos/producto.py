
# Clase Producto
# Representa un producto dentro del inventario
# creado por: Leiber Correa

class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        Inicializa los atributos básicos del producto.
        """
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        """
        Método especial que convierte el objeto en texto.
        Se usa para guardar el producto en el archivo.
        Formato: codigo,nombre,cantidad,precio
        """
        return f"{self.codigo},{self.nombre},{self.cantidad},{self.precio}"
