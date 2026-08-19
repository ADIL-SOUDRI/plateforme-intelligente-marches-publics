from fastapi import APIRouter, Form
from fastapi import Depends
from app.core.dependencies import get_current_admin, get_current_user, get_current_utilisateur
from app.core.database import SessionLocal
from app.models.chat import Chat

from app.schemas.chat_schema import ChatCreate,ChatResponse

from app.services.chat_service import CHatService
from app.exceptions.auth_exceptions import AccessDeniedException
from app.services.rag.rag_service import RAGService


api = APIRouter()
service = CHatService()
rag_service=RAGService()

@api.post("/chats",response_model=ChatResponse)
def create_chat(id_utilisateur: int = Form(...),question: str = Form(...),id_admin: int | None = Form(None),id_document_importe: int | None = Form(None),current_user=Depends(get_current_user)):
    db = SessionLocal()

    try:
        if current_user["role"] == "utilisateur":

            if id_utilisateur != int(current_user["sub"]):
                raise AccessDeniedException()
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
# @api.get("/chatss")
# def get_all_chats(
#     current_user=Depends(get_current_user)
# ):
#     return {
#         "message": "Token valide",
#         "user": current_user
#     }

@api.get("/chats/{id}",response_model=ChatResponse)
def get_chat(id: int,current_user=Depends(get_current_user)):
    db = SessionLocal()

    try:
        chat = service.obtenir_chat(db, id)
        if current_user["role"] == "utilisateur":

            if chat.id_utilisateur != int(current_user["sub"]):
                raise AccessDeniedException()

        return chat

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
        if id_utilisateur != int(current_utilisateur["sub"]):
            raise AccessDeniedException()
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
        if id_admin != int(current_admin["sub"]):
            raise AccessDeniedException()
        return service.consulter_historique_admin(db,id_admin)

    finally:
        db.close()

@api.post("/chats",response_model=ChatResponse)
def poser_question(request:ChatCreate,current_user=Depends(get_current_user)):
    db = SessionLocal()
    resultat = rag_service.repondre(
        question=request.question,
        # document_id=request.document_id
    )
    chat = service.creer_chat(
        db=db,
        question=request.question,
        reponse=resultat["reponse"],
        id_utilisateur=int(current_user["sub"])
    )
    return chat
@api.post("/chatss")
def poser_question(
    request: ChatCreate,
    current_user=Depends(get_current_user)
):
    resultat = rag_service.repondre(
        question=request.question
    )

    return {
        "question": resultat["question"],
        "reponse": resultat["reponse"],
        "sources": resultat["sources"]
    }
@api.post("/chatsss", response_model=ChatResponse)
def poser_question(
    request: ChatCreate,
    current_user=Depends(get_current_user)
):
    db=SessionLocal()
    id_utilisateur = int(current_user["sub"])

    resultat = {
    "question": request.question,
    "reponse": "Réponse de test du système RAG.",
    "sources": []
}

    chat = Chat(
        question=resultat["question"],
        reponse=resultat["reponse"],
        id_utilisateur=id_utilisateur
    )

    db.add(chat)
    db.commit()
    db.refresh(chat)

    return chat

# @api.post("/chats", response_model=ChatResponse)
# def poser_question(
#     request: str,
#     current_user=Depends(get_current_user)
# ):
#     db = SessionLocal()

#     resultat = rag_service.repondre(
#         question=request
#     )
#     chat_shema=ChatCreate(
#         question=request
#     )

#     chat = Chat(
#         question=chat_shema.question,
#         reponse=resultat["reponse"],
#         id_utilisateur=int(current_user["sub"]),
#         id_admin=None,
#         id_document_importe=None
#     )

#     chat = service.creer_chat(
#         db=db,
#         chat=chat
#     )

#     return chat

@api.post("/chats-s",response_model=ChatResponse)
def poser_question(question:str,current_user=Depends(get_current_user)):
    db = SessionLocal()
    resultat = rag_service.repondre(
        question=question,
        # document_id=request.document_id
    )
    id_utilisateur = int(current_user["sub"])
    chat_create=ChatCreate(
        question=question
    )
    chat=Chat(
        question=chat_create.question,
        reponse=resultat["reponse"],
        id_utilisateur=id_utilisateur
    )
    chat1 = service.creer_chat(
        db,chat
    )
    return chat1
@api.post("/chats-ss", response_model=ChatResponse)
def poser_question(
    request: ChatCreate,
    current_user=Depends(get_current_user)
):
    db = SessionLocal()

    resultat = rag_service.repondre(
        question=request.question
    )

    id_utilisateur = int(current_user["sub"])

    chat = Chat(
        question=request.question,
        reponse=resultat["reponse"],
        id_utilisateur=id_utilisateur
    )

    chat = service.creer_chat(
        db=db,
        chat=chat
    )

    return chat