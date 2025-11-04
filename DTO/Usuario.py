from DAO.Conexion import Conexion
import bcrypt

host = 'localhost'
user = 'ecosolutions'
password = '3k0Z0iuTloNz'
db = 'ecotech solutions'

class Usuario:
    def __init__(self, username, password_hash, nombre, apellidos, email, tipo_usuario):
        self.username = username
        self.password_hash = password_hash
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.tipo_usuario = tipo_usuario

    @staticmethod
    def login(username, password):
        con = Conexion(host, user, password, db)
        datos = con.obtenerUsuario(username)
        if datos and len(datos) == 1:
            datos = datos[0]
            hashed_password = datos[2].encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                return Usuario(
                    username=datos[1],
                    password_hash=datos[2],
                    nombre=datos[3],
                    apellidos=datos[4],
                    email=datos[5],
                    tipo_usuario=datos[6]
                )
        return None
    
    @staticmethod
    def registrar_usuario(username, password, nombre, apellidos, email, tipo_usuario):
        # generar el hash de la contraseña utilizando bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        nuevo_usuario = Usuario(
            username=username,
            password_hash=hashed_password,
            nombre=nombre,
            apellidos=apellidos,
            email=email,
            tipo_usuario=tipo_usuario
        )

        con = Conexion(host, user, password, db)
        con.error = None
        exito = con.agregaUsuario(
            username=nuevo_usuario.username,
            password_hash=nuevo_usuario.password_hash_decode('utf-8'),
            nombre=nuevo_usuario.nombre,
            apellidos=nuevo_usuario.apellidos,
            email=nuevo_usuario.email,
            tipo_usuario=nuevo_usuario.tipo_usuario
        )

        if exito:
            print("Usuario registrado exitosamente.")
            return nuevo_usuario
        else:
            if con.error == "Duplicado":
                print("El usuario ya existe.")
            elif con.error is not None:
                print("Error al registrar el usuario:", con.error)
            else:
                print("Error al registrar el usuario.")
            return None