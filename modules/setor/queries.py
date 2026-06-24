QUERY_SETORES = """SELECT
                        s.id,
                        s.nome,
                        s.responsavel_id,
                        r.nome as responsavel_nome,
                        r.cargo as cargo_responsavel,
                        s.flag_almoxarifado,
                        s.ativo
                    FROM
                        setores s
                    LEFT JOIN
                        responsaveis r ON s.responsavel_id = r.id
                    WHERE
                        s.ativo = TRUE;"""

QUERY_SETOR_BY_ID = """SELECT s.id, s.nome, s.responsavel_id,
                        r.nome as responsavel_nome, r.cargo as cargo_responsavel, 
                        s.flag_almoxarifado, s.ativo
                       FROM setores s
                        LEFT JOIN responsaveis r ON s.responsavel_id = r.id 
                       WHERE s.id = %s AND s.ativo = TRUE;"""
QUERY_CREATE_SETOR = """INSERT INTO setores (nome, responsavel_id, flag_almoxarifado)
                         VALUES (%s, %s, %s) RETURNING id"""

QUERY_PUT_SETOR = """UPDATE setores SET nome = %s, responsavel_id = %s, flag_almoxarifado = %s
                    WHERE id = %s RETURNING id"""

QUERY_DELETE_SETOR = """UPDATE setores SET ativo = FALSE WHERE id = %s RETURNING id"""
