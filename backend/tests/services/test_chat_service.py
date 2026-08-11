from app.core.database import SessionLocal
from app.models.chat import Chat
from app.services.chat_service import ChatService


db = SessionLocal()
service = ChatService()


# 1. Tester la création
chat = Chat(question="Qu'est-ce qu'un marché public ?",reponse="je vais bie3n",id_utilisateur=5,id_admin=2,id_document_importe=2)


chat = service.creer_chat(db, chat)

print("Chat créé :")
print(chat.id, chat.question)


# 2. Tester l'obtention par ID
chat = service.obtenir_chat(db, chat.id)

print("Chat obtenu :")
if chat:
    print(chat.id, chat.question)


# 3. Tester la liste
chats = service.lister_chats(db)

print("Liste des chats :")
for c in chats:
    print(c.id, c.question)


# 4. Tester la modification
nouveau_chat = Chat(question="Qu'est-ce qu'un marché public new ?",reponse=" marche public new",id_utilisateur=5,id_admin=2,id_document_importe=2)


chat = service.modifier_chat(
    db,
    chat.id,
    nouveau_chat
)

print("Chat modifié :")
if chat:
    print(chat.id, chat.question)


# 5. Tester la suppression
resultat = service.supprimer_chat(
    db,
    chat.id
)

print("Suppression :")
print(resultat)


db.close()