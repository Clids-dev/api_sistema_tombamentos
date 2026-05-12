from core.database import DataBase
from modules.setor.schemas import SetorCreate, SetorFlat
from . import queries

class SetorRepository:
    def get_all(self):
        db = DataBase()
        rows = db.execute(queries.QUERY_SETORES)
        results = []
        if not rows:
            return results
        for row in rows:
            results.append(SetorFlat(
                id_setor=row[0],
                setor=row[1],
                id_responsavel=row[2],
                responsavel=row[3],
                cargo_responsavel=row[4],
                flag_almoxarifado=bool(row[5])
            ))
        return results

    def get_id(self, id: int):
        db = DataBase()
        rows = db.execute(queries.QUERY_SETOR_BY_ID, (id,))
        if not rows:
            return None
        row = rows[0]
        return SetorFlat(
            id_setor=row[0],
            setor=row[1],
            id_responsavel=row[2],
            responsavel=row[3],
            cargo_responsavel=row[4],
            flag_almoxarifado=bool(row[5])
        )

    def save(self, setor: SetorCreate):
        db = DataBase()
        result = db.commit(queries.QUERY_CREATE_SETOR, (setor.nome, setor.responsavel_id, setor.flag_almoxarifado))
        if result:
            return self.get_id(result[0])
        return None

    def put(self, id: int, novo_nome: str, novo_responsavel_id: int, flag_almoxarifado: bool = False):
        db = DataBase()
        result = db.commit(queries.QUERY_PUT_SETOR, (novo_nome, novo_responsavel_id, flag_almoxarifado, id))
        if result:
            return self.get_id(id)
        return None

    def delete(self, id: int):
        db = DataBase()
        result = db.commit(queries.QUERY_DELETE_SETOR, (id,))
        if result:
            return self.get_id(id)
        return None
