from core.db import DataBase
from modules.categoria.schemas import CategoriaCreate


class CategoriaRepository:
    QUERY_CATEGORIAS = "SELECT nome FROM categoria"
    QUERY_CATEGORIA_ID = "SELECT name FROM categoria where id = (%s)"
    QUERY_CREATE_CATEGORIA = 'INSERT INTO categoria (nome) VALUES (%s) RETURNING id;'
    QUERY_PUT_CATEGORIA = "UPDATE categorias SET name = (%s) WHERE categorias.id = (%s)"
    QUERY_DELETE_CATEGORIA = "UPDATE categorias SET ativo = FALSE WHERE categorias.id = (%s)"
    def get_all(self):
        db = DataBase()
        categorias = db.execute(self.QUERY_CATEGORIAS)
        results = []
        for categoria in categorias:
            results.append({"id": categoria[0], "nome": categoria[1], "ativo": categoria[2]})
        return results

    def save(self, categoria: CategoriaCreate):
        db = DataBase()
        query = self.QUERY_CREATE_CATEGORIA % f"'{categoria[0]}, {categoria[1]}, {categoria[2]}'"
        result = db.execute(query)
        return {"id": result[0], "nome": categoria[1], "ativo": categoria[2]}

    def get_id(self, id: int):
        db = DataBase()
        query = self.QUERY_CATEGORIA_ID % id
        categoria = db.execute(query, many=False)
        if categoria:
            return {"id": categoria[0], "nome": categoria[1], "ativo": categoria[2]}
        return {}

    def put(self, id: int, novo_nome: str):
        db = DataBase()
        query = self.QUERY_PUT_CATEGORIA % f"{novo_nome}, {id}"
        categoria = db.execute(query, many=False)
        if categoria:
            return f"Nome: {categoria[1]}"
        return False

    def delete(self, id: int):
        db = DataBase()
        query = self.QUERY_DELETE_CATEGORIA % f"{id}"
        categoria = db.execute(query, many=False)
        if categoria:
            return True
        return False
