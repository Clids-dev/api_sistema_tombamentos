from core.database import DataBase
from modules.bem.schemas import BemCreate, Bem, BemDetalhes
from modules.movimentacao.schemas import Movimentacao
from modules.bem import queries as queries


class BemRepository(DataBase):

    def get_all(self):
        db = DataBase()
        rows = db.execute(queries.QUERY_BENS)
        results = []
        if not rows:
            return results
        for row in rows:
            results.append(Bem(id=row[0], nome=row[1], tipo=row[2], codigo_tombamento=row[3], valor=row[4], status=row[5], ativo=row[6], id_categoria=row[7]))
        return results

    def get_by_id(self, id: int):
        db = DataBase()
        rows = db.execute(queries.QUERY_BEM_ID, (id,))
        if not rows:
            return None
        row = rows[0]
        return Bem(id=row[0], nome=row[1], tipo=row[2], codigo_tombamento=row[3], valor=row[4], status=row[5], ativo=row[6], id_categoria=row[7])

    def get_detalhes(self, id: int):
        db = DataBase()
        rows = db.execute(queries.QUERY_BEM_DETALHES, (id,))
        if not rows:
            return None
        row = rows[0]
        return BemDetalhes(
            id=row[0],
            nome=row[1],
            tipo=row[2],
            codigo_tombamento=row[3],
            valor=row[4],
            status=row[5],
            ativo=row[6],
            setor_atual=row[7],
            data_ultima_movimentacao=row[8],
            justificativa=row[9],
            id_setor_atual=row[10],
            id_categoria=row[11],
            categoria_nome=row[12]
        )

    def save(self, bem : BemCreate):
        db = DataBase()
        query = queries.QUERY_CREATE_BEM
        result = db.commit(query, (bem.nome, bem.tipo, bem.codigo_tombamento, bem.valor, bem.status, True, bem.id_categoria))
        return Bem(id=result[0], nome=bem.nome, tipo=bem.tipo, codigo_tombamento=bem.codigo_tombamento, valor=bem.valor, status=bem.status , ativo=True, id_categoria=bem.id_categoria)

    def count_by_categoria(self, id_categoria: int):
        db = DataBase()
        rows = db.execute(queries.QUERY_COUNT_BY_CATEGORIA, (id_categoria,))
        return rows[0][0] if rows else 0

    def put(self, id: int, novo_nome: str, novo_status: str):
        db = DataBase()
        query = queries.QUERY_PUT_BEM
        bem = db.commit(query, (novo_nome, novo_status, id))
        if bem:
            return Bem(
                id=bem[0],
                nome=bem[1],
                tipo=bem[2],
                codigo_tombamento=bem[3],
                valor=bem[4],
                status=bem[5],
                ativo=bem[6],
                id_categoria=bem[7]
            )
        return None

    def delete(self, id: int):
        db = DataBase()
        query = queries.QUERY_DELETE_BEM
        bem = db.commit(query, (id,))
        if bem:
            return Bem(
                id=bem[0],
                nome=bem[1],
                tipo=bem[2],
                codigo_tombamento=bem[3],
                valor=bem[4],
                status=bem[5],
                ativo=False,
                id_categoria=bem[7]
            )
        return None

    def get_by_codTombamento(self, codigo_tombamento: str):
        db = DataBase()
        rows = db.execute(queries.QUERY_BEM_CODTOMB, (codigo_tombamento,))
        if not rows:
            return None
        row = rows[0]
        return Bem(id=row[0], nome=row[1], tipo=row[2], codigo_tombamento=row[3], valor=row[4], status=row[5], ativo=row[6], id_categoria=row[7])

    def get_historico_by_bem(self, id: int):
        db = DataBase()
        rows = db.execute(queries.QUERY_HISTORICO, (id,))
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
        rows = db.execute(queries.QUERY_BENS_POR_SETOR, (setor_id,))
        results = []
        for row in rows:
            results.append(
                Bem(
                    id=row[0],
                    nome=row[1],
                    tipo=row[2],
                    codigo_tombamento=row[3],
                    valor=row[4],
                    status=row[5],
                    ativo=bool(row[6]),
                    id_categoria=row[7]
                )
            )
        return results

    def desativar(self, bem_id: int):
        db = DataBase()
        return db.commit(queries.QUERY_DESATIVAR, (bem_id,))

    def reativar(self, bem_id: int):
        db = DataBase()
        return db.commit(queries.QUERY_REATIVAR, (bem_id,))

    def relatorio_bens_ativos_por_status(self):
        db = DataBase()
        rows = db.execute(queries.QUERY_RELATORIO_ATIVOS)
        return [
            {"status": row[0], "quantidade": row[1]}
            for row in rows
            ]

    def quantidade_total_bens(self):
        db = DataBase()
        return db.execute(queries.QUERY_QUANTIDADE_BENS)

    def quantidade_bens_ativos(self):
        db = DataBase()
        return db.execute(queries.QUERY_QUANTIDADE_BENS_ATIVOS)

    def quantidade_bens_inativos(self):
        db = DataBase()
        return db.execute(queries.QUERY_QUANTIDADE_BENS_INATIVOS)

    def get_registros_recentes(self):
        db = DataBase()
        return db.execute(queries.QUERY_RECENTES)
