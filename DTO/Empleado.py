# DTO/Empleado.py
from DTO.Persona import Persona

class Empleado(Persona):
    def __init__(self, run, nombre, direccion=None, telefono=None, correo=None, fecha_inicio=None, salario=0.0, departamento_id=None):
        super().__init__(run, nombre, direccion, telefono, correo)
        self._fecha_inicio = fecha_inicio
        self._salario = salario
        self._departamento_id = departamento_id
        self._user_id = None

        self.run = run
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.user_id = None
        self.fecha_inicio = fecha_inicio
        self.salario = salario
        self.departamento_id = departamento_id
        self.user_id = None

    #Métodos getters para encapsulamiento
    def get_fecha_inicio(self):
        return self._fecha_inicio

    def get_salario(self):
        return self._salario

    def get_departamento_id(self):
        return self._departamento_id

    def info(self):
        base = super().info()
        return f"{base} | Empleado - Fecha inicio: {self._fecha_inicio} | Salario: {self._salario} | Dept ID: {self._departamento_id}"

    def __str__(self):
        return self.info()