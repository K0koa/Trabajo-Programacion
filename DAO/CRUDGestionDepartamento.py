from DAO.Conexion import Conexion

host = 'localhost'
user = 'ecosolutions'
password = '3k0Z0iuTloNz'
db = 'ecotech'

def agregar(d):
    try:
        con = Conexion(host, user, password, db)
        sql = ("INSERT INTO departamento (nombre, gerente_empleado_id, descripcion) "
               "VALUES (%s, %s, %s)")
        params = (d.nombre, d.gerente_empleado_id, d.descripcion)
        con.ejecuta_query(sql, params)
        con.commit()
        print("\nDatos ingresados Satisfactoriamente")
        con.desconectar()
    except Exception as e:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error registrar departamento: ", e)

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
        sql = f"SELECT * FROM departamento WHERE USER_ID = %s"
        cursor = con.ejecuta_query(sql, (id,))
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
        sql = "UPDATE departamento SET nombre = %s, gerente_empleado_id = %s, descripcion = %s WHERE USER_ID = %s"
        params = (d[1], d[2], d[3], d[0])
        con.ejecuta_query(sql, params)
        con.commit()
        print("\nDatos modificados Satisfactoriamente")
        con.desconectar()
    except Exception as e:
        print(e)

def eliminar(id):
    try:
        con = Conexion(host, user, password, db)
        sql = f"DELETE FROM departamento WHERE USER_ID = %s"
        con.ejecuta_query(sql, (id,))
        con.commit()
        print("\nDatos elimados Satisfactoriamente")
        con.desconectar()
    except Exception as e:
        print(e)

def verificarDepartamento(id):
    try:
        con = Conexion(host, user, password, db)
        sql = f"SELECT COUNT(*) FROM departamento WHERE USER_ID = %s"
        cursor = con.ejecuta_query(sql, (id,))
        datos = cursor.fetchone()
        con.desconectar()
        if datos[0] > 0:
            return True
        else:
            return False
    except Exception as e:
        con.rollback()
        print(e)

def verificarGerente(id):
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT COUNT(*) FROM empleado WHERE USER_ID = %s"
        cursor = con.ejecuta_query(sql, (id,))
        datos = cursor.fetchone()
        con.desconectar()
        if datos[0] > 0:
            return True
        else:
            return False
    except Exception as e:
        con.rollback()
        print(e)