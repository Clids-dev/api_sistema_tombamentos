from core.db import DataBase
from modules.responsavel.schemas import Responsavel
from modules.setor.schemas import SetorCreate, Setor, SetorFlat


class SetorRepository:
    QUERY_SETORES = """SELECT
                            s.id as id_setor,
                            s.nome as setor,
                            s.responsavel_id as id_responsavel,
                            r.nome as responsaveis,
                            r.cargo as cargo_responsavel
                        FROM
                            setores s
                        JOIN
                            responsaveis r ON s.responsavel_id = r.id
                        WHERE 
                            s.ativo = TRUE;"""

    QUERY_SETOR_BY_ID = """SELECT
                            s.id as id_setor,
                            s.nome as setor,
                            s.responsavel_id as id_responsavel,
                            r.nome as responsaveis,
                            r.cargo as cargo_responsavel
                            FROM
                            setores s
                            JOIN
                            responsaveis r ON s.responsavel_id = r.id 
                           WHERE 
                                s.id = (%s)
                                AND s.ativo = TRUE;"""

    QUERY_CREATE_SETOR = """
                             INSERT INTO setores (nome, responsavel_id)
                             VALUES (%s, %s)
                             RETURNING id"""
    QUERY_PUT_SETOR = """UPDATE
                        setores SET 
                        nome = (%s),
                        responsavel_id = (%s) 
                        WHERE 
                        setores.id = (%s)
                        RETURNING id"""
    QUERY_DELETE_SETOR = """UPDATE
                            setores SET
                            ativo = FALSE WHERE setores.id = (%s) RETURNING id"""

    def get_all(self):
        db = DataBase()
        rows = db.execute(self.QUERY_SETORES)
        results = []
        for row in rows:
            results.append(SetorFlat(
            id_setor=row[0]
                , setor=row[1]
                , id_responsavel=row[2]
                , responsavel = row[3]
                , cargo_responsavel=row[4]
                , ativo=True))
        return results

    def get_id(self, id: int):
        db = DataBase()
        query = self.QUERY_SETOR_BY_ID % id
        rows = db.execute(query)
        if not rows:
            return None
        row = rows[0]
        return SetorFlat(id_setor=row[0]
                         , setor=row[1]
                         , id_responsavel=row[2]
                         , responsavel = row[3]
                         , cargo_responsavel=row[4]
                         , ativo=True)


    def save(self, setor: SetorCreate):
        db = DataBase()
        query = self.QUERY_CREATE_SETOR
        setor = db.commit(query, (setor.nome, setor.responsavel_id,))
        if setor:
            return self.get_id(setor.id)
        return None

    def put(self, id: int, novo_nome: str, novo_responsavel_id: int):
        db = DataBase()
        query = self.QUERY_PUT_SETOR
        setor = db.commit(query, (novo_nome, novo_responsavel_id, id,))
        if setor:
            return self.get_id(id)
        return None

    def delete(self, id: int):
        db = DataBase()
        query = self.QUERY_DELETE_SETOR % id
        setor = db.commit(query)
        if setor:
            return self.get_id(id)
        return None