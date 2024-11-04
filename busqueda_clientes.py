# busqueda_clientes.py
import os

DIRECTORIO_CLIENTES = "clientes"

class BusquedaClientes:
    
    @staticmethod
    def buscarClientePorNombre(nombre):
        """Busca y retorna la información de un cliente por nombre."""
        ruta_archivo = os.path.join(DIRECTORIO_CLIENTES, f"{nombre}.txt")
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, "r") as archivo:
                return archivo.read()
        else:
            print(f"No se encontró el archivo para '{nombre}'.")
            return None

    @staticmethod
    def listarClientes():
        """Devuelve una lista de todos los clientes registrados."""
        if os.path.exists(DIRECTORIO_CLIENTES):
            return [f.split(".")[0] for f in os.listdir(DIRECTORIO_CLIENTES) if f.endswith(".txt")]
        else:
            print("No hay clientes registrados.")
            return []
