from fastapi import APIRouter

from app.services.administrateur_service import AdministrateurService
from app.core.database import SessionLocal
from app.models.administrateur import Administrateur
from app.schemas.administrateur_schema import AdministrateurCreate,AdministrateurResponse,AdministrateurUpdate

api = APIRouter()
service = AdministrateurService()
db = SessionLocal()

@api.get("/administrateurs",response_model=list[AdministrateurResponse])
def get_all():
    try:
        return service.lister_administrateurs(db)
    finally:
        db.close()


@api.get(
    "/administrateurs/{id}",response_model=AdministrateurResponse)
def get_by_id(id: int):
    try:
        return service.obtenir_administrateur(db, id)
    finally:
        db.close()

@api.post("/administrateurs",response_model=AdministrateurResponse)
def create(admin: AdministrateurCreate):
    db = SessionLocal()
    try:
        administrateur = Administrateur(
            nom=admin.nom,
            prenom=admin.prenom,
            email=admin.email,
            mot_de_passe=admin.mot_de_passe)
        return service.creer_administrateur(db, administrateur)

    finally:
        db.close()

@api.put("/administrateurs/{id}",response_model=AdministrateurResponse)
def update(id: int, admin: AdministrateurUpdate):
    db = SessionLocal()
    try:
        administrateur = Administrateur(
            nom=admin.nom,
            prenom=admin.prenom,
            email=admin.email,
            mot_de_passe=admin.mot_de_passe)
        return service.modifier_administrateur(
db,id,administrateur)

    finally:
        db.close()

@api.delete("/administrateurs/{id}")
def delete(id: int):
    db = SessionLocal()
    try:
        return service.supprimer_administrateur(db, id)
    finally:
        db.close()