from core.database import DataBase
from modules.categoria.schemas import CategoriaCreate, Categoria
from . import queries

class CategoriaRepository:
    def get_all(self):
        db = DataBase()
        rows = db.execute(queries.QUERY_CATEGORIAS)
        results = []
        if not rows:
            return results
        for row in rows:
            results.append(Categoria(id=row[0], nome=row[1], ativo=row[2]))
        return results

    def save(self, categoria: CategoriaCreate):
        db = DataBase()
        result = db.commit(queries.QUERY_CREATE_CATEGORIA, (categoria.nome,))
        return Categoria(id=result[0], nome=categoria.nome, ativo=True)

    def get_id(self, id: int):
        db = DataBase()
        rows = db.execute(queries.QUERY_CATEGORIA_ID, (id,))
        if not rows:
            return None
        row = rows[0]
        return Categoria(id=row[0], nome=row[1], ativo=row[2])

    def put(self, id: int, novo_nome: str):
        db = DataBase()
        categoria = db.commit(queries.QUERY_PUT_CATEGORIA, (novo_nome, id))
        if categoria:
            return Categoria(id=categoria[0], nome=categoria[1], ativo=True)
        return None

    def delete(self, id: int):
        db = DataBase()
        categoria = db.commit(queries.QUERY_DELETE_CATEGORIA, (id,))
        if categoria:
            return Categoria(id=categoria[0], nome=categoria[1], ativo=False)
        return None
