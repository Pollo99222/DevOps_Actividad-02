# almacenamiento_archivos.py
import os

DIRECTORIO_CLIENTES = "clientes"

class AlmacenamientoArchivos:
    
    @staticmethod
    def crearArchivoCliente(nombreCliente, datosCliente):
        """Crea un archivo de cliente y guarda los datos iniciales."""
        if not os.path.exists(DIRECTORIO_CLIENTES):
            os.makedirs(DIRECTORIO_CLIENTES)
        
        ruta_archivo = os.path.join(DIRECTORIO_CLIENTES, f"{nombreCliente}.txt")
        with open(ruta_archivo, "w") as archivo:
            archivo.write(datosCliente)
        print(f"Archivo para '{nombreCliente}' creado.")
    
    @staticmethod
    def actualizarArchivoCliente(nombreCliente, datosActualizados):
        """Modifica el archivo existente del cliente."""
        ruta_archivo = os.path.join(DIRECTORIO_CLIENTES, f"{nombreCliente}.txt")
        with open(ruta_archivo, "a") as archivo:
            archivo.write("\n" + datosActualizados)
        print(f"Archivo para '{nombreCliente}' actualizado.")
    
    @staticmethod
    def buscarArchivoCliente(nombreCliente):
        """Busca y retorna el contenido del archivo de un cliente."""
        ruta_archivo = os.path.join(DIRECTORIO_CLIENTES, f"{nombreCliente}.txt")
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, "r") as archivo:
                return archivo.read()
        else:
            print(f"No se encontró el archivo para '{nombreCliente}'.")
            return None
