from fastapi import APIRouter
from app.services.utilisateur_service import UtilisateurService
from app.core.database import SessionLocal
from app.models.utilisateur import Utilisateur
from app.schemas.utilisateur_schema import UtilisateurCreate,UtilisateurResponse,UtilisateurUpdate


api = APIRouter()
service = UtilisateurService()
db = SessionLocal()

@api.get("/users",response_model=list[UtilisateurResponse])
def get_all():
    try:
        return service.lister_utilisateurs(db)
    finally:
        db.close()

@api.get("/users/{id}", response_model=UtilisateurResponse)
def get_by_id(id:int):
    try:
        return service.obtenir_utilisateur(db, id)
    finally:
        db.close()

@api.post("/users",response_model=UtilisateurResponse)
def create(user: UtilisateurCreate):
    db = SessionLocal()
    try:
        utilisateur = Utilisateur(
            nom=user.nom,
            prenom=user.prenom,
            email=user.email,
            mot_de_passe=user.mot_de_passe
            )

        return service.creer_utilisateur(db, utilisateur)

    finally:
        db.close()

@api.put("/users/{id}", response_model=UtilisateurResponse)
def update(id: int, user: UtilisateurUpdate):
    try:
        utilisateur = Utilisateur(
                    nom=user.nom,
                    prenom=user.prenom,
                    email=user.email,
                    mot_de_passe=user.mot_de_passe
)
        return service.modifier_utilisateur(db, id, utilisateur)
    finally:
        db.close()

@api.delete("/users/{id}")
def delete(id: int):
    try:
        return service.supprimer_utilisateur(db, id)
    finally:
        db.close()