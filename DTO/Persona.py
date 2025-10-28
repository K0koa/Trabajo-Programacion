class Persona():
    def __init__(self, id, nombre, direccion = None, telefono = None, correo = None):
        # Protegidos
        self._id = id
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo
        self._user_id = None

        #publicos
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.user_id = None

    def get_id(self):
        return self._id
    
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
    
    def info(self):
        return f"Persona: {self._nombre} (ID: {self._id})"
    
    def __str__(self):
        return self.info()