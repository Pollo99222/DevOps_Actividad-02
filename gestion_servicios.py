# gestion_servicios.py
from datetime import datetime

class GestionServicios:
    historial_servicios = {} # Tabla hash para el historial de servicios

    @staticmethod
    def agregarServicio(nombreCliente, detallesServicio, descripcion):
        """Registra una solicitud de servicio con descripción y fecha."""
        fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        servicio = {
            "detalles": detallesServicio,
            "descripcion": descripcion,
            "fecha_creacion": fecha_creacion
        }
        
        if nombreCliente in GestionServicios.historial_servicios:
            GestionServicios.historial_servicios[nombreCliente].append(servicio)
        else:
            GestionServicios.historial_servicios[nombreCliente] = [servicio]
        
        print(f"Servicio agregado para '{nombreCliente}' con fecha {fecha_creacion}.")

    @staticmethod
    def consultarServicios(nombreCliente):
        """Obtiene el historial de servicios solicitados para el cliente."""
        return GestionServicios.historial_servicios.get(nombreCliente, None)
