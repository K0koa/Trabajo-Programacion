from DAO.Conexion import Conexion

host = 'localhost'
user = 'ecosolutions'
password = '3k0Z0iuTloNz'
<<<<<<< HEAD
db = 'ecotech'
=======
db = 'ecotech solutions'
>>>>>>> 30b4954ae90717eee331200485bf8ffe4f88aa6b

def asignar(empleado_id, proyecto_id, rol=None):
    try:
        con = Conexion(host, user, password, db)
        sql = "INSERT INTO asignacion_emp (empleado_id, proyecto_id, rol) VALUES (%s, %s, %s)"
        params = (empleado_id, proyecto_id, rol)
        con.ejecuta_query(sql, params)
        con.commit()
        input("\n\n Datos ingresados Satisfactoriamente")
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
        input("\n\n Datos eliminados Satisfactoriamente")
        con.desconectar()
    except Exception as e:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error desasignacion", e)

def obtenerPorEmpleado(empleado_id):
    try:
        con = Conexion(host, user, password, db)
        sql = f"SELECT * FROM asignacion_emp WHERE empleado_id = %s"
        con.ejecuta_query(sql, (empleado_id,))
        datos = con.cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as ex:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error obtener por empleado", ex)
        return []