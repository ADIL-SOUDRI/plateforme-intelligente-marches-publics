from fastapi import FastAPI

from app.core.database import Base, engine

from app.models.utilisateur import Utilisateur
from app.models.document_importe import DocumentImporte
from app.models.document_reference import DocumentReference
from app.models.chat import Chat
from app.models.administrateur import Administrateur

app = FastAPI()

Base.metadata.create_all(bind=engine)