from core.db import DataBase
from modules.bem.schemas import BemCreate, Bem


class BemRepository(DataBase):
    QUERY_BENS = "SELECT id, nome, codigo_tombamento, valor, status, ativo FROM bens"
    QUERY_BEM_ID = "SELECT id, nome, codigo_tombamento, valor, status, ativo FROM bens WHERE id = %s"
    QUERY_CREATE_BEM = ('INSERT INTO bens (nome, codigo_tombamento, valor, status, ativo) '
                        'VALUES (%s, %s, %s, %s, %s) RETURNING id;')

    def get_all(self):
        db = DataBase()
        rows = db.execute(BemRepository.QUERY_BENS)
        results = []
        if not rows:
            return results

        for row in rows:
            (results.append(Bem(id=row[0], nome=row[1], codigo_tombamento=row[2], valor=row[3], status=row[4], ativo=row[5])))
        return results



    def save(self, bem : BemCreate):
        db = DataBase()
        query = self.QUERY_CREATE_BEM
        result = db.commit(query, (bem.nome, bem.codigo_tombamento, bem.valor, bem.status, True))
        return Bem(id=result[0], nome=bem.nome, codigo_tombamento=bem.codigo_tombamento, valor=bem.valor, status=bem.status , ativo=True)

    def get_by_id(self, id: id):
        db = DataBase()
        query = self.QUERY_BEM_ID % id
        bem = db.execute(query, many =False)
        if bem:
            return {"id": bem[0], "nome": bem[1], "codigo_tombamento": bem[2],
                    "valor": bem[3], "status": bem[4], "ativo": bem[5]}