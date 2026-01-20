class Archivo:
    """
    Clase que representa un archivo del sistema.
    Demuestra el uso de constructor y destructor con tipado de datos.
    """

    def __init__(self, nombre_archivo: str, modo: str = "w") -> None:
        """
        Constructor:
        Inicializa los atributos del objeto y abre el archivo.

        :param nombre_archivo: Nombre del archivo (tipo string)
        :param modo: Modo de apertura del archivo (tipo string)
        """
        self.nombre_archivo: str = nombre_archivo
        self.modo: str = modo
        self.archivo = open(self.nombre_archivo, self.modo)

        print(f"[INIT] Archivo '{self.nombre_archivo}' abierto en modo '{self.modo}'")

    def escribir(self, texto: str) -> None:
        """
        Escribe texto dentro del archivo.
        """
        self.archivo.write(texto + "\n")

    def __del__(self) -> None:
        """
        Destructor:
        Cierra el archivo y libera el recurso cuando el objeto deja de existir.
        """
        if not self.archivo.closed:
            self.archivo.close()
            print(f"[DEL] Archivo '{self.nombre_archivo}' cerrado correctamente")
