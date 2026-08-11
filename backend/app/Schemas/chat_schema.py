from datetime import datetime
from pydantic import BaseModel


class ChatCreate(BaseModel):
    question: str
    id_admin: int | None = None
    id_document_importe: int | None = None


class ChatResponse(BaseModel):
    id: int
    question: str
    reponse: str
    date_creation: datetime
    id_utilisateur: int
    id_admin: int | None
    id_document_importe: int | None

    class Config:
        from_attributes = True