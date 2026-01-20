from servicios.archivo_service import ArchivoService

def main():
    print("=== Inicio del programa ===")

    servicio = ArchivoService()
    archivo = servicio.crear_y_escribir_archivo(
        "ejemplo.txt",
        "Este archivo demuestra el uso de __init__ y __del__"
    )

    print("El archivo fue creado y escrito correctamente.")

    # Eliminamos manualmente la referencia para forzar el destructor
    del archivo

    print("=== Fin del programa ===")

if __name__ == "__main__":
    main()
