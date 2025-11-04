from DAO.Conexion import Conexion

host = 'localhost'
user = 'ecosolutions'
password = '3k0Z0iuTloNz'
db = 'ecotech'

def agregar(e):
    try:
<<<<<<< HEAD
        con = Conexion(host, user, password, db)
        sql = ("INSERT INTO empleado (run, nombre, direccion, telefono, correo, fecha_inicio, salario, departamento_id) " 
                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
        params = (e.run, e.nombre, e.direccion, e.telefono, e.correo, e.fecha_inicio, e.salario, e.departamento_id)
        con.ejecuta_query(sql, params)
=======
        con = Conexion(host, user, password,db)
        sql = f"INSERT INTO empleado SET id = {e.id}, nombre = '{e.nombre}', apellido = '{e.apellido}', correo = '{e.correo}', telefono = '{e.telefono}', FechaContrato = '{e.FechaContrato}', salario = {e.salario}"
        con.ejecuta_query(sql)
>>>>>>> 30b4954ae90717eee331200485bf8ffe4f88aa6b
        con.commit()
        input("\n\n Datos ingresados Satisfactoriamente")
        con.desconectar()
    except Exception as e:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error registrar empleado:", e)

def mostrarTodos():
    try:
<<<<<<< HEAD
        con = Conexion(host,user,password,db)
=======
        con = Conexion(host, user, password, db)
>>>>>>> 30b4954ae90717eee331200485bf8ffe4f88aa6b
        sql = "SELECT * FROM empleado"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as ex:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error mostrartodos:", ex)
        return []

def buscarEmpleado(user_id):
    try:
        con = Conexion(host, user, password, db)
<<<<<<< HEAD
        sql = "SELECT * FROM empleado WHERE USER_ID = %s"
        cursor = con.ejecuta_query(sql, (user_id,))
=======
        sql = f"SELECT * FROM empleado WHERE id = {id}"
        cursor = con.ejecuta_query(sql)
>>>>>>> 30b4954ae90717eee331200485bf8ffe4f88aa6b
        datos = cursor.fetchone()
        con.desconectar()
        return datos
    except Exception as e:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error buscar empleado:", e)
        return None
        
def cosultaParcial(cant):
    try:
        con = Conexion(host, user, password, db)
<<<<<<< HEAD
        sql = "SELECT * FROM empleado"
=======
        sql = f"SELECT * FROM empleado"
>>>>>>> 30b4954ae90717eee331200485bf8ffe4f88aa6b
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchmany(size = cant)
        con.desconectar()
        return datos
    except Exception as e:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error mostrar empleado:", e)


def editar(e):
    try:
        con = Conexion(host, user,password,db)
<<<<<<< HEAD
        sql = "UPDATE empleado SET nombre = %s, direccion = %s, telefono = %s, correo = %s, fecha_inicio = %s, salario = %s, departamento_id = %s WHERE USER_ID = %s"
        params = (e.nombre, e.direccion, e.telefono, e.correo, e.fecha_inicio, e.salario, e.departamento_id, e.user_id)
        con.ejecuta_query(sql, params)
=======
        sql = f"UPDATE empleado SET nombre = '{e.nombre}', apellido = '{e.apellido}', correo = '{e.correo}', telefono = '{e.telefono}', FechaContrato = '{e.FechaContrato}', salario = {e.salario} WHERE id = {e.id}"
        con.ejecuta_query(sql)
>>>>>>> 30b4954ae90717eee331200485bf8ffe4f88aa6b
        con.commit()
        input("\n\n Datos modificados correctamente")
        con.desconectar()
    except Exception as e:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error modificar empleado:", e)

def eliminar(id):
    try:
        con = Conexion(host, user, password, db)
<<<<<<< HEAD
        sql = "DELETE FROM empleado WHERE USER_ID = %s"
        params = (id,)
        con.ejecuta_query(sql, params)
=======
        sql = "DELETE FROM empleado WHERE id={}".format(id)
        con.ejecuta_query(sql)
>>>>>>> 30b4954ae90717eee331200485bf8ffe4f88aa6b
        con.commit()
        input("\n\n empleado Eliminado Satisfactoriamente ")
        con.desconectar()
    except Exception as e:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error eliminar empleado:", e)

def verificar(id):
    try:
        con = Conexion(host, user, password, db)
<<<<<<< HEAD
        sql = "SELECT * FROM empleado WHERE id = %s"
        cursor = con.ejecuta_query(sql, (id,))
        datos = cursor.fetchone()
=======
        sql = f"SELECT COUNT(*) FROM empleado WHERE id = {id}"
        cursor = con.ejecuta_query(sql)
        resultado = cursor.fetchone()
>>>>>>> 30b4954ae90717eee331200485bf8ffe4f88aa6b
        con.desconectar()
        if datos is not None:
            return True
        else:
            return False
    except Exception as e:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error verificar empleado:", e)