class RegistroTiempo():
    def __init__(self, empleado_id, proyecto_id, fecha, hora, descripcion = None):
        self.empleado_id = empleado_id
        self.proyecto_id = proyecto_id
        self.fechas = fecha
        self.horas = hora
        self.descripcion = descripcion
        self.user_id = None