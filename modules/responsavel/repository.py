from core.database import DataBase
from modules.responsavel.schemas import ResponsavelCreate, Responsavel
from . import queries

class ResponsavelRepository:
    def get_all(self):
        db = DataBase()
        rows = db.execute(queries.QUERY_RESPONSAVEIS)
        results = []
        for row in rows:
            results.append(Responsavel(id=row[0], nome=row[1], cargo=row[2], ativo=row[3]))
        return results

    def get_id(self, id: int):
        db = DataBase()
        rows = db.execute(queries.QUERY_RESPONSAVEL_BY_ID, (id,))
        if not rows:
            return None
        row = rows[0]
        return Responsavel(id=row[0], nome=row[1], cargo=row[2], ativo=row[3])

    def save(self, responsavel: ResponsavelCreate):
        db = DataBase()
        resp = db.commit(queries.QUERY_CREATE_RESPONSAVEL, (responsavel.nome, responsavel.cargo))
        if resp:
            return Responsavel(id=resp[0], nome=resp[1], cargo=resp[2], ativo=resp[3])
        return None

    def put(self, id: int, novo_nome: str, novo_cargo: str):
        db = DataBase()
        resp = db.commit(queries.QUERY_PUT_RESPONSAVEL, (novo_nome, novo_cargo, id))
        if resp:
            return Responsavel(id=resp[0], nome=resp[1], cargo=resp[2], ativo=resp[3])
        return None

    def delete(self, id: int):
        db = DataBase()
        resp = db.commit(queries.QUERY_DELETE_RESPONSAVEL, (id,))
        if resp:
            return Responsavel(id=resp[0], nome=resp[1], cargo=resp[2], ativo=resp[3])
        return None
