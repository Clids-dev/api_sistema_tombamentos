from fastapi import HTTPException

from modules.responsavel.repository import ResponsavelRepository
from modules.responsavel.schemas import ResponsavelCreate


class ResponsavelService:
    def get_responsaveis(self):
        try:
            repository = ResponsavelRepository()
            if repository.get_all() is None:
                raise ValueError
            return repository.get_all()
        except ValueError:
            raise HTTPException(status_code=404, detail="Nenhum responsável encontrado")

    def get_responsavel_by_id(self, id: int):
        try:
            task = ResponsavelRepository().get_id(id)
            if task is None:
                raise ValueError
            return task
        except ValueError:
            raise HTTPException(status_code=404, detail=f"Responsável com id {id} não encontrado")

    def create_responsavel(self, responsavel: ResponsavelCreate):
        try:
            repository = ResponsavelRepository()
            if responsavel.nome.strip() == "" or responsavel.cargo.strip() == "":
                raise ValueError
            for resp in repository.get_all():
                if resp.nome == responsavel.nome and resp.cargo == responsavel.cargo:
                    raise FileExistsError
            return repository.save(responsavel)
        except ValueError:
            raise HTTPException(status_code=400, detail="Nome ou cargo do responsável não podem ser vazios")
        except FileExistsError:
            raise HTTPException(status_code=409, detail=f"Responsável {responsavel.nome} com cargo {responsavel.cargo} já existe")


    def put_responsavel(self, id: int, novo_nome: str, novo_cargo: str):
        try:
            repository = ResponsavelRepository()
            if self.get_responsavel_by_id(id) is None:
                raise HTTPException(status_code=404, detail=f"Responsável com id {id} não encontrado")
            if novo_nome == "" and novo_cargo == "":
                raise HTTPException(status_code=400, detail="Nenhum dado fornecido para atualização.")
            if (novo_cargo == repository.get_id(id).cargo and novo_nome == repository.get_id(id).nome):
                raise ValueError
            if (novo_cargo == repository.get_id(id).cargo and novo_nome == ""):
                raise ValueError
            if (novo_nome == repository.get_id(id).nome and novo_cargo == ""):
                raise ValueError
            if novo_nome == "":
                novo_nome = repository.get_id(id).nome
            if novo_cargo == "":
                novo_cargo = repository.get_id(id).cargo
            return repository.put(id, novo_nome, novo_cargo)
        except ValueError:
            raise HTTPException(status_code=400, detail="Os novos dados são iguais aos dados atuais do responsável.")

    def delete_responsavel(self, id: int):
        try:
            if self.get_responsavel_by_id(id) is None:
                raise FileNotFoundError
            service = ResponsavelRepository().delete(id)
            return service
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail=f"Responsável com id {id} não encontrado")
