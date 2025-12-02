from modules.bem.Repository import BemRepository
from modules.bem.schemas import BemCreate

from psycopg2 import errors
from fastapi import HTTPException

class BemService:
    def get_bens(self):
        repository = BemRepository()
        return repository.get_all()

    def get_bem_by_id(self, id: int):
        repository = BemRepository()
        return repository.get_by_id(id)

    def create_bem(self, bem : BemCreate):
        repository = BemRepository()
        return repository.save(bem)

    def put_bem(self, id: int, novo_nome: str, status: str):
        try:
            repository = BemRepository()
            return repository.put(id, novo_nome, status)
        except errors.NoDataFound:
            raise HTTPException(status_code=404, detail=f"Bem com id {id} não encontrada")
        except errors.UniqueViolation:
            raise HTTPException(status_code=409, detail=f"Bem {novo_nome} já existe")

    def delete_bem(self, id: int):
        try:
            repository = BemRepository()
            return repository.delete(id)
        except errors.NoDataFound:
            raise HTTPException(status_code=404, detail=f"Categoria com id {id} não encontrada")

    def get_by_codTomb(self, codigo_tombamento: str):
        repository = BemRepository()
        bem = repository.get_by_codTombamento(codigo_tombamento)
        if not bem:
            raise HTTPException(
                status_code=404,
                detail="Bem não encontrado com esse código de tombamento"
            )

        return bem

    def get_historico_by_bem(self, bem_id: int):
        if not isinstance(bem_id, int) or bem_id <= 0:
            raise HTTPException(status_code=400, detail="ID do bem inválido.")

        repository = BemRepository()

        try:
            historico = repository.get_historico_by_bem(bem_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao obter histórico: {str(e)}")

        return historico

    def get_por_setor(self, setor_id: int):
        if not isinstance(setor_id, int) or setor_id <= 0:
            raise HTTPException(status_code=400, detail="ID do setor inválido.")

        repository = BemRepository()

        try:
            bens = repository.get_bens_por_setor(setor_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao buscar bens por setor: {str(e)}")

        return bens

    def desativar_bem(self, bem_id: int):
        repo = BemRepository()

        bem = repo.get_by_id(bem_id)
        if not bem:
            raise HTTPException(404, "Bem não encontrado")

        repo.desativar(bem_id)

        return {
            "id": bem_id,
            "ativo": False,
            "message": "Bem desativado"
        }

    def reativar_bem(self, bem_id: int):
        repo = BemRepository()

        bem = repo.get_by_id(bem_id)
        if not bem:
            raise HTTPException(404, "Bem não encontrado")

        repo.reativar(bem_id)

        return {
            "id": bem_id,
            "ativo": True,
            "message": "Bem reativado"
        }

    def bens_ativos_por_status(self):
        repository = BemRepository()
        return repository.relatorio_bens_ativos_por_status()