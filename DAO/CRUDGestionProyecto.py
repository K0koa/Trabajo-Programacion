from DAO.Conexion import Conexion

host = 'localhost'
user = 'ecosolutions'
password = '3k0Z0iuTloNz'
db = 'ecotech solutions'

def registrarProyecto(p):
    try:
        con = Conexion(host, user, password, db)
        sql = f"INSERT INTO PROYECTO SET id = {p.id}, nombre  = '{p.nombre}', descripcion  = '{p.descripcion}', FechaInicio = '{p.fechaInicio}'"
        con.ejecuta_query(sql)
        con.commit()
        input("\n\n Datos ingresados Satisfactoriamente")
        con.desconectar()
    except Exception as e:
        print(e)

def mostrarProyecto(): 
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT * FROM PROYECTO"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as e:
        print(e)

def buscarProyecto(id):
    try:
        con = Conexion(host, user, password, db)
        sql = f"SELECT * FROM PROYECTO WHERE id = {id}"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchone()
        con.desconectar()
        return datos
    except Exception as e:
        print(e)

def cosultaparcialProyecto(cant):
    try:
        con = Conexion(host, user, password, db)
        sql = f"SELECT * FROM PROYECTO"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchmany(size = cant)
        con.desconectar()
        return datos
    except Exception as e:
        con.rollback()
        print(e)

def modificarProyecto(p):
    try:
        con = Conexion(host, user,password,db)
        sql = f"UPDATE PROYECTO SET nombre = '{p.nombre}', descripcion  = '{p.descripcion}', FechaInicio  = '{p.fechaInicio}' WHERE id = {p.id}" 
        con.ejecuta_query(sql)
        con.commit()
        input("\n\n Datos modificados correctamente")
        con.desconectar()
    except Exception as e:
        print(e)

def eliminarProyecto(id):
    try:
        con = Conexion(host, user, password, db)
        sql = f"DELETE FROM PROYECTO WHERE id = {id}"
        con.ejecuta_query(sql)
        con.commit()
        input("\n\n Datos eliminados Satisfactoriamente")
        con.desconectar()
    except Exception as e:
        print(e)