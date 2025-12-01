from datetime import datetime

from core.db import DataBase
from modules.movimentacao.schemas import MovimentacaoCreate


class MovimentacaoRepository():
    QUERY_MOVIMENTACOES = """
                          SELECT id, bem_id, setor_origem_id, setor_destino_id, data
                          FROM movimentacoes
                          WHERE ativo = TRUE
                          """
    QUERY_MOVIMENTACOES_ID = """
                             SELECT id, bem_id, setor_origem_id, setor_destino_id, data
                             """
    QUERY_CREATE_MOVIMENTACOES = """
                                 INSERT INTO movimentacoes (bem_id, setor_origem_id, setor_destino_id, data, ativo)
                                 VALUES (%s, %s, %s, %s, %s, TRUE)
                                     RETURNING id, bem_id, setor_origem_id, setor_destino_id, data; 
                                 """
    QUERY_PUT_MOVIMENTACAO = """
                             UPDATE movimentacoes
                             SET data = %s, setor_origem_id = %s
                             WHERE id = %s AND ativo = TRUE
                                 RETURNING id, bem_id, setor_origem_id, setor_destino_id, data; 
                             """
    QUERY_DELETE_MOVIMENTACAO = """
                                UPDATE movimentacoes
                                SET ativo = FALSE
                                WHERE id = %s
                                    RETURNING id; 
                                """

    def get_all(self):
        db = DataBase()
        movimentacoes = db.execute(self.QUERY_MOVIMENTACOES)
        results = []
        for movimentacao in movimentacoes:
            results.append(movimentacao)
        return results

    def get_id(self, id: int):
        db = DataBase()
        query = self.QUERY_MOVIMENTACOES_ID % id
        movimentacao = db.execute(query, many=False)
        if movimentacao:
            return {movimentacao[0], movimentacao[1], movimentacao[2], movimentacao[3], movimentacao[4], movimentacao[5]}
        return {}

    def save(self, movimentacao: MovimentacaoCreate):
        db = DataBase()
        query = self.QUERY_CREATE_MOVIMENTACOES % (f"{movimentacao.bem_id}, {movimentacao.setor_origem_id}, {movimentacao.setor_destino_id}")
        movimentacao = db.commit(query)
        return {"bem_id": movimentacao[0], "setor_destino_id": movimentacao[1], "setor_destino_origem": movimentacao[2]}

    def put(self, id: int, data: datetime, setor_origem_id: int):
        db = DataBase()
        query = self.QUERY_PUT_MOVIMENTACAO % f"{id},{data},{setor_origem_id}"
        movimentacao = db.execute(query)
        if movimentacao:
            return {"bem_id": movimentacao[0], "setor_destino_id": movimentacao[1], "setor_destino_origem": movimentacao[2]}
        return {}

    def delete(self, id: int):
        db = DataBase()
        query = self.QUERY_DELETE_MOVIMENTACAO % id
        movimentacao = db.execute(query, many=False)
        if movimentacao:
            return {"bem_id": movimentacao[0], "setor_destino_id": movimentacao[1], "setor_destino_origem": movimentacao[2]}
        return {}
