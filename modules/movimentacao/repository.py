from datetime import datetime
from typing import Optional
from core.database import DataBase
from modules.movimentacao.schemas import MovimentacaoCreate, Movimentacao
from . import queries, schemas

class MovimentacaoRepository:
    def get_all(self):
        db = DataBase()
        rows = db.execute(queries.QUERY_MOVIMENTACOES)
        results = []
        if not rows:
            return results
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

    def get_detailed(self):
        db = DataBase()
        rows = db.execute(queries.QUERY_MOVIMENTACOES_DETALHADAS)
        results = []
        if not rows:
            return results
        for row in rows:
            results.append(
                schemas.MovimentacaoDetailed(
                    id=row[0],
                    bem_nome=row[1],
                    codigo_tombamento=row[2],
                    setor_origem_nome=row[3],
                    setor_destino_nome=row[4],
                    data_movimentacao=row[5],
                    justificativa=row[6],
                    ativo=bool(row[7])
                )
            )
        return results

    def get_by_bem_codigo(self, codigo: str):
        db = DataBase()
        rows = db.execute(queries.QUERY_MOVIMENTACOES_POR_BEM_CODIGO, (codigo,))
        results = []
        if not rows:
            return results
        for row in rows:
            results.append(
                schemas.MovimentacaoDetailed(
                    id=row[0],
                    bem_nome=row[1],
                    codigo_tombamento=row[2],
                    setor_origem_nome=row[3],
                    setor_destino_nome=row[4],
                    data_movimentacao=row[5],
                    justificativa=row[6],
                    ativo=bool(row[7])
                )
            )
        return results

    def get_id(self, id: int):
        db = DataBase()
        rows = db.execute(queries.QUERY_MOVIMENTACOES_ID, (id,))
        if not rows:
            return None
        row = rows[0]
        return Movimentacao(
            id=row[0], 
            bem_id=row[1], 
            setor_origem_id=row[2], 
            setor_destino_id=row[3], 
            data=row[4], 
            ativo=bool(row[5])
        )

    def save(self, movimentacao: MovimentacaoCreate):
        db = DataBase()
        result = db.commit(queries.QUERY_CREATE_MOVIMENTACOES, (movimentacao.bem_id, movimentacao.setor_origem_id, movimentacao.setor_destino_id, datetime.now(), movimentacao.justificativa))
        if result:
            return Movimentacao(
                id=result[0], 
                bem_id=result[1], 
                setor_origem_id=result[2], 
                setor_destino_id=result[3], 
                data=result[4], 
                ativo=result[5]
            )
        return None

    def put(self, id: int, data: datetime, setor_destino_id: int, justificativa: Optional[str] = None):
        db = DataBase()
        movimentacao = db.commit(queries.QUERY_PUT_MOVIMENTACAO, (data, setor_destino_id, justificativa, id))
        if movimentacao:
            return Movimentacao(
                id=movimentacao[0],
                bem_id=movimentacao[1],
                setor_origem_id=movimentacao[2],
                setor_destino_id=movimentacao[3],
                data=movimentacao[4],
                justificativa=movimentacao[5],
                ativo=movimentacao[6]
            )
        return None

    def delete(self, id: int):
        db = DataBase()
        movimentacao = db.commit(queries.QUERY_DELETE_MOVIMENTACAO, (id,))
        if movimentacao:
            return Movimentacao(
                id=movimentacao[0],
                bem_id=movimentacao[1],
                setor_origem_id=movimentacao[2],
                setor_destino_id=movimentacao[3],
                data=movimentacao[4],
                ativo=False
            )
        return None
