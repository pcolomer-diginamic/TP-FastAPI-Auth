from sqlmodel import SQLModel, Field

class UserBase(SQLModel):
    user_id: str
    passwd: str
    role: security

class UserPost(UserBase):
    pass

class User(UserBase, table=True):
    user_id: str | None = Field(default=None, primary_key=True)
    passwd: str
    role: str