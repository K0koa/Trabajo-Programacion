
class Persona:
    def __init__(self, run, nombre, direccion=None, telefono=None, correo=None):
        self._run = run #protegidos
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo
        self._user_id = None

        self.run = run #públicos
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.user_id = None

    #Métodos getters para encapsulamiento
    def get_run(self):
        return self._run

    def get_nombre(self):
        return self._nombre

    def get_direccion(self):
        return self._direccion

    def get_telefono(self):
        return self._telefono

    def get_correo(self):
        return self._correo

    def get_user_id(self):
        return self._user_id

    #APlicar polimorfismo
    def info(self):
        return f"Persona: {self._nombre} (RUN: {self._run})"

    def __str__(self):
        return self.info()
