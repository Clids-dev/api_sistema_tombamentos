from fastapi import HTTPException

from modules.bem.Repository import BemRepository
from modules.bem.schemas import BemCreate


class BemService:
    def get_bens(self):
        repository = BemRepository()
        return repository.get_all()

    def get_bem_by_id(self, id: int):
        try:
            repository = BemRepository()
            if id == "":
                raise ValueError("ID do bem não pode ser vazio.")
            if repository.get_id(id) is None:
                raise ValueError("Nenhum bem encontrado.")
            return repository.get_id(id)
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))

    def create_bem(self, bem : BemCreate):
        try:
            repository = BemRepository()
            if bem.nome.strip() == "":
                raise ValueError("Nome do bem não pode ser vazio.")
            for b in repository.get_all():
                if b.nome == bem.nome:
                    raise FileExistsError("Bem já existente.")
            return repository.save(bem)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    def put_bem(self, id: int, novo_nome: str, novo_status: str):
        try:
            repository = BemRepository()
            if self.get_bem_by_id(id) is None:
                raise HTTPException(status_code=404, detail=f"Bem com id {id} não encontrado")
            if novo_nome == "" and novo_status == "":
                raise ValueError("Nenhum dado fornecido para atualização.")
            if novo_nome == "":
                novo_nome = self.get_bem_by_id(id).nome
            if novo_status == "":
                novo_status = self.get_bem_by_id(id).status
            if novo_nome == self.get_bem_by_id(id).nome and novo_status == self.get_bem_by_id(id).status:
                raise ValueError("Os dados fornecidos são iguais aos atuais.")
            return repository.put(int(id), novo_nome, novo_status)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except HTTPException as e:
            raise e

    def delete_bem(self, id: int):
        try:
            repository = BemRepository()
            if self.get_bem_by_id(id) is None:
                raise HTTPException(status_code=404, detail=f"Bem com id {id} não encontrado")
            if self.get_bem_by_id(id).ativo == False:
                raise HTTPException(status_code=400, detail="Bem já está inativo.")
            return repository.delete(id)
        except HTTPException as e:
            raise e