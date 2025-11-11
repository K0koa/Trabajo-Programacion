from DAO.Conexion import Conexion

host = 'localhost'
user = 'ecosolutions'
password = '3k0Z0iuTloNz'
db = 'ecotech'

def agregar(r):
    try:
        con = Conexion(host, user, password, db)
        sql = ("INSERT INTO tiempo (empleado_id, proyecto_id, fecha, horas, descripcion) "
               "VALUES (%s, %s, %s, %s, %s)")
        params = (r.empleado_id, r.proyecto_id, r.fecha, r.horas, r.descripcion)
        con.ejecuta_query(sql, params)
        con.commit()
        input("\n\n Datos ingresados Satisfactoriamente")
        con.desconectar()
    except Exception as ex:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error agregar registro tiempo", ex)
    
def mostrarTodo():
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT * FROM tiempo"
        con.ejecuta_query(sql)
        datos = con.cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as ex:
        try:
            con.rollback()
        except Exception as e:
            pass
        print("Error mostrar todos tiempo", ex)
        return []
    
def consultaPorEmpleado(empleado_id):
    try:
        con = Conexion(host, user, password, db)
        sql = f"SELECT * FROM tiempo WHERE empleado_id = {empleado_id}"
        con.ejecuta_query(sql)
        datos = con.cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as ex:
        try:
            con.rollback()
        except Exception as e:
            pass
        print("Error consulta por empleado", ex)
        return []