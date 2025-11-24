from modules.bem.Repository import BemRepository
from modules.bem.schemas import BemCreate


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
