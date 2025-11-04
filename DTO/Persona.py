class Persona():
<<<<<<< HEAD
    def __init__(self, run, nombre, direccion = None, telefono = None, correo = None):
        # Protegidos
        self._run = run
=======
    def __init__(self, id, nombre, direccion = None, telefono = None, correo = None):
        # Protegidos
        self._id = id
>>>>>>> 30b4954ae90717eee331200485bf8ffe4f88aa6b
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo
        self._user_id = None

        #publicos
<<<<<<< HEAD
        self.run = run
=======
        self.id = id
>>>>>>> 30b4954ae90717eee331200485bf8ffe4f88aa6b
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.user_id = None

    def get_id(self):
<<<<<<< HEAD
        return self._run
=======
        return self._id
>>>>>>> 30b4954ae90717eee331200485bf8ffe4f88aa6b
    
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
<<<<<<< HEAD
        return f"Persona: {self._nombre} (run: {self._run})"
=======
        return f"Persona: {self._nombre} (ID: {self._id})"
>>>>>>> 30b4954ae90717eee331200485bf8ffe4f88aa6b
    
    def __str__(self):
        return self.info()