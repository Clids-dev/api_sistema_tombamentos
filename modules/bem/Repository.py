from core.db import DataBase
from modules.bem.schemas import BemCreate, Bem
from modules.movimentacao.schemas import Movimentacao
from modules.bem import querys


class BemRepository(DataBase):

    def get_all(self):
        db = DataBase()
        rows = db.execute(querys.QUERY_BENS)
        results = []
        if not rows:
            return results
        for row in rows:
            (results.append(Bem(id=row[0], nome=row[1], codigo_tombamento=row[2], valor=row[3], status=row[4], ativo=row[5])))
        return results

    def get_by_id(self, id: int):
        db = DataBase()
        rows = db.execute(querys.QUERY_BEM_ID % id)
        if not rows:
            return None
        row = rows[0]
        return Bem(id=row[0], nome=row[1], codigo_tombamento=row[2], valor=row[3], status=row[4], ativo=row[5])

    def save(self, bem : BemCreate):
        db = DataBase()
        query = querys.QUERY_CREATE_BEM
        result = db.commit(query, (bem.nome, bem.codigo_tombamento, bem.valor, bem.status, True))
        return Bem(id=result[0], nome=bem.nome, codigo_tombamento=bem.codigo_tombamento, valor=bem.valor, status=bem.status , ativo=True)

    def put(self, id: int, novo_nome: str, novo_status: str):
        db = DataBase()
        query = querys.QUERY_PUT_BEM
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
        query = querys.QUERY_DELETE_BEM % id
        bem = db.commit(query, id)
        if bem:
            return Bem(
                id=bem[0],
                nome=bem[1],
                codigo_tombamento=bem[2],
                valor=bem[3],
                status=bem[4],
                ativo=False
            )
        return None

    def get_by_codTombamento(self, codigo_tombamento: str):
        db = DataBase()
        rows = db.execute(querys.QUERY_BEM_CODTOMB, (codigo_tombamento,))
        if not rows:
            return None
        row = rows[0]
        return Bem(id=row[0], nome=row[1], codigo_tombamento=row[2], valor=row[3], status=row[4], ativo=row[5])

    def get_historico_by_bem(self, id: int):
        db = DataBase()
        rows = db.execute(querys.QUERY_HISTORICO, (id,))
        results = []
        for row in rows:
            results.append(
                Movimentacao(
                    id=row[0],
                    bem_id=row[1],
                    setor_origem_id=row[2],
                    setor_destino_id=row[3],
                    data=row[4],
                    ativo=bool(row[5])
                )
            )
        return results

    def get_bens_por_setor(self, setor_id: int):
        db = DataBase()
        rows = db.execute(querys.QUERY_BENS_POR_SETOR, (setor_id,))
        results = []
        for row in rows:
            results.append(
                Bem(
                    id=row[0],
                    nome=row[1],
                    codigo_tombamento=row[2],
                    valor=row[3],
                    status=row[4],
                    ativo=bool(row[5])
                )
            )
        return results

    def desativar(self, bem_id: int):
        db = DataBase()
        return db.commit(querys.QUERY_DESATIVAR, (bem_id,))

    def reativar(self, bem_id: int):
        db = DataBase()
        return db.commit(querys.QUERY_REATIVAR, (bem_id,))

    def relatorio_bens_ativos_por_status(self):
        db = DataBase()
        rows = db.execute(querys.QUERY_RELATORIO_ATIVOS)
        return [
            {"status": row[0], "quantidade": row[1]}
            for row in rows
            ]
