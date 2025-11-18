from DAO.Conexion import Conexion

host = 'localhost'
user = 'ecosolutions'
password = '3k0Z0iuTloNz'
db = 'ecotech'

def verificarTipo(username):
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT * FROM usuarios WHERE username = %s"
        cursor = con.ejecuta_query(sql, (username,))
        datos = cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as e:
        con.rollback()
        print(e)

def obtenerID(username):
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT * FROM usuarios WHERE username = %s"
        cursor = con.ejecuta_query(sql, (username,))
        datos = cursor.fetchall()
        con.desconectar()
        return datos[0][0]
    except Exception as e:
        con.rollback()
        print(e)