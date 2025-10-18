class Persona():
    def __init__(self, id, nombre, apellido, correo, telefono):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
    
    def mostrar_info(self):
        return f"{self.nombre} {self.apellido} - {self.correo}"
