from fastapi import APIRouter, Depends

from app.core.database import SessionLocal

from app.schemas.auth_schema import (
    LoginRequest,
    RegisterRequest,
    TokenResponse
)

from app.services.auth_service import AuthService
from app.core.dependencies import get_current_admin, get_current_user, get_current_utilisateur


api = APIRouter()

service = AuthService()


@api.post(
    "/auth/login",
    response_model=TokenResponse
)
def login(data: LoginRequest):

    db = SessionLocal()

    try:

        return service.login(
            db,
            data.email,
            data.mot_de_passe,
            data.role
        )

    finally:
        db.close()

@api.post("/auth/register")
def register(data: RegisterRequest):

    db = SessionLocal()

    try:

        return service.register(
            db,
            data.nom,
            data.prenom,
            data.email,
            data.mot_de_passe
        )

    finally:
        db.close()

# @api.get("/test-auth")
# def test_auth(
#     current_user=Depends(get_current_user)
# ):
#     return {
#         "message": "Token valide",
#         "user": current_user
#     }

# @api.get("/test-utilisateur")

# def test_utilisateur(
#     current_user=Depends(get_current_utilisateur)
# ):
#     return {
#         "message": "Accès utilisateur autorisé",
#         "id": current_user["sub"],
#         "role": current_user["role"]
#     }

# @api.get("/test-admin")
# def test_admin(
#     current_admin=Depends(get_current_admin)
# ):
#     return {
#         "message": "Accès administrateur autorisé",
#         "id": current_admin["sub"],
#         "role": current_admin["role"]
#     }