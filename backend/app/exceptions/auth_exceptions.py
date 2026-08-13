from app.exceptions.base import AppException


class InvalidCredentialsException(AppException):

    def __init__(self):
        super().__init__(
            message="Email, mot de passe ou rôle incorrect.",
            status_code=401
        )

class InvalidTokenException(AppException):

    def __init__(self):
        super().__init__(
            message="Token invalide ou expiré.",
            status_code=401
        )


class AccessDeniedException(AppException):

    def __init__(self):
        super().__init__(
            message="Accès refusé. Vous n'avez pas les autorisations nécessaires.",
            status_code=403
        )
