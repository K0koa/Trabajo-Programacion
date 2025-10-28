from DAO.Conexion import Conexion

host = 'localhost'
user = 'ecosolutions'
password = '3k0Z0iuTloNz'
db = 'ecotech solutions'

def registrarEmpleado(e):
    try:
        con = Conexion(host, user, password,db)
        sql = f"INSERT INTO empleado SET id = {e.id}, nombre = '{e.nombre}', apellido = '{e.apellido}', correo = '{e.correo}', telefono = '{e.telefono}', FechaContrato = '{e.FechaContrato}', salario = {e.salario}"
        con.ejecuta_query(sql)
        con.commit()
        input("\n\n Datos ingresados Satisfactoriamente")
        con.desconectar()
    except Exception as e:
        print(e)

def mostrarEmpleado():
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT * FROM empleado"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as e:
        con.rollback()
        print(e)

def buscarEmpleado(id):
    try:
        con = Conexion(host, user, password, db)
        sql = f"SELECT * FROM empleado WHERE id = {id}"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchone()
        con.desconectar()
        return datos
    except Exception as e:
        con.rollback()
        print(e)
        
def cosultaparcialEmpleado(cant):
    try:
        con = Conexion(host, user, password, db)
        sql = f"SELECT * FROM empleado"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchmany(size = cant)
        con.desconectar()
        return datos
    except Exception as e:
        con.rollback()
        print(e)


def modificarEmpleado(e):
    try:
        con = Conexion(host, user,password,db)
        sql = f"UPDATE empleado SET nombre = '{e.nombre}', apellido = '{e.apellido}', correo = '{e.correo}', telefono = '{e.telefono}', FechaContrato = '{e.FechaContrato}', salario = {e.salario} WHERE id = {e.id}"
        con.ejecuta_query(sql)
        con.commit()
        input("\n\n Datos modificados correctamente")
        con.desconectar()
    except Exception as e:
        print(e)

def eliminarEmpleado(id):
    try:
        con = Conexion(host, user, password, db)
        sql = "DELETE FROM empleado WHERE id={}".format(id)
        con.ejecuta_query(sql)
        con.commit()
        input("\n\n empleado Eliminado Satisfactoriamente ")
        con.desconectar()
    except Exception as e:
        print(e)

def verificarEmpleado(id):
    try:
        con = Conexion(host, user, password, db)
        sql = f"SELECT COUNT(*) FROM empleado WHERE id = {id}"
        cursor = con.ejecuta_query(sql)
        resultado = cursor.fetchone()
        con.desconectar()
        return resultado[0] > 0
    except Exception as e:
        con.rollback()
        print(e)