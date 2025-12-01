from core.db import DataBase
from modules.setor.schemas import SetorCreate, Setor


class SetorRepository:
    QUERY_SETORES = "SELECT id, nome, responsavel, ativo FROM setores"
    QUERY_SETOR_BY_ID = "SELECT nome FROM setores WHERE setores.id = (%s)"
    QUERY_CREATE_SETOR = "INSERT INTO setores VALUES (%s) RETURNING id"
    QUERY_PUT_SETOR = "UPDATE setores SET nome = (%s) WHERE setores.id = (%s)"
    QUERY_DELETE_SETOR = "UPDATE setores SET ativo = FALSE WHERE setores.id = (%s)"

    def get_all(self):
        db = DataBase()
        setores = db.execute(self.QUERY_SETORES)
        results = []
        for setor in setores:
           results.append(Setor(id=setor[0], nome=setor[1], responsavel=setor[2], ativo=setor[3]))
        return results

    def get_id(self, id: int):
        db = DataBase()
        query = self.QUERY_SETOR_BY_ID % id
        setor = db.execute(query, many=False)
        if setor:
            return {"id": setor[0], "nome": setor[1], "responsavel": setor[2], "ativo": setor[3]}
        return {}

    def save(self, setor: SetorCreate):
        db = DataBase()
        query = self.QUERY_CREATE_SETOR % f"{setor.nome}, {setor.responsavel}"
        setor = db.commit(query)
        return {"id": setor[0], "nome": setor[1], "responsavel": setor[2], "ativo": setor[3]}

    def put(self, id: int, novo_nome: str):
        db = DataBase()
        query = self.QUERY_PUT_SETOR % f"{novo_nome}, {id}"
        setor = db.execute(query)
        if setor:
            return {"id": setor[0], "nome": setor[1], "responsavel": setor[2], "ativo": setor[3]}
        return {}

    def delete(self, id: int):
        db = DataBase()
        query = self.QUERY_DELETE_SETOR % id
        setor = db.execute(query)
        if setor:
            return {"id": setor[0], "nome": setor[1], "responsavel": setor[2], "ativo": setor[3]}
        return {}