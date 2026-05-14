QUERY_MOVIMENTACOES = """SELECT id, bem_id, setor_origem_id, setor_destino_id, data_movimentacao, ativo
                      FROM movimentacoes WHERE ativo = TRUE"""

QUERY_MOVIMENTACOES_DETALHADAS = """
    SELECT 
        m.id, 
        b.nome as bem_nome, 
        b.codigo_tombamento,
        s1.nome as setor_origem_nome, 
        s2.nome as setor_destino_nome, 
        m.data_movimentacao, 
        m.justificativa,
        m.ativo
    FROM movimentacoes m
    JOIN bens b ON m.bem_id = b.id
    LEFT JOIN setores s1 ON m.setor_origem_id = s1.id
    JOIN setores s2 ON m.setor_destino_id = s2.id
    WHERE m.ativo = TRUE
    ORDER BY m.data_movimentacao DESC
"""

QUERY_MOVIMENTACOES_POR_BEM_CODIGO = """
    SELECT 
        m.id, 
        b.nome as bem_nome, 
        b.codigo_tombamento,
        s1.nome as setor_origem_nome, 
        s2.nome as setor_destino_nome, 
        m.data_movimentacao, 
        m.justificativa,
        m.ativo
    FROM movimentacoes m
    JOIN bens b ON m.bem_id = b.id
    LEFT JOIN setores s1 ON m.setor_origem_id = s1.id
    JOIN setores s2 ON m.setor_destino_id = s2.id
    WHERE b.codigo_tombamento = %s AND m.ativo = TRUE
    ORDER BY m.data_movimentacao DESC
"""

QUERY_MOVIMENTACOES_ID = """SELECT id, bem_id, setor_origem_id, setor_destino_id, data_movimentacao, ativo FROM movimentacoes WHERE id = %s"""

QUERY_CREATE_MOVIMENTACOES = """INSERT INTO movimentacoes (bem_id, setor_origem_id, setor_destino_id, data_movimentacao, justificativa, ativo)
                                VALUES (%s, %s, %s, %s, %s, TRUE)
                                RETURNING id, bem_id, setor_origem_id, setor_destino_id, data_movimentacao, ativo;"""

QUERY_PUT_MOVIMENTACAO = """UPDATE movimentacoes SET data_movimentacao = %s, setor_origem_id = %s, justificativa = %s 
                            WHERE id = %s AND ativo = TRUE 
                            RETURNING id, bem_id, setor_origem_id, setor_destino_id, data_movimentacao, justificativa, ativo;"""

QUERY_DELETE_MOVIMENTACAO = """UPDATE movimentacoes SET ativo = FALSE WHERE id = %s RETURNING id, bem_id, setor_origem_id, setor_destino_id, data_movimentacao, ativo;"""
