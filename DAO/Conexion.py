import pymysql

class Conexion:
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
    
    def ejecuta_query(self,sql):
        self.cursor.execute(sql)
        return self.cursor
    
    def desconectar(self):
        self.db.close()
    
    def commit(self):
        self.db.commit()
    
    def rollback(self):
        self.db.rollback()
    
    def obtenerUsuario(self, username):
        try:
            sql = f"SELECT FROM usuarios WHERE username = {username}"
            cursor = self.ejecuta_query(sql)
            datos = cursor.fetchall()
            return datos
        except Exception as e:
            print(e)

    def agregaUsuario(self, username, password_hash, nombre, apellidos, email, tipo_usuario):
        try:
            sql = f"INSERT INTO usuarios (username, password_hash, nombre, apellidos, email, tipo_usuario)" \
            "VALUES ('{username}', '{password_hash}', '{nombre}', '{apellidos}', '{email}', '{tipo_usuario}')"
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