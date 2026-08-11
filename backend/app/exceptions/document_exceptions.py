from app.exceptions.base import AppException


class DocumentImporteNotFoundException(AppException):

    def __init__(self):
        super().__init__(
            message="Document importé introuvable.",
            status_code=404
        )


class DocumentReferenceNotFoundException(AppException):

    def __init__(self):
        super().__init__(
            message="Document de référence introuvable.",
            status_code=404
        )


class DocumentAlreadyExistsException(AppException):

    def __init__(self):
        super().__init__(
            message="Ce document existe déjà.",
            status_code=409
        )