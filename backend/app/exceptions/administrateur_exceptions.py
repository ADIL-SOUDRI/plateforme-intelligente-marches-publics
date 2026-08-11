from app.exceptions.base import AppException


class AdministrateurNotFoundException(AppException):

    def __init__(self):
        super().__init__(
            message="Administrateur introuvable.",
            status_code=404
        )