# cliente_manager.py
from gestion_clientes import GestionClientes
from gestion_servicios import GestionServicios
from almacenamiento_archivos import AlmacenamientoArchivos
from busqueda_clientes import BusquedaClientes

def main():
    while True:
        print("\n--- Menú de Gestión de Clientes ---")
        print("1. Crear Cliente")
        print("2. Solicitar Servicio")
        print("3. Consultar Historial de Servicios")
        print("4. Listar Clientes")
        print("5. Buscar Cliente")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del cliente: ")
            datosCliente = f"Cliente: {nombre}\nServicio solicitado: Ninguno"
            if GestionClientes.crearCliente(nombre, datosCliente):
                AlmacenamientoArchivos.crearArchivoCliente(nombre, datosCliente)

        elif opcion == "2":
            nombre = input("Nombre del cliente: ")
            servicio = input("Servicio solicitado: ")
            descripcion = input("Descripción del servicio: ")
            
            if GestionClientes.verificarCliente(nombre):
                # Agregar el servicio al historial y actualizar el registro de cliente
                GestionServicios.agregarServicio(nombre, servicio, descripcion)
                GestionClientes.actualizarCliente(nombre, f"Servicio solicitado: {servicio}")
                AlmacenamientoArchivos.actualizarArchivoCliente(nombre, f"Servicio solicitado: {servicio}\nDescripción: {descripcion}")
            else:
                print(f"Cliente '{nombre}' no encontrado. Por favor, créelo primero.")

        elif opcion == "3":
            nombre = input("Nombre del cliente: ")
            servicios = GestionServicios.consultarServicios(nombre)
            if servicios:
                print(f"Historial de servicios para {nombre}:")
                for servicio in servicios:
                    print(f"  - Detalles: {servicio['detalles']}")
                    print(f"  - Descripción: {servicio['descripcion']}")
                    print(f"  - Fecha de creación: {servicio['fecha_creacion']}")
            else:
                print(f"No se encontraron servicios para el cliente '{nombre}'.")

        elif opcion == "4":
            clientes = BusquedaClientes.listarClientes()
            print("Clientes registrados:")
            for cliente in clientes:
                print(f"- {cliente}")

        elif opcion == "5":
            nombre = input("Nombre del cliente: ")
            informacion = BusquedaClientes.buscarClientePorNombre(nombre)
            if informacion:
                print(f"Información de '{nombre}':\n{informacion}")
            else:
                print(f"Cliente '{nombre}' no encontrado.")

        elif opcion == "6":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
