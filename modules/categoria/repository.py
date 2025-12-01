from core.db import DataBase
from modules.categoria.schemas import CategoriaCreate, Categoria


class CategoriaRepository:
    QUERY_CATEGORIAS = """SELECT id, nome, ativo FROM categorias WHERE ativo = TRUE"""
    QUERY_CATEGORIA_ID = """SELECT id, nome, ativo FROM categorias where id = %s AND ativo = TRUE"""
    QUERY_CREATE_CATEGORIA = """INSERT INTO categorias (nome) VALUES (%s) RETURNING id"""
    QUERY_PUT_CATEGORIA = "UPDATE categorias SET nome = (%s) WHERE categorias.id = (%s) RETURNING id, nome, ativo"
    QUERY_DELETE_CATEGORIA = """UPDATE categorias SET ativo = FALSE WHERE categorias.id = (%s) RETURNING id, nome, ativo"""

    def get_all(self):
        db = DataBase()
        rows = db.execute(self.QUERY_CATEGORIAS)
        results = []
        if not rows:
            return results
        for row in rows:
            (results.append(Categoria(id=row[0], nome=row[1], ativo=row[2])))
        return results

    def save(self, categoria: CategoriaCreate):
        db = DataBase()
        query = self.QUERY_CREATE_CATEGORIA
        result = db.commit(query, (categoria.nome,))
        return Categoria(id=result[0], nome=categoria.nome, ativo=True)

    def get_id(self, id: int):
        db = DataBase()
        rows = db.execute(self.QUERY_CATEGORIA_ID % id)
        if not rows:
            return None
        row = rows[0]
        return Categoria(id=row[0], nome=row[1], ativo=row[2])

    def put(self, id: int, novo_nome: str):
        db = DataBase()
        query = self.QUERY_PUT_CATEGORIA
        categoria = db.commit(query, (novo_nome, id))
        if categoria:
            return Categoria(id=categoria[0], nome=categoria[1], ativo=True)
        return None

    def delete(self, id: int):
        db = DataBase()
        query = self.QUERY_DELETE_CATEGORIA % id
        categoria = db.commit(query)
        if categoria:
            return Categoria(id=categoria[0], nome=categoria[1], ativo=False)
        return None
