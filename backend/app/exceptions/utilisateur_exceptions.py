from app.exceptions.base import AppException


class UtilisateurNotFoundException(AppException):

    def __init__(self):
        super().__init__(
            message="Utilisateur introuvable.",
            status_code=404
        )


class UtilisateurAlreadyExistsException(AppException):

    def __init__(self):
        super().__init__(
            message="Cet utilisateur existe déjà.",
            status_code=409
        )