from ..exceptions import NotFoundException
from ..models.classe import ClassePost, ClassePatch, Classe
from ..repositories.classe_repository import ClasseRepository


class ClasseService:
    def __init__(self, repository: ClasseRepository):
        self.repository = repository

    def __normalize_data(self, data: dict) -> dict:
        """Normalise les données : supprime les espaces, met en majuscules."""
        normalized = data.copy()

        if "nom" in normalized and isinstance(normalized["nom"], str):
            normalized["nom"] = normalized["nom"].strip().upper() or None

        if "niveau" in normalized and isinstance(normalized["niveau"], str):
            normalized["niveau"] = normalized["niveau"].strip().upper() or None

        return normalized

    def get_all(self, offset: int = 0, limit: int = 10) -> list[Classe]:
        return self.repository.get_all(offset, limit)

    def get_by_id(self, id: int) -> Classe:
        classe = self.repository.get_by_id(id)
        if not classe:
            raise NotFoundException("Classe introuvable")
        return classe

    def create(self, classe_data: ClassePost) -> Classe:
        classe_dict = classe_data.model_dump()
        normalized = self.__normalize_data(classe_dict)
        return self.repository.create(normalized)

    def patch(self, id: int, classe_data: ClassePatch) -> Classe:
        classe = self.repository.get_by_id(id)
        if not classe:
            raise NotFoundException("Classe introuvable")
        classe_dict = classe_data.model_dump(exclude_unset=True)
        normalized = self.__normalize_data(classe_dict)
        return self.repository.patch(classe, normalized)

    def delete(self, id: int) -> None:
        classe = self.repository.get_by_id(id)
        if not classe:
            raise NotFoundException("Classe introuvable")
        self.repository.delete(classe)

