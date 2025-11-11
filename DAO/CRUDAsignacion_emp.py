from DAO.Conexion import Conexion

host = 'localhost'
user = 'ecosolutions'
password = '3k0Z0iuTloNz'
db = 'ecotech'

def asignar(empleado_id, proyecto_id, rol=None):
    try:
        con = Conexion(host, user, password, db)
        sql = "INSERT INTO asignacion_emp (empleado_id, proyecto_id, rol) VALUES (%s, %s, %s)"
        params = (empleado_id, proyecto_id, rol)
        con.ejecuta_query(sql, params)
        con.commit()
        print("\nDatos ingresados Satisfactoriamente")
        con.desconectar()
    except Exception as ex:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error asignacion", ex)

def desasignar(asignacion_id):
    try:
        con = Conexion(host, user, password, db)
        sql = f"DELETE FROM asignacion_emp WHERE user_id = %s"
        con.ejecuta_query(sql, (asignacion_id,))
        con.commit()
        print("\nDatos eliminados Satisfactoriamente")
        con.desconectar()
    except Exception as e:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error desasignacion", e)

def obtenerPorEmpleado(empleado_id):
    try:
        con = Conexion(host,user,password,db)
        sql = "SELECT * FROM asignacion_emp WHERE empleado_id = %s"
        cursor = con.ejecuta_query(sql, (empleado_id,))
        datos = cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as ex:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error obtenerPorEmpleado:", ex)
        return []
    
def verificar(id):
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT COUNT(*) FROM asignacion_emp WHERE USER_ID = %s"
        cursor = con.ejecuta_query(sql, (id,))
        datos = cursor.fetchone()
        con.desconectar()
        if datos[0] > 0:
            return True
        else:
            return False
    except Exception as e:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error verificar asignacion: ", e)