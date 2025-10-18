from DTO.Persona import Persona

class Empleado(Persona):
    def __init__(self, id, nombre, apellido, correo, telefono, FechaContrato, salario):
        super().__init__(id, nombre, apellido, correo, telefono)
        self.FechaContrato = FechaContrato
        self.salario = salario
       