from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING


class ClasseBase(SQLModel):
    nom: str
    niveau: str
    capacite: int


class ClasseRead(ClasseBase):
    id: int


class ClassePost(ClasseBase):
    pass


class ClassePatch(SQLModel):
    nom: str | None = None
    niveau: str | None = None
    capacite: int | None = None


class Classe(ClasseBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
