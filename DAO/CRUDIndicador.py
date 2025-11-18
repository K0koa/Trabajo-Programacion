from DAO.Conexion import Conexion
from decimal import Decimal

host = 'localhost'
user = 'ecosolutions'
password = '3k0Z0iuTloNz'
db = 'ecotech'


def agregar(indicador):
    try:
        con = Conexion(host, user, password, db)
        sql = ("INSERT INTO indicador "
                "(tipo_indicador, fecha_valor, valor, fecha_consulta, usuario_id, fuente) "
                "VALUES (%s, %s, %s, %s, %s, %s)")

        def get(x, name, default=None):
            try:
                return getattr(x, name)
            except Exception:
                try:
                    return x.get(name, default)
                except Exception:
                    return default
                
        # Soportar objetos con atributos o dicts
        tipo = get(indicador, 'tipo_indicador') or get(indicador, 'tipo') or ''
        fecha_valor = get(indicador, 'fecha_valor') or get(indicador, 'Fecha') or None
        valor = get(indicador, 'valor') or get(indicador, 'Valor') or 0
        fecha_consulta = get(indicador, 'fecha_consulta') or get(indicador, 'fechaConsulta') or None
        usuario_id = get(indicador, 'usuario_id') or get(indicador, 'id_usuario') or None
        fuente = get(indicador, 'fuente') or None

        if not isinstance(valor, Decimal):
            try:
                valor = Decimal(str(valor))
            except Exception:
                valor = Decimal('0')

        params = (tipo, fecha_valor, valor, fecha_consulta, usuario_id, fuente)
        con.ejecuta_query(sql, params)
        con.commit()
        con.desconectar()
        print(f"Indicador '{tipo}' para {fecha_valor} agregado correctamente.")
    except Exception as ex:
        try:
            con.rollback()
        except Exception:
            pass
        print(f"Error al agregar indicador: {ex}")

def obtenerTodos():
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT * FROM indicador"
        con.ejecuta_query(sql)
        datos = con.cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as ex:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error obtener todos indicadores", ex)
        return []

def obtenerPorFecha(fecha, tipo_indicador):
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT * FROM indicador WHERE fecha_valor = %s AND tipo_indicador = %s"
        con.ejecuta_query(sql, (fecha, tipo_indicador))
        datos = con.cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as ex:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error obtener todos indicadores", ex)
        return []

def obtenerPorId(idU):
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT * FROM indicador WHERE usuario_id = %s"
        con.ejecuta_query(sql, (idU,))
        datos = con.cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as ex:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error obtener todos indicadores", ex)
        return []

def eliminar(id):
    try:
        con = Conexion(host, user, password, db)
        sql = "DELETE FROM indicador WHERE id = %s"
        con.ejecuta_query(sql, (id,))
        con.commit()
        con.desconectar()
    except Exception as ex:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error eliminar indicador", ex)

def editar(indicador):
    try:
        con = Conexion(host, user, password, db)
        sql = "UPDATE indicador (tipo_indicador, nombre_indicador, fecha_valor, valor, fecha_consulta, usuario_id, fuente) " \
        "VALUES (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"

        def get(x, name, default=None):
            try:
                return getattr(x, name)
            except Exception:
                try:
                    return x.get(name, default)
                except Exception:
                    return default
        
        # Soportar objetos con atributos o dicts
        id_indicador = get(indicador, 'id_indicador') or get(indicador, 'id')
        tipo = get(indicador, 'tipo_indicador') or get(indicador, 'tipo') or ''
        nombre = get(indicador, 'nombre_indicador') or get(indicador, 'nombre') or tipo
        fecha_valor = get(indicador, 'fecha_valor') or get(indicador, 'Fecha') or None
        valor = get(indicador, 'valor') or get(indicador, 'Valor') or 0
        fecha_consulta = get(indicador, 'fecha_consulta') or get(indicador, 'fechaConsulta') or None
        usuario_id = get(indicador, 'usuario_id') or get(indicador, 'id_usuario') or None
        fuente = get(indicador, 'fuente') or None

        if not isinstance(valor, Decimal):
            try:
                valor = Decimal(str(valor))
            except Exception:
                valor = Decimal('0')

        params = (tipo, nombre, fecha_valor, valor, fecha_consulta, usuario_id, fuente, id_indicador)
        con.ejecuta_query(sql, params)
        con.commit()
        con.desconectar()
        print(f"Indicador '{tipo}' para {fecha_valor} editado correctamente.")
    except Exception as ex:
        try:
            con.rollback()
        except Exception:
            pass
        print("Error editar indicador", ex)