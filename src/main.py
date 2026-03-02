from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlmodel import SQLModel
from .conf.session import engine
from .exceptions import AppException
from .routes.classe_router import router_classe


#TP Vuln
#Logger et gestion exceptions HTTP 
from .services.logger_service import get_logger
#Authentification Basique
from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext
from .conf.session import get_session
#User model
from .models.user import User
from sqlmodel import select

from .services.authentication_service import basic_auth

@asynccontextmanager
async def lifespan(app: FastAPI, logg = Depends(get_logger)):
    #logg = Depends(get_logger)
    #logg.info("Application démarrée")
    # Création des tables au démarrage
    SQLModel.metadata.create_all(engine)
    #logg.info("DB initialisée")
    yield

app = FastAPI(lifespan=lifespan)

#TP - HTTP CSP
"""@app.middleware("http")
async def security_headers(request, call_next):
    response = await call_next(request)
    response.headers["Content-Security-Policy"] = "default-src 'self'; script-src 'self'; style-src 'self'"
    return response"""



@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException, logg = Depends(get_logger)) -> JSONResponse:
    #TP - Logging
    logg.warning(f"Code exception: {exc.status_code} - detail: {exc.detail}")
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})


app.include_router(router_classe)


@app.get("/health")
def health_check(_user=Depends(basic_auth)):
    return {"status": "ok"}

