from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..conf.session import get_session
from ..models.classe import ClasseRead, ClassePost, ClassePatch
from ..services.classe_service import ClasseService
from ..repositories.classe_repository import ClasseRepository

#TP - Authentification
from ..services.authentication_service import basic_auth
#import logging
from fastapi import HTTPException, status
from ..services.logger_service import get_logger

########################
# DEPENDENCY INJECTION #
########################

def get_classe_service(session: Session = Depends(get_session)) -> ClasseService:
    repository = ClasseRepository(session)
    return ClasseService(repository)

######################
# CLASSES ENDPOINTS  #
######################

router_classe = APIRouter(prefix="/classes", tags=["classes"])


@router_classe.get("/", response_model=list[ClasseRead], status_code=200)
def get_all(offset: int = 0, limit: int = 10, service: ClasseService = Depends(get_classe_service), _user=Depends(basic_auth)):
    if _user.role in ("USER","ADMIN"):
        return service.get_all(offset, limit)
    raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Accès refusé",
                    headers={"WWW-Authenticate": "Basic"},
                    )

@router_classe.get("/{id}", response_model=ClasseRead, status_code=200)
def get_by_id(id: int, service: ClasseService = Depends(get_classe_service), _user=Depends(basic_auth)):
    if _user.role in ("USER","ADMIN"):
        return service.get_by_id(id)
    raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Accès refusé",
                    headers={"WWW-Authenticate": "Basic"},
                    )

@router_classe.post("/", response_model=ClasseRead, status_code=201)
def create(classe_data: ClassePost, service: ClasseService = Depends(get_classe_service), _user=Depends(basic_auth)):
    if _user.role == "ADMIN":
        return service.create(classe_data)
    raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Accès refusé",
                    headers={"WWW-Authenticate": "Basic"},
                    )

@router_classe.patch("/{id}", response_model=ClasseRead, status_code=200)
def patch(id: int, classe_data: ClassePatch, service: ClasseService = Depends(get_classe_service), _user=Depends(basic_auth)):
    if _user.role == "ADMIN":
        return service.patch(id, classe_data)
    raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Accès refusé",
                headers={"WWW-Authenticate": "Basic"},
                )


@router_classe.delete("/{id}", status_code=204)
def delete(id: int, service: ClasseService = Depends(get_classe_service), _user=Depends(basic_auth)):
    if _user.role == "ADMIN":
            return service.delete(id)
    raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Accès refusé",
                headers={"WWW-Authenticate": "Basic"},
                )    


