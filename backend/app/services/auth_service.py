from sqlalchemy.orm import Session

from app.repositories.utilisateur_repository import UtilisateurRepo
from app.repositories.administrateur_repository import AdministrateurRepo

from app.core.security import (
    verify_password,
    create_access_token
)

from app.exceptions.auth_exceptions import InvalidCredentialsException



class AuthService:

    def __init__(self):

        self.utilisateur_repo = UtilisateurRepo()
        self.administrateur_repo = AdministrateurRepo()

    def login(
        self,
        db: Session,
        email: str,
        mot_de_passe: str,
        role: str
    ):

        utilisateur = self.utilisateur_repo.get_by_email(
            db,
            email
        )
        if role == "utilisateur":

            if utilisateur:

                if not verify_password(
                    mot_de_passe,
                    utilisateur.mot_de_passe
                ):
                    raise InvalidCredentialsException()

                token = create_access_token({
                    "sub": str(utilisateur.id_utilisateur),
                    "role": "utilisateur"
                })

                return {
                    "access_token": token,
                    "token_type": "bearer"
                }
        elif role=="administrateur":

            administrateur = self.administrateur_repo.get_by_email(
                db,
                email
            )

            if administrateur:

                if not verify_password(
                    mot_de_passe,
                    administrateur.mot_de_passe
                ):
                    raise InvalidCredentialsException()

                token = create_access_token({
                    "sub": str(administrateur.id_admin),
                    "role": "administrateur"
                })

                return {
                    "access_token": token,
                    "token_type": "bearer"
                }

        else:
            raise InvalidCredentialsException()