from fastapi import APIRouter, Depends
from app.services.utilisateur_service import UtilisateurService
from app.core.database import SessionLocal
from app.models.utilisateur import Utilisateur
from app.schemas.utilisateur_schema import UtilisateurCreate,UtilisateurResponse,UtilisateurUpdate
from app.core.dependencies import get_current_user, get_current_utilisateur , get_current_admin
from app.core.security import hash_password

api = APIRouter()
service = UtilisateurService()
db = SessionLocal()

@api.get("/users",response_model=list[UtilisateurResponse])
def get_all( current_admin=Depends(get_current_admin)):
    try:
        return service.lister_utilisateurs(db)
    finally:
        db.close()
@api.get("/users/me", response_model=UtilisateurResponse)
def get_current_user_info(
    current_user=Depends(get_current_utilisateur)
):
    db = SessionLocal()

    try:
        utilisateur = service.obtenir_utilisateur(
            db,
            int(current_user["sub"])
        )

        return utilisateur

    finally:
        db.close()
@api.get("/users/{id}", response_model=UtilisateurResponse)
def get_by_id(id:int,current_admin=Depends(get_current_admin)):
    try:
        return service.obtenir_utilisateur(db, id)
    finally:
        db.close()

@api.post("/users",response_model=UtilisateurResponse)
def create( user: UtilisateurCreate,current_admin=Depends(get_current_admin)):
    db = SessionLocal()
    try:
        utilisateur = Utilisateur(
            nom=user.nom,
            prenom=user.prenom,
            email=user.email,
            mot_de_passe=hash_password(user.mot_de_passe)
            )

        return service.creer_utilisateur(db, utilisateur)

    finally:
        db.close()

@api.put("/users/{id}", response_model=UtilisateurResponse)
def update(id: int, user: UtilisateurUpdate,current_admin=Depends(get_current_admin)):
    try:
        utilisateur = Utilisateur(
                    nom=user.nom,
                    prenom=user.prenom,
                    email=user.email,
                    mot_de_passe=hash_password(user.mot_de_passe)
)
        return service.modifier_utilisateur(db, id, utilisateur)
    finally:
        db.close()


@api.delete("/users/{id}",response_model=UtilisateurResponse)
def delete(id: int,current_admin=Depends(get_current_admin)):
    try:
        return service.supprimer_utilisateur(db, id)
    finally:
        db.close()

# @api.get("/test-utilisateur")
# def test_utilisateur(
#     current_user=Depends(get_current_utilisateur)
# ):
#     return {
#         "message": "Accès utilisateur autorisé",
#         "id_utilisateur": current_user["sub"],
#         "role": current_user["role"]
#     }

# @api.get("/test-utilisateur")
# def test_utilisateur(
#     current_user=Depends(get_current_user)
# ):
#     return {
#         "message": "Accès autorisé",
#         "id": current_user["sub"],
#         "role": current_user["role"]
#     }