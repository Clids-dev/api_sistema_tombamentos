from core.db import DataBase
from modules.bem.schemas import BemCreate, Bem


class BemRepository(DataBase):
    QUERY_BENS = "SELECT id, nome, codigo_tombamento, valor, status, ativo FROM bens"
    QUERY_BEM_ID = "SELECT id, nome, codigo_tombamento, valor, status, ativo FROM bens WHERE id = %s"
    QUERY_CREATE_BEM = ('INSERT INTO bens (nome, codigo_tombamento, valor, status) '
                        'VALUES (%s, %s, %s, %s) RETURNING id;')
    QUERY_PUT_BEM = """UPDATE bens SET nome = %s, status = %s WHERE id = %s RETURNING id, nome, codigo_tombamento, valor, status, ativo;"""
    QUERY_DELETE_BEM = "UPDATE bens SET ativo = FALSE WHERE id = %s RETURNING id;"

    def get_all(self):
        db = DataBase()
        bens = db.execute(BemRepository.QUERY_BENS)
        results = []
        for bem in bens:
            results.append(Bem(
                id=bem[0],
                nome=bem[1],
                codigo_tombamento=bem[2],
                valor=bem[3],
                status=bem[4],
                ativo=bem[5]
            ))
        return results


    def save(self, bem : BemCreate):
        db = DataBase()
        query = self.QUERY_CREATE_BEM
        db.commit(query, (bem.nome, bem.codigo_tombamento, bem.valor, bem.status,))
        return bem

    def get_id(self, id: int):
        db = DataBase()
        query = self.QUERY_BEM_ID % id
        bem = db.execute(query)
        if bem:
            return Bem(
                id=bem[0][0],
                nome=bem[0][1],
                codigo_tombamento=bem[0][2],
                valor=bem[0][3],
                status=bem[0][4],
                ativo=bem[0][5]
            )
        return None

    def put(self, id: int, novo_nome: str, novo_status: str):
        db = DataBase()
        query = self.QUERY_PUT_BEM
        bem = db.commit(query, (novo_nome, novo_status, id,))
        if bem:
            return Bem(
                id=bem[0],
                nome=bem[1],
                codigo_tombamento=bem[2],
                valor=bem[3],
                status=bem[4],
                ativo=bem[5]
            )
        return None

    def delete(self, id: int):
        db = DataBase()
        query = self.QUERY_DELETE_BEM % id
        result = self.get_id(id)
        bem = db.commit(query)
        if bem:
            return Bem(
                id=result.id,
                nome=result.nome,
                codigo_tombamento=result.codigo_tombamento,
                valor=result.valor,
                status=result.status,
                ativo=False
            )
        return None