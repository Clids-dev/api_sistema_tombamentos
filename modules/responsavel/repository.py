from core.db import DataBase
from modules.responsavel.schemas import ResponsavelCreate, Responsavel


class ResponsavelRepository:
    QUERY_RESPONSAVEIS = "SELECT id, nome, cargo, ativo FROM responsaveis WHERE ativo = TRUE"
    QUERY_RESPONSAVEL_BY_ID = """SELECT id, nome, cargo, ativo FROM responsaveis WHERE id = (%s) AND ativo = TRUE"""
    QUERY_CREATE_RESPONSAVEL = "INSERT INTO responsaveis (nome, cargo) VALUES (%s, %s) RETURNING id, nome, cargo"
    QUERY_PUT_RESPONSAVEL = "UPDATE responsaveis SET nome = (%s), cargo = (%s) WHERE responsaveis.id = (%s) RETURNING id, nome, cargo, ativo"
    QUERY_DELETE_RESPONSAVEL = "UPDATE responsaveis SET ativo = FALSE WHERE  responsaveis.id = (%s) RETURNING id, nome, cargo, ativo"

    def get_all(self):
        db = DataBase()
        rows = db.execute(self.QUERY_RESPONSAVEIS)
        results = []
        for row in rows:
            results.append(Responsavel(id=row[0], nome=row[1], cargo=row[2], ativo=row[3]))
        return results

    def get_id(self, id: int):
        db = DataBase()
        query = self.QUERY_RESPONSAVEL_BY_ID % id
        rows = db.execute(query)
        if not rows:
            return None
        row = rows[0]
        return Responsavel(id=row[0], nome=row[1], cargo=row[2], ativo=row[3])

    def save(self, responsavel: ResponsavelCreate):
        db = DataBase()
        query = self.QUERY_CREATE_RESPONSAVEL
        responsavel = db.commit(query, (responsavel.nome, responsavel.cargo,))
        if responsavel:
            return Responsavel(id=responsavel[0], nome=responsavel[1], cargo=responsavel[2], ativo=True)
        return None

    def put(self, id: int, novo_nome, novo_cargo):
        db = DataBase()
        query = self.QUERY_PUT_RESPONSAVEL
        responsavel = db.commit(query, (novo_nome, novo_cargo, id))
        if responsavel:
            return Responsavel(id=responsavel[0], nome=responsavel[1], cargo=responsavel[2], ativo=True)
        return None

    def delete(self, id: int):
        db = DataBase()
        query = self.QUERY_DELETE_RESPONSAVEL % id
        responsavel = db.commit(query)
        if responsavel:
            return Responsavel(id=responsavel[0], nome=responsavel[1], cargo=responsavel[2], ativo=False)
        return None
