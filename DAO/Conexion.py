import pymysql

class Conexion:
<<<<<<< HEAD
    def __init__(self, host = 'localhost', user = 'ecosolutions', password = '3k0Z0iuTloNz', db = 'ecotech'):
        self.db = pymysql.connect(
            host = host,
            user = user,
            password = password,
            db = db,
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.Cursor
        )
            
        self.cursor = self.db.cursor()
=======
    def __init__(self, host = 'localhost', user = 'ecosolutions', password = '3k0Z0iuTloNz', db = 'ecotech solutions'):
        self.db = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
            charset= 'utf8mb4',
            cursorclass=pymysql.cursors.Cursos
        )
            
        self.cursor=self.db.cursor()
>>>>>>> 30b4954ae90717eee331200485bf8ffe4f88aa6b
    
    def ejecuta_query(self, sql, params = None):
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        return self.cursor
    
    def desconectar(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.db:
                self.db.close()
        except Exception:
            pass
    
    def commit(self):
        self.db.commit()
    
    def rollback(self):
<<<<<<< HEAD
        try:
            self.db.rollback()
        except Exception:
            pass
    
    def obtenerUsuario(self, username):
        try:
            sql = f"SELECT * FROM usuarios WHERE username = {username}"
=======
        self.db.rollback()
    
    def obtenerUsuario(self, username):
        try:
            sql = f"SELECT FROM usuarios WHERE username = {username}"
>>>>>>> 30b4954ae90717eee331200485bf8ffe4f88aa6b
            cursor = self.ejecuta_query(sql)
            datos = cursor.fetchall()
            return datos
        except Exception as e:
            print(e)

    def agregaUsuario(self, username, password_hash, nombre, apellidos, email, tipo_usuario):
        try:
            sql = f"INSERT INTO usuarios (username, password_hash, nombre, apellidos, email, tipo_usuario)" \
<<<<<<< HEAD
            f"VALUES ('{username}', '{password_hash}', '{nombre}', '{apellidos}', '{email}', '{tipo_usuario}')"
=======
            "VALUES ('{username}', '{password_hash}', '{nombre}', '{apellidos}', '{email}', '{tipo_usuario}')"
>>>>>>> 30b4954ae90717eee331200485bf8ffe4f88aa6b
            self.ejecuta_query(sql)
            self.commit()
            return True
        except Exception as e:
            self.rollback()
            error_msg = str(e).lower()
            if "duplicate entry" in error_msg:
                self.error = "Duplicado"
            else:
                self.error = str(e)
            return False