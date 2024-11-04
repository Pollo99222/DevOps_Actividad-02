# gestion_clientes.py
class GestionClientes:
    clientes = {} # Tabla hash para almacenar la información de los clientes

    @staticmethod
    def verificarCliente(nombre):
        """Verifica si el cliente ya existe."""
        return nombre in GestionClientes.clientes

    @staticmethod
    def crearCliente(nombre, datosCliente):
        """Registra un nuevo cliente y crea su archivo."""
        if not GestionClientes.verificarCliente(nombre):
            GestionClientes.clientes[nombre] = datosCliente
            print(f"Cliente '{nombre}' creado.")
            return True
        else:
            print(f"Cliente '{nombre}' ya existe.")
            return False

    @staticmethod
    def actualizarCliente(nombre, nuevaSolicitud):
        """Actualiza el registro de un cliente existente."""
        if GestionClientes.verificarCliente(nombre):
            GestionClientes.clientes[nombre] += f"\n{nuevaSolicitud}"
            print(f"Cliente '{nombre}' actualizado con nueva solicitud.")
            return True
        else:
            print(f"Cliente '{nombre}' no existe.")
            return False
