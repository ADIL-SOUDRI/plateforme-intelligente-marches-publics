from fastapi import FastAPI

from app.core.database import Base, engine
from app.models.utilisateur import Utilisateur
from app.models.document_importe import DocumentImporte
from app.models.document_reference import DocumentReference
# from app.models.conversation import Conversation
from app.models.chat import Chat
from app.models.administrateur import Administrateur
from app.controllers.utilisateur_controller import api as utilisateur_api
from app.controllers.administrateur_controller import api as administrateur_api
from app.controllers.document_importe_controller import api as document_importe_api
from app.controllers.document_reference_controller import api as document_reference_api
from app.controllers.chat_controller import api as chat_api
from app.exceptions.base import AppException
from app.handlers.exception_handler import app_exception_handler
from app.controllers.auth_controller import api as auth_api
app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(utilisateur_api)
app.include_router(administrateur_api)
app.include_router(document_importe_api)
app.include_router(document_reference_api)
app.include_router(chat_api)
app.add_exception_handler(AppException,app_exception_handler)
app.include_router(auth_api)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)