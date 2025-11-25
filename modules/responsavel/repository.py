from core.db import DataBase
from modules.responsavel.schemas import ResponsavelCreate


class ResponsavelRepository:
    QUERY_RESPONSAVEIS = "SELECT nome FROM responsaveis"
    QUERY_RESPONSAVEL_BY_ID = "SELECT nome FROM responsaveis WHERE responsaveis.id = (%s)"
    QUERY_CREATE_RESPONSAVEL = "INSERT INTO responsaveis VALUES (%s) RETURNING id"
    QUERY_PUT_RESPONSAVEL = "UPDATE responsaveis SET nome = (%s) WHERE responsaveis.id = (%s)"
    QUERY_DELETE_RESPONSAVEL = "UPDATE responsaveis SET ativo = FALSE WHERE  responsaveis.id = (%s)"

    def get_all(self):
        db = DataBase()
        responsaveis = db.execute(self.QUERY_RESPONSAVEIS)
        results = []
        for responsavel in responsaveis:
            results.append({"nome": responsavel[1], "Cargo": responsavel[2], "Ativo": responsavel[3]})
        return results

    def get_id(self, id: int):
        db = DataBase()
        query = self.QUERY_RESPONSAVEIS % id
        responsavel = db.execute(query)
        if responsavel:
            return {"nome": responsavel[1], "Cargo": responsavel[2], "Ativo": responsavel[3]}
        return False

    def save(self, responsavel: ResponsavelCreate):
        db = DataBase()
        query = self.QUERY_CREATE_RESPONSAVEL % f"{responsavel.nome}, {responsavel.cargo}"
        responsavel = db.commit(query)
        if responsavel:
            return {"nome": responsavel[1], "Cargo": responsavel[2], "Ativo": responsavel[3]}
        return False

    def put(self, id: int, novo_nome):
        db = DataBase()
        query = self.QUERY_PUT_RESPONSAVEL % f"{novo_nome}, {id}"
        responsavel = db.execute(query, many=False)
        if responsavel:
            return {"nome": responsavel[1], "Cargo": responsavel[2], "Ativo": responsavel[3]}
        return False

    def delete(self, id: int):
        db = DataBase()
        query = self.QUERY_DELETE_RESPONSAVEL % id
        responsavel = db.execute(query, many=False)
        if responsavel:
            return {"nome": responsavel[1], "Cargo": responsavel[2], "Ativo": responsavel[3]}
        return False
