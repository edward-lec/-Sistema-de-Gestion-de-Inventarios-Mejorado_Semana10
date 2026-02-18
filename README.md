**1. Introducción**

El presente proyecto consiste en el desarrollo de un Sistema de Gestión de Inventarios mejorado, implementado en Python, aplicando los conceptos de Programación Orientada a Objetos, manipulación de archivos y manejo de excepciones.

El objetivo principal es permitir el almacenamiento persistente de productos en un archivo de texto (inventario.txt), garantizando que la información no se pierda al cerrar el programa y asegurando un manejo adecuado de errores durante la ejecución.

**2. Estructura del Programa**

El sistema está organizado en tres módulos principales:

producto.py → Define la clase Producto.

inventario.py → Contiene la lógica del sistema y la manipulación de archivos.

main.py → Maneja la interfaz de usuario en consola.

Esta estructura permite mantener el código organizado y modular.

**3. Funcionamiento del Sistema**


**3.1 Clase Producto**

Representa cada artículo del inventario con los siguientes atributos:

Código

Nombre

Cantidad

Precio

Incluye el método especial __str__() que permite convertir el objeto en formato texto para almacenarlo en el archivo.

Formato de almacenamiento:

codigo,nombre,cantidad,precio

**3.2 Clase Inventario**

Es la clase principal del sistema. Sus funciones principales son:

Cargar productos desde el archivo al iniciar el programa.

Guardar productos en el archivo después de cada modificación.

Agregar productos.

Actualizar productos.

Eliminar productos.

Mostrar productos almacenados.

**4. Manipulación de Archivos**

El programa utiliza la función open() con diferentes modos:

'r' → Para lectura del archivo.

'w' → Para sobrescribir el archivo con datos actualizados.

Se utiliza la estructura with para asegurar el cierre automático del archivo, evitando pérdida de datos o bloqueos.

Cuando el archivo no existe, el sistema lo crea automáticamente.

**5. Manejo de Excepciones**

El programa implementa estructuras try y except para evitar que errores interrumpan la ejecución.

Se manejan las siguientes excepciones:

FileNotFoundError → Si el archivo no existe.

PermissionError → Si no hay permisos de lectura o escritura.

ValueError → Si el usuario ingresa datos incorrectos (por ejemplo, texto en lugar de números).

Exception → Para capturar errores inesperados.

Esto mejora la robustez y estabilidad del sistema.

**6. Interfaz de Usuario**

El sistema presenta un menú interactivo en consola que permite al usuario:

Agregar producto

Actualizar producto

Eliminar producto

Mostrar productos

Salir

Después de cada operación, el sistema informa si fue exitosa o si ocurrió algún error.

**7. Persistencia de Datos**

Una de las mejoras principales del sistema es la persistencia de datos.
Los productos agregados se guardan en el archivo inventario.txt, lo que permite que la información se mantenga incluso después de cerrar el programa.

Al reiniciar el sistema, los datos se cargan automáticamente.

**8. Conclusión**

El sistema desarrollado cumple con los requisitos establecidos en la semana 10, integrando correctamente:

Programación Orientada a Objetos.

Manipulación de archivos.

Manejo de excepciones.

Persistencia de datos.

El programa es funcional, organizado y robusto ante errores comunes, demostrando la aplicación práctica de los conceptos estudiados.
