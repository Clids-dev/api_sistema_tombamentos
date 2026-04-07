class UsuarioRepository:
    def __init__(self, db):
        self.db = db

    def buscar_por_username(self, username):
        cursor = self.db.conn.cursor()
    
        try:
            cursor.execute(
                "SELECT id, username, senha, tipo, ativo FROM usuarios WHERE username = %s",
                (username,)
            )
            return cursor.fetchone()
        
        except Exception as e:
            print("ERRO NO BANCO:", e)
            self.db.conn.rollback()
            return None