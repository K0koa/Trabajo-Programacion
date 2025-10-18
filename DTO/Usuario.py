from DTO.Persona import Persona

class Usuario(Persona):
    def __init__(self, id, nombre, apellido, correo, telefono, clave, acceso):
        super().__init__(id, nombre, apellido, correo, telefono)
        self.clave = clave
        self.acceso = acceso