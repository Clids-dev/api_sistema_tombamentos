from datetime import datetime

from core.db import DataBase
from modules.movimentacao.schemas import MovimentacaoCreate, Movimentacao


class MovimentacaoRepository():
    QUERY_MOVIMENTACOES = """
                          SELECT id, bem_id, setor_origem_id, setor_destino_id, data_movimentacao, justificativa
                          FROM movimentacoes
                          WHERE ativo = TRUE
                          """
    QUERY_MOVIMENTACOES_ID = """
                             SELECT id, bem_id, setor_origem_id, setor_destino_id, data_movimentacao, justificativa
                             FROM movimentacoes
                             WHERE id = %s AND ativo = TRUE
                             """
    QUERY_CREATE_MOVIMENTACOES = """
                                 INSERT INTO movimentacoes (bem_id, setor_origem_id, setor_destino_id)
                                 VALUES (%s, %s, %s)
                                     RETURNING id; 
                                 """
    QUERY_PUT_MOVIMENTACAO = """
                             UPDATE movimentacoes
                             SET data_movimentacao = %s, setor_origem_id = %s, justificativa = %s
                             WHERE id = %s AND ativo = TRUE
                                 RETURNING id, bem_id, setor_origem_id, setor_destino_id, data_movimentacao; 
                             """
    QUERY_DELETE_MOVIMENTACAO = """
                                UPDATE movimentacoes
                                SET ativo = FALSE
                                WHERE id = %s
                                    RETURNING id; 
                                """

    #eu tive q fazer um tratamento especial pq o banco ta retornando arrays em vez de inteiros simples
    def get_all(self):
        db = DataBase()
        movimentacoes = db.execute(self.QUERY_MOVIMENTACOES)
        results = []
        for row in movimentacoes:
            origem = row[2]
            if isinstance(origem, (list, tuple)):
                origem = origem[0]
            destino = row[3]
            if isinstance(destino, (list, tuple)):
                destino = destino[0]
            results.append(Movimentacao(
                id=row[0],
                bem_id=row[1],
                setor_origem_id=origem,
                setor_destino_id=destino,
                data=row[4],
                justificativa=row[5],
                ativo=True
            ))
        return results

    def get_id(self, id: int):
        db = DataBase()
        query = self.QUERY_MOVIMENTACOES_ID % id
        rows = db.execute(query)
        if not rows:
            return None
        row = rows[0]
        origem = row[2]
        if isinstance(origem, (list, tuple)):
            origem = origem[0]
        destino = row[3]
        if isinstance(destino, (list, tuple)):
            destino = destino[0]
        return Movimentacao(
            id=row[0],
            bem_id=row[1],
            setor_origem_id=origem,
            setor_destino_id=destino,
            data=row[4],
            justificativa=row[5],
            ativo=True
        )

    def save(self, movimentacao: MovimentacaoCreate):
        db = DataBase()
        query = self.QUERY_CREATE_MOVIMENTACOES
        rows = db.commit(query, (movimentacao.bem_id, movimentacao.setor_origem_id, movimentacao.setor_destino_id,))
        if rows:
            return self.get_id(rows[0])
        return None

    def put(self, id: int, data: datetime, setor_origem_id: int, justificativa: str):
        db = DataBase()
        query = self.QUERY_PUT_MOVIMENTACAO
        movimentacao = db.commit(query, (data, setor_origem_id, justificativa, id,))
        if movimentacao:
            return self.get_id(id)
        return None

    def delete(self, id: int):
        db = DataBase()
        result = self.get_id(id)
        query = self.QUERY_DELETE_MOVIMENTACAO % id
        movimentacao = db.commit(query)
        if movimentacao:
            return Movimentacao(
                id=result.id,
                bem_id=result.bem_id,
                setor_origem_id=result.setor_origem_id,
                setor_destino_id=result.setor_destino_id,
                data=result.data,
                justificativa=result.justificativa,
                ativo=False
            )
        return None
