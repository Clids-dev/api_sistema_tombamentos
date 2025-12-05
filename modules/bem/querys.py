QUERY_BENS = "SELECT id, nome, codigo_tombamento, valor, status, ativo FROM bens"

QUERY_BEM_ID = "SELECT id, nome, codigo_tombamento, valor, status, ativo FROM bens WHERE id = %s"

QUERY_CREATE_BEM = ('INSERT INTO bens (nome, codigo_tombamento, valor, status, ativo) '
                    'VALUES (%s, %s, %s, %s, %s) '
                    'RETURNING id;')

QUERY_PUT_BEM = ("UPDATE bens SET nome = %s, status = %s "
                 "WHERE bens.id = %s "
                 "RETURNING id, nome, codigo_tombamento, valor, status, ativo")

QUERY_DELETE_BEM = """UPDATE bens SET ativo = FALSE 
                      WHERE bens.id = (%s) 
                      RETURNING id, nome, codigo_tombamento, valor, status, ativo"""

QUERY_BEM_CODTOMB = ("SELECT id, nome, codigo_tombamento, valor, status, ativo "
                     "FROM bens "
                     "WHERE codigo_tombamento = %s")

QUERY_HISTORICO = """SELECT id, bem_id, setor_origem_id, setor_destino_id, data_movimentacao, ativo 
                     FROM movimentacoes WHERE id = %s 
                     ORDER BY data_movimentacao DESC"""

QUERY_BENS_POR_SETOR = """
                       SELECT b.id, b.nome, b.codigo_tombamento,b.valor, b.status, b.ativo, b.status
                       FROM bens b
                       JOIN (SELECT DISTINCT ON (bem_id) bem_id, setor_destino_id 
                             FROM movimentacoes WHERE ativo = TRUE 
                             ORDER BY bem_id, data_movimentacao DESC) m ON m.bem_id = b.id
                       WHERE m.setor_destino_id = %s
                         AND b.ativo = TRUE"""

QUERY_DESATIVAR = "UPDATE bens SET ativo = false WHERE id = %s RETURNING id"

QUERY_REATIVAR = "UPDATE bens SET ativo = true  WHERE id = %s RETURNING id"

QUERY_ULTIMO_SETOR = """
        SELECT setor_destino_id 
        FROM movimentacoes 
        WHERE bem_id = %s AND ativo = TRUE
        ORDER BY data_movimentacao DESC 
        LIMIT 1;
    """

QUERY_RELATORIO_ATIVOS = """
        SELECT status, COUNT(*) AS quantidade
        FROM bens
        WHERE ativo = TRUE
        GROUP BY status;
    """