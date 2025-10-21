from DAO.Conexion import Conexion

host = 'localhost'
user = 'ecosolutions'
password = '3k0Z0iuTloNz'
db = 'ecotech solutions'

def registrarUsuario(u):
    try:
        con = Conexion(host, user, password, db)
        sql = f"INSERT INTO USUARIO SET id = {u.id}, nombre = '{u.nombre}', apellido = '{u.apellido}', correo = '{u.correo}', telefono = '{u.telefono}', clave = '{u.clave}', acceso = '{u.acceso}'"
        con.ejecuta_query(sql)
        con.commit()
        input("\n\n Datos ingresados Satisfactoriamente")
        con.desconectar()
    except Exception as e:
        print(e)

def mostrarUsuario():
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT * FROM USUARIO"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as e:
        con.rollback()        
        print(e)

def buscarUsuario(id):
    try:
        con = Conexion(host, user, password, db)
        sql = f"SELECT * FROM USUARIO WHERE id = {id}"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchone()
        con.desconectar()
        return datos
    except Exception as e:
        con.rollback()        
        print(e)
        
def cosultaparcialUsuario(cant):
    try:
        con = Conexion(host, user, password, db)
        sql = f"SELECT * FROM USUARIO"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchmany(size = cant)
        con.desconectar()
        return datos
    except Exception as e:
        con.rollback()
        print(e)

def modificarUsuario(u):
    try:
        con = Conexion(host, user, password, db)
        sql = "UPDATE USUARIO SET nombre = '{}', apellido = '{}', correo = '{}'," \
        "telefono = '{}', clave = '{}', acceso = '{}' WHERE id = {}".format(u.nombre, u.apellido, u.correo, u.telefono, u.clave, u.acceso, u.id)
        con.ejecuta_query(sql)
        con.commit()
        input("\n\n Datos modificados Satisfactoriamente")
        con.desconectar()
    except Exception as e:
        print(e)

def eliminarUsuario(id):
    try:
        con = Conexion(host, user, password, db)
        sql = f"DELETE FROM USUARIO WHERE id = {id}"
        con.ejecuta_query(sql)
        con.commit()
        input("\n\n Datos eliminados Satisfactoriamente")
        con.desconectar()
    except Exception as e:
        print(e)

def verificarUsuario(id):
    try:
        con = Conexion(host, user, password, db)
        sql = f"SELECT COUNT(*) FROM USUARIO WHERE id = {id}"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchone()
        con.desconectar()
        if datos[0] > 0:
            return True
        else:
            return False
    except Exception as e:
        con.rollback()        
        print(e)