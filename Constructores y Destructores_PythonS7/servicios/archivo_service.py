from modelos.archivo import Archivo

class ArchivoService:
    """
    Servicio que gestiona operaciones sobre archivos.
    """

    def crear_y_escribir_archivo(self, nombre, texto):
        """
        Crea un archivo y escribe información dentro.
        """
        archivo = Archivo(nombre)
        archivo.escribir(texto)

        # Al salir del método, el objeto puede ser destruido
        # dependiendo del recolector de basura
        return archivo

