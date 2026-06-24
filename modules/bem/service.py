from fastapi import HTTPException
from modules.bem.repository import BemRepository
from modules.bem.schemas import BemCreate
from modules.categoria.repository import CategoriaRepository
from modules.bem.queries_stats import QUERY_STATS_CATEGORIA, QUERY_STATS_STATUS
from core.database import DataBase
from psycopg2 import errors

class BemService:
    def get_bens(self):
        repository = BemRepository()
        return repository.get_all()

    def get_stats_categoria(self):
        db = DataBase()
        return db.execute(QUERY_STATS_CATEGORIA)

    def get_stats_status(self):
        db = DataBase()
        return db.execute(QUERY_STATS_STATUS)

    def get_bem_by_id(self, id: int):
        try:
            repository = BemRepository()
            if id == "":
                raise ValueError("ID do bem não pode ser vazio.")
            bem = repository.get_by_id(id)
            if bem is None:
                raise ValueError("Nenhum bem encontrado.")
            return bem
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))

    def get_bem_detalhes(self, id: int):
        repository = BemRepository()
        bem = repository.get_detalhes(id)
        if not bem:
            raise HTTPException(status_code=404, detail="Bem não encontrado")
        return bem

    def create_bem(self, bem : BemCreate):
        repository = BemRepository()
        return repository.save(bem)

    def put_bem(self, id: int, novo_nome: str, novo_tipo: str, status: str):
        try:
            repository = BemRepository()
            return repository.put(id, novo_nome, novo_tipo, status)
        except errors.NoDataFound:
            raise HTTPException(status_code=404, detail=f"Bem com id {id} não encontrada")
        except errors.UniqueViolation:
            raise HTTPException(status_code=409, detail=f"Bem {novo_nome} já existe")

    def delete_bem(self, id: int):
        try:
            repository = BemRepository()
            return repository.delete(id)
        except errors.NoDataFound:
            raise HTTPException(status_code=404, detail=f"Bem com id {id} não encontrado")

    def get_by_codTomb(self, codigo_tombamento: str):
        repository = BemRepository()
        bem = repository.get_by_codTombamento(codigo_tombamento)
        if not bem:
            raise HTTPException(
                status_code=404,
                detail="Bem não encontrado com esse código de tombamento"
            )
        return bem

    def get_proximo_codigo(self, id_categoria: int):
        repo_cat = CategoriaRepository()
        repo_bem = BemRepository()
        
        categoria = repo_cat.get_id(id_categoria)
        if not categoria:
            raise HTTPException(status_code=404, detail="Categoria não encontrada")
        
        quantidade = repo_bem.count_by_categoria(id_categoria)
        proximo_numero = quantidade + 1
        
        # Formata com zeros à esquerda (ex: INF-001)
        return f"{categoria.sigla}-{str(proximo_numero).zfill(3)}"

    def quantidade_bens(self):
        repo = BemRepository()
        res = repo.quantidade_total_bens()
        return res[0][0] if res else 0

    def quantidade_bens_ativos(self):
        repo = BemRepository()
        res = repo.quantidade_bens_ativos()
        return res[0][0] if res else 0

    def quantidade_bens_inativos(self):
        repo = BemRepository()
        res = repo.quantidade_bens_inativos()
        return res[0][0] if res else 0

    def bens_recentes(self):
        repo = BemRepository()
        return repo.get_registros_recentes()

    def get_historico_by_bem(self, bem_id: int):
        repository = BemRepository()
        return repository.get_historico_by_bem(bem_id)

    def get_por_setor(self, setor_id: int):
        repository = BemRepository()
        return repository.get_bens_por_setor(setor_id)

    def desativar_bem(self, bem_id: int):
        repo = BemRepository()
        bem = repo.get_by_id(bem_id)
        if not bem:
            raise HTTPException(404, "Bem não encontrado")
        repo.desativar(bem_id)
        return {"id": bem_id, "ativo": False}

    def reativar_bem(self, bem_id: int):
        repo = BemRepository()
        bem = repo.get_by_id(bem_id)
        if not bem:
            raise HTTPException(404, "Bem não encontrado")
        repo.reativar(bem_id)
        return {"id": bem_id, "ativo": True}
