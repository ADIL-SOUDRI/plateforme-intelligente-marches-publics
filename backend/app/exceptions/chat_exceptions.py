from app.exceptions.base import AppException


class ChatNotFoundException(AppException):

    def __init__(self):
        super().__init__(
            message="Conversation introuvable.",
            status_code=404
        )