from fastapi import APIRouter

from app.core.database import SessionLocal

from app.schemas.auth_schema import (
    LoginRequest,
    TokenResponse
)

from app.services.auth_service import AuthService


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