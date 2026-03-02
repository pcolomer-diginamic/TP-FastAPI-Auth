from sqlmodel import Session, create_engine, select
from .settings import settings
from ..models.user import User

#TP - Hash mot de passe
from passlib.context import CryptContext


# L'engine est créé une seule fois au démarrage de l'application
engine = create_engine(settings.CONNECTION_STRING, echo=True)


def get_session():
    
    with Session(engine) as session:

        """pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
        u_user = User(user_id="admin@fastapi.io", passwd=pwd_context.hash("testapi"), role="ADMIN")
        session.add(u_user)
        session.commit()"""

        """pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
        u_user = User(user_id="lambda@fastapi.io", passwd=pwd_context.hash("test"), role="USER")
        session.add(u_user)
        session.commit()   """
        
        yield session
