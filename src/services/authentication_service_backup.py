#TP Vuln
#Logger et gestion exceptions HTTP 
#import logging
from fastapi import HTTPException, status
from .logger_service import get_logger
#Authentification Basique
from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext
from ..conf.session import get_session
#User model
from ..models.user import User
from sqlmodel import select

#TP - Some sec param
security = HTTPBasic()

def basic_auth(session: Session = Depends(get_session), logg = Depends(get_logger), credentials: HTTPBasicCredentials = Depends(security)):
    #logg.info("###############################################################################")
    statement = select(User).where(User.user_id == credentials.username)
    ls_user = session.exec(statement)
    if ls_user:
        pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
        for user in ls_user:
            if pwd_context.verify(credentials.password,user.passwd):
                logg.info(f"Utilisaeur connecté: {credentials.username}")
                return (user)
        logg.error(f"Credentials invalides: password incorrect utilisateur {credentials.username} *** {credentials.password}")
    logg.error(f"Credentials invalides: identifiant utilisateur incorrect: {credentials.username} *** {credentials.password}")
    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Invalid authentication credentials TP2",
                        headers={"WWW-Authenticate": "Basic"},
                        )