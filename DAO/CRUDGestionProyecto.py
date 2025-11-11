from DAO.Conexion import Conexion

host = 'localhost'
user = 'ecosolutions'
password = '3k0Z0iuTloNz'
db = 'ecotech'

def registrar(p):
    try:
        con = Conexion(host, user, password, db)
        sql = "INSERT INTO proyecto (nombre, descripcion, fecha_inicio) VALUES (%s, %s, %s)"
        params = (p.nombre, p.descripcion, p.fechaInicio)
        con.ejecuta_query(sql, params)
        con.commit()
        input("\n\n Datos ingresados Satisfactoriamente")
        con.desconectar()
    except Exception as e:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error registrar proyecto: ", e)

def mostrarTodo(): 
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT * FROM proyecto"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as e:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error mostrar proyecto: ", e)

def buscar(id):
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT * FROM proyecto WHERE USER_ID = %s"
        cursor = con.ejecuta_query(sql, (id,))
        datos = cursor.fetchone()
        con.desconectar()
        return datos
    except Exception as e:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error buscar proyecto: ", e)

def cosultaParcial(cant):
    try:
        con = Conexion(host, user, password, db)
        sql = f"SELECT * FROM proyecto"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchmany(size = cant)
        con.desconectar()
        return datos
    except Exception as e:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error buscar proyecto: ", e)

def editar(p):
    try:
        con = Conexion(host, user,password,db)
        sql = "UPDATE proyecto SET nombre = %s, descripcion = %s, fecha_inicio = %s WHERE USER_ID = %s"
        params = (p[1], p[2], p[3], p[0])
        con.ejecuta_query(sql, params)
        con.commit()
        print("\n=Datos modificados correctamente")
        con.desconectar()
    except Exception as e:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error modificar proyecto: ", e)

def eliminar(id):
    try:
        con = Conexion(host, user, password, db)
        sql = "DELETE FROM proyecto WHERE USER_ID = %s"
        con.ejecuta_query(sql, (id,))
        con.commit()
        print("\nDatos eliminados Satisfactoriamente")
        con.desconectar()
    except Exception as e:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error eliminar proyecto: ", e)

def buscarEspecifico(id):
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT * FROM proyecto WHERE USER_ID = %s"
        cursor = con.ejecuta_query(sql, (id,))
        datos = cursor.fetchone()
        con.desconectar()
        return datos
    except Exception as e:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error buscar proyecto: ", e)

def verificar(id):
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT COUNT(*) FROM proyecto WHERE USER_ID = %s"
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
        print("Error verificar proyecto: ", e)