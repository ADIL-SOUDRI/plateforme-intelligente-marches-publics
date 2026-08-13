from fastapi import APIRouter, Form
from fastapi import Depends
from app.core.dependencies import get_current_admin, get_current_user, get_current_utilisateur
from app.core.database import SessionLocal
from app.models.chat import Chat

from app.schemas.chat_schema import ChatCreate,ChatResponse

from app.services.chat_service import CHatService


api = APIRouter()
service = CHatService()

@api.post("/chats",response_model=ChatResponse)
def create_chat(id_utilisateur: int = Form(...),question: str = Form(...),id_admin: int | None = Form(None),id_document_importe: int | None = Form(None),current_user=Depends(get_current_user)):
    db = SessionLocal()

    try:
        
        chat_create = ChatCreate(
            question=question,
            id_admin=id_admin,
            id_document_importe=id_document_importe)
        chat = Chat(
            question=chat_create.question,
            reponse="Réponse temporaire",
            id_utilisateur=id_utilisateur,
            id_admin=chat_create.id_admin,
            id_document_importe=chat_create.id_document_importe)
        return service.creer_chat(db, chat)

    finally:
        db.close()


@api.get("/chats",response_model=list[ChatResponse])
def get_all_chats(current_user=Depends(get_current_user)):
    db = SessionLocal()

    try:
        return service.lister_chats(db)

    finally:
        db.close()
@api.get("/chatss")
def get_all_chats(
    current_user=Depends(get_current_user)
):
    return {
        "message": "Token valide",
        "user": current_user
    }

@api.get("/chats/{id}",response_model=ChatResponse)
def get_chat(id: int,current_user=Depends(get_current_user)):
    db = SessionLocal()

    try:
        return service.obtenir_chat(db, id)

    finally:
        db.close()

@api.delete("/chats/{id}")
def delete_chat(id: int,current_user=Depends(get_current_user)):
    db = SessionLocal()

    try:
        return service.supprimer_chat(db, id)

    finally:
        db.close()
@api.get(
    "/chats/utilisateur/{id_utilisateur}",
    response_model=list[ChatResponse]
)
def get_historique_utilisateur(id_utilisateur: int,current_utilisateur=Depends(get_current_utilisateur)):
    db = SessionLocal()

    try:
        return service.consulter_historique_utilisateur(db,id_utilisateur)

    finally:
        db.close()

@api.get(
    "/chats/admin/{id_admin}",
    response_model=list[ChatResponse]
)
def get_historique_admin(id_admin: int,current_admin=Depends(get_current_admin)):
    db = SessionLocal()

    try:
        return service.consulter_historique_admin(
db,id_admin)

    finally:
        db.close()