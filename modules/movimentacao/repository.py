from datetime import datetime
from typing import Optional

from core.db import DataBase
from modules.movimentacao.schemas import MovimentacaoCreate, Movimentacao


class MovimentacaoRepository():
    db = DataBase()
    QUERY_MOVIMENTACOES = """SELECT id, bem_id, setor_origem_id, setor_destino_id, data_movimentacao, ativo
                          FROM movimentacoes WHERE ativo = TRUE"""

    QUERY_MOVIMENTACOES_ID = """SELECT id, bem_id, setor_origem_id, setor_destino_id, data_movimentacao, ativo FROM movimentacoes WHERE id = %s"""

    QUERY_CREATE_MOVIMENTACOES = """INSERT INTO movimentacoes (bem_id, setor_origem_id, setor_destino_id, data_movimentacao)
                                    VALUES (%s, %s, %s, %s, TRUE)
                                    RETURNING id, bem_id, setor_origem_id, setor_destino_id, data_movimentacao;"""

    QUERY_PUT_MOVIMENTACAO = """UPDATE movimentacoes SET data_movimentacao = %s, setor_origem_id = %s,justificativa = %s 
                                WHERE id = %s AND ativo = TRUE 
                                RETURNING id, bem_id, setor_origem_id, setor_destino_id, data_movimentacao, justificativa, ativo;"""

    QUERY_DELETE_MOVIMENTACAO = """UPDATE movimentacoes SET ativo = FALSE WHERE id = %s RETURNING id;"""


    def get_all(self):
        db = DataBase()
        rows = db.execute(self.QUERY_MOVIMENTACOES)
        results = []
        if not rows:
            return results
        for row in rows:
            (results.append(
                Movimentacao(id=row[0], bem_id=row[1], setor_origem_id=row[2], setor_destino_id=row[3], data=row[4], ativo=bool(row[5]))))
        return results

    def get_id(self, id: int):
        db = DataBase()
        rows = db.execute(self.QUERY_MOVIMENTACOES_ID % id)
        if not rows:
            return None
        row = rows[0]
        return Movimentacao(id=row[0], bem_id=row[1], setor_origem_id=row[2], setor_destino_id=row[3], data=row[4], ativo=bool(row[5]))

    def save(self, movimentacao: MovimentacaoCreate):
        db = DataBase()
        query = self.QUERY_CREATE_MOVIMENTACOES
        result = db.commit(query, (movimentacao.bem_id, movimentacao.setor_origem_id, movimentacao.setor_destino_id, True))
        return Movimentacao(id=result[0], bem_id=result[1], setor_origem_id=result[2], setor_destino_id=result[3], data=result[4], ativo=result[5])

    def put(self, id: int, data: datetime, setor_origem_id: int,  justificativa: Optional[str] = None):
        db = DataBase()
        query = self.QUERY_PUT_MOVIMENTACAO
        movimentacao = db.commit(query, (data, setor_origem_id, justificativa, id))
        if movimentacao:
            return Movimentacao(
                id=movimentacao[0],
                bem_id=movimentacao[1],
                setor_origem_id=movimentacao[2],
                setor_destino_id=movimentacao[3],
                data=movimentacao[4],
                justificativa= movimentacao[5],
                ativo=movimentacao[6]
            )
        return None

    def delete(self, id: int):
        db = DataBase()
        result = self.get_id(id)
        query = self.QUERY_DELETE_MOVIMENTACAO % id
        movimentacao = db.commit(query, id)
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
