from fastapi import APIRouter, Depends

from app.services.administrateur_service import AdministrateurService
from app.core.database import SessionLocal
from app.models.administrateur import Administrateur
from app.schemas.administrateur_schema import AdministrateurCreate,AdministrateurResponse,AdministrateurUpdate
from app.core.security import hash_password
from app.core.dependencies import get_current_admin
from app.exceptions.auth_exceptions import AccessDeniedException

api = APIRouter()
service = AdministrateurService()
db = SessionLocal()

@api.get("/administrateurs",response_model=list[AdministrateurResponse])
def get_all(current_admin=Depends(get_current_admin)):
    try:
        return service.lister_administrateurs(db)
    finally:
        db.close()

@api.get("/admin/me")
def get_current_admin_profile(
    current_admin=Depends(get_current_admin)
):
    db = SessionLocal()

    try:
        id_admin = int(current_admin["sub"])

        admin = service.obtenir_administrateur(
            db,
            id_admin
        )

        return admin

    finally:
        db.close()
@api.get(
    "/administrateurs/{id}",response_model=AdministrateurResponse)
def get_by_id(id: int,current_admin=Depends(get_current_admin)):
    try:
        return service.obtenir_administrateur(db, id)
    finally:
        db.close()

@api.post("/administrateurs",response_model=AdministrateurResponse)
def create(admin: AdministrateurCreate,current_admin=Depends(get_current_admin)):
    db = SessionLocal()
    try:
        administrateur = Administrateur(
            nom=admin.nom,
            prenom=admin.prenom,
            email=admin.email,
            mot_de_passe=hash_password(admin.mot_de_passe))
        return service.creer_administrateur(db, administrateur)

    finally:
        db.close()

@api.put("/administrateurs/{id}",response_model=AdministrateurResponse)
def update(id: int, admin: AdministrateurUpdate,current_admin=Depends(get_current_admin)):
    db = SessionLocal()
    try:
        if id != int(current_admin["sub"]):
            raise AccessDeniedException()
        administrateur = Administrateur(
            nom=admin.nom,
            prenom=admin.prenom,
            email=admin.email,
            mot_de_passe=hash_password(admin.mot_de_passe))
        return service.modifier_administrateur(
db,id,administrateur)

    finally:
        db.close()

@api.delete("/administrateurs/{id}")
def delete(id: int,current_admin=Depends(get_current_admin)):
    db = SessionLocal()
    try:
        if id != int(current_admin["sub"]):
            raise AccessDeniedException()
        return service.supprimer_administrateur(db, id)
    finally:
        db.close()