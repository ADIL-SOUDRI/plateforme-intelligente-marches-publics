from app.core.database import SessionLocal

from app.models.chat import Chat
from app.repositories.chat_repository import ChatRepo

from app.models.utilisateur import Utilisateur
from app.models.administrateur import Administrateur
from app.models.document_importe import DocumentImporte

db = SessionLocal()
repo = ChatRepo()


chat1 = Chat(
    question="Bonjour",
    reponse="Bonjour, comment puis-je vous aider ?",
    id_utilisateur=1,
    id_admin=1,
    id_document_importe=1
)


chat2 = Chat(
    question="Qu'est-ce qu'un CPS ?",
    reponse="Le CPS est le Cahier des Prescriptions Spéciales.",
    id_utilisateur=2,
    id_admin=1,
    id_document_importe=2
)


chat3 = Chat(
    question="Quel est le délai du marché ?",
    reponse="Le délai est indiqué dans le CPS.",
    id_utilisateur=3,
    id_admin=2,
    id_document_importe=3
)


chat4 = Chat(
    question="Qu'est-ce qu'un décret ?",
    reponse="Un décret est un texte réglementaire.",
    id_utilisateur=4,
    id_admin=2,
    id_document_importe=4
)


chat5 = Chat(
    question="Comment consulter les documents ?",
    reponse="Vous pouvez consulter les documents depuis la plateforme.",
    id_utilisateur=5,
    id_admin=1,
    id_document_importe=5
)


chat6 = Chat(
    question="Comment importer un document ?",
    reponse="Vous pouvez importer un document depuis votre espace.",
    id_utilisateur=5,
    id_admin=1,
    id_document_importe=4
)


repo.create(db, chat1)
repo.create(db, chat2)
repo.create(db, chat3)
repo.create(db, chat4)
repo.create(db, chat5)
repo.create(db, chat6)


chats = repo.get_all(db)


print("Liste des conversations :")


for chat in chats:
    print(
        chat.id,
        chat.question,
        chat.reponse,
        chat.id_utilisateur,
        chat.id_admin,
        chat.id_document_importe
    )


chat = repo.get_by_id(db, 3)


print("\nChat avec ID 3 :")


if chat:
    print(
        chat.id,
        chat.question,
        chat.reponse,
        chat.id_utilisateur,
        chat.id_admin,
        chat.id_document_importe
    )


chat_modifie = Chat(
    question="Quel est le délai du marché public ?",
    reponse="Le délai est indiqué dans le CPS du marché public.",
    id_utilisateur=3,
    id_admin=2,
    id_document_importe=3
)


chat = repo.update(db, 3, chat_modifie)


print("\nChat modifié :")


if chat:
    print(
        chat.id,
        chat.question,
        chat.reponse,
        chat.id_utilisateur,
        chat.id_admin,
        chat.id_document_importe
    )


chat = repo.get_by_id(db, 3)


print("\nVérification après modification :")


if chat:
    print(
        chat.id,
        chat.question,
        chat.reponse,
        chat.id_utilisateur,
        chat.id_admin,
        chat.id_document_importe
    )


resultat = repo.delete(db, 6)


print("\nChat supprimé :")
print(resultat)


chat = repo.get_by_id(db, 6)


print("\nVérification après suppression :")


if chat:
    print(
        chat.id,
        chat.question,
        chat.reponse,
        chat.id_utilisateur,
        chat.id_admin,
        chat.id_document_importe
    )
else:
    print("Chat introuvable")


chats = repo.get_all(db)


print("\nListe finale :")


for chat in chats:
    print(
        chat.id,
        chat.question,
        chat.reponse,
        chat.id_utilisateur,
        chat.id_admin,
        chat.id_document_importe
    )


db.close()