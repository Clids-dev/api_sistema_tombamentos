from core.db import DataBase
from modules.bem.schemas import BemCreate

class BemRepository(DataBase):
    QUERY_BENS = "SELECT id, name, codigo_tombamento, valor, status, ativo FROM bem"
    QUERY_BEM_ID = "SELECT id, name, codigo_tombamento, valor, status, ativo FROM bem WHERE id = %s"
    QUERY_CREATE_BEM = ('INSERT INTO bem (nome, codigo_tombamento, valor, status, ativo) '
                        'VALUES (%s, %s, %s, %s, %s) RETURNING id;')

    def get_all(self):
        db = DataBase()
        bens = db.execute(BemRepository.QUERY_BENS)
        results = []
        for bem in bens:
            results.append({"id": bem[0], "nome": bem[1], "codigo_tombamento": bem[2],
                            "valor": bem[3], "status": bem[4], "ativo": bem[5]})
            return results


    def save(self, bem : BemCreate):
        db = DataBase()
        query = self.QUERY_CREATE_BEM % f"'{bem.nome}',{bem.codigo_tombamento},{bem.valor}, '{bem.status}',{bem.ativo}"
        db.commit(query)
        return {"id": bem[0], "nome": bem[1], "codigo_tombamento": bem[2],
                "valor": bem[3], "status": bem[4], "ativo": bem[5]}

    def get_by_id(self, id: id):
        db = DataBase()
        query = self.QUERY_BEM_ID % id
        bem = db.execute(query, many =False)
        if bem:
            return {"id": bem[0], "nome": bem[1], "codigo_tombamento": bem[2],
                    "valor": bem[3], "status": bem[4], "ativo": bem[5]}