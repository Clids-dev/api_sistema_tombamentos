from core.db import DataBase
from modules.bem.schemas import BemCreate, Bem


class BemRepository(DataBase):
    QUERY_BENS = "SELECT id, nome, codigo_tombamento, valor, status, ativo FROM bens"
    QUERY_BEM_ID = "SELECT id, nome, codigo_tombamento, valor, status, ativo FROM bens WHERE id = %s"
    QUERY_CREATE_BEM = ('INSERT INTO bens (nome, codigo_tombamento, valor, status, ativo) '
                        'VALUES (%s, %s, %s, %s, %s) RETURNING id;')
    QUERY_PUT_BEM = "UPDATE bens SET nome = %s, status = %s WHERE bens.id = %s RETURNING id, nome, codigo_tombamento, valor, status, ativo"""
    QUERY_DELETE_BEM = """UPDATE bens SET ativo = FALSE WHERE bens.id = (%s) RETURNING id, nome, codigo_tombamento, valor, status, ativo"""
    QUERY_BEM_CODTOMB = "SELECT id, nome, codigo_tombamento, valor, status, ativo FROM bens WHERE codigo_tombamento = %s"

    def get_all(self):
        db = DataBase()
        rows = db.execute(BemRepository.QUERY_BENS)
        results = []
        if not rows:
            return results

        for row in rows:
            (results.append(Bem(id=row[0], nome=row[1], codigo_tombamento=row[2], valor=row[3], status=row[4], ativo=row[5])))
        return results

    def get_by_id(self, id: id):
        db = DataBase()
        rows = db.execute(self.QUERY_BEM_ID % id)
        if not rows:
            return None
        row = rows[0]
        return Bem(id=row[0], nome=row[1], codigo_tombamento=row[2], valor=row[3], status=row[4], ativo=row[5])

    def save(self, bem : BemCreate):
        db = DataBase()
        query = self.QUERY_CREATE_BEM
        result = db.commit(query, (bem.nome, bem.codigo_tombamento, bem.valor, bem.status, True))
        return Bem(id=result[0], nome=bem.nome, codigo_tombamento=bem.codigo_tombamento, valor=bem.valor, status=bem.status , ativo=True)

    def put(self, id: int, novo_nome: str, novo_status: str):
        db = DataBase()
        query = self.QUERY_PUT_BEM
        bem = db.commit(query, (novo_nome, novo_status, id))
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
        bem = db.commit(query, id)
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

    def get_by_codTombamento(self, codigo_tombamento: str):
        db = DataBase()
        rows = db.execute(self.QUERY_BEM_CODTOMB, (codigo_tombamento,))
        if not rows:
            return None
        row = rows[0]
        return Bem(id=row[0], nome=row[1], codigo_tombamento=row[2], valor=row[3], status=row[4], ativo=row[5])
