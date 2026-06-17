QUERY_STATS_CATEGORIA = """
    SELECT c.nome, COUNT(b.id) as total
    FROM categorias c
    LEFT JOIN bens b ON b.id_categoria = c.id AND b.ativo = TRUE
    WHERE c.ativo = TRUE
    GROUP BY c.nome
    ORDER BY total DESC
"""

QUERY_STATS_STATUS = """
    SELECT status, COUNT(id) as total
    FROM bens
    WHERE ativo = TRUE
    GROUP BY status
    ORDER BY total DESC
"""
