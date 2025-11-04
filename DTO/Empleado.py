from DTO.Persona import Persona

class Empleado(Persona):
    def __init__(self, run, nombre, direccion = None, telefono = None, correo = None, fecha_inicio = None, salario = 0.0, departamento_id = None):
        super().__init__(run, nombre, direccion, telefono, correo)
        # Privados
        self._fecha_Inicio = fecha_inicio
        self._salario = salario
        self._departamento_id = departamento_id

        # Publicos
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

    def get_fecha_Inicio(self):
        return self._fecha_Inicio
    
    def get_salario(self):
        return self._salario
    
    def get_departamento(self):
        return self._departamento
    
    def info(self):
        base = super().info()
        return f"{base} | Empleado - Fecha inicio: {self._fecha_Inicio} | Salario: {self._salario} | Dep_id: {self._departamento_id}"
    
    def __str__(self):
        return self.info()