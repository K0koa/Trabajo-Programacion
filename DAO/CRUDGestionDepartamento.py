from DAO.Conexion import Conexion

host = 'localhost'
user = 'ecosolutions'
password = '3k0Z0iuTloNz'
db = 'ecotech'

def agregar(d):
    try:
        con = Conexion(host, user, password, db)
        sql = f"INSERT INTO departamento SET id = {d.id}, nombre = '{d.nombre}', gerente = '{d.gerente}'"
        con.ejecuta_query(sql)
        con.commit()
        input("\n\n Datos ingresados Satisfactoriamente")
        con.desconectar()
    except Exception as e:
        print(e)

def mostrarTodo(): 
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT * FROM departamento"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as e:
        con.rollback()
        print(e)

def buscarDepartamento(id):
    try:
        con = Conexion(host, user, password, db)
        sql = f"SELECT * FROM departamento WHERE id = {id}"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchone()
        con.desconectar()
        return datos
    except Exception as e:
        con.rollback()
        print(e)
    
def cosultaparcialDepartamento(cant):
    try:
        con = Conexion(host, user, password, db)
        sql = f"SELECT * FROM departamento"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchmany(size = cant)
        con.desconectar()
        return datos
    except Exception as e:
        con.rollback()
        print(e)

def editar(d):
    try:
        con = Conexion(host, user, password, db)
        sql = f"UPDATE departamento SET nombre = '{d.nombre}', gerente = '{d.gerente}' WHERE id = {d.id}"
        con.ejecuta_query(sql)
        con.commit()
        input("\n\n Datos modificados Satisfactoriamente")
        con.desconectar()
    except Exception as e:
        print(e)

def eliminar(id):
    try:
        con = Conexion(host, user, password, db)
        sql = f"DELETE FROM departamento WHERE id = {id}"
        con.ejecuta_query(sql)
        con.commit()
        input("\n\n Datos elimados Satisfactoriamente")
        con.desconectar()
    except Exception as e:
        print(e)

def verificarDepartamento(id):
    try:
        con = Conexion(host, user, password, db)
        sql = f"SELECT COUNT(*) FROM departamento WHERE id = {id}"
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