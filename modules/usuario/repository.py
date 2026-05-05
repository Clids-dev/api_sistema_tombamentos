from core.database import DataBase
from . import queries

class UsuarioRepository:
    def buscar_por_username(self, username: str):
        db = DataBase()
        try:
            result = db.execute(queries.QUERY_BUSCAR_POR_USERNAME, (username,), many=False)
            return result
        except Exception as e:
            print(f"ERRO NO BANCO: {e}")
            return None
