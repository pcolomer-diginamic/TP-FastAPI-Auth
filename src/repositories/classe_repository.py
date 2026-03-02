from sqlmodel import Session, select
from ..models.classe import Classe


class ClasseRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self, offset: int = 0, limit: int = 10) -> list[Classe]:
        statement = select(Classe).offset(offset).limit(limit)
        return self.session.exec(statement).all()

    def get_by_id(self, id: int) -> Classe | None:
        return self.session.get(Classe, id)

    def create(self, classe_data: dict) -> Classe:
        classe = Classe(**classe_data)
        self.session.add(classe)
        self.session.commit()
        self.session.refresh(classe)
        return classe

    def patch(self, classe: Classe, classe_data: dict) -> Classe:
        for field, value in classe_data.items():
            setattr(classe, field, value)
        self.session.commit()
        self.session.refresh(classe)
        return classe

    def delete(self, classe: Classe) -> None:
        self.session.delete(classe)
        self.session.commit()
