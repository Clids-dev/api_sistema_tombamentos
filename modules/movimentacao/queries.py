QUERY_MOVIMENTACOES = """SELECT id, bem_id, setor_origem_id, setor_destino_id, data_movimentacao, ativo
                      FROM movimentacoes WHERE ativo = TRUE"""

QUERY_MOVIMENTACOES_ID = """SELECT id, bem_id, setor_origem_id, setor_destino_id, data_movimentacao, ativo FROM movimentacoes WHERE id = %s"""

QUERY_CREATE_MOVIMENTACOES = """INSERT INTO movimentacoes (bem_id, setor_origem_id, setor_destino_id, data_movimentacao, ativo)
                                VALUES (%s, %s, %s, %s, TRUE)
                                RETURNING id, bem_id, setor_origem_id, setor_destino_id, data_movimentacao, ativo;"""

QUERY_PUT_MOVIMENTACAO = """UPDATE movimentacoes SET data_movimentacao = %s, setor_origem_id = %s, justificativa = %s 
                            WHERE id = %s AND ativo = TRUE 
                            RETURNING id, bem_id, setor_origem_id, setor_destino_id, data_movimentacao, justificativa, ativo;"""

QUERY_DELETE_MOVIMENTACAO = """UPDATE movimentacoes SET ativo = FALSE WHERE id = %s RETURNING id, bem_id, setor_origem_id, setor_destino_id, data_movimentacao, ativo;"""
