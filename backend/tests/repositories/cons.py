from app.core.database import SessionLocal

from app.models.chat import Chat
from app.models.utilisateur import Utilisateur
from app.models.administrateur import Administrateur
from app.models.document_importe import DocumentImporte
from app.models.conversation import Conversation

from app.repositories.chat_repository import ChatRepo


db = SessionLocal()
repo = ChatRepo()

try:

    # =====================================================
    # 1. CREATION
    # =====================================================

    chat = Chat(
        question="Qu'est-ce qu'un marché public ?",
        reponse="Réponse de test",
        id_utilisateur=5,
        id_conversation=10
    )

    chat = repo.create(db, chat)

    print("\n" + "=" * 60)
    print("CHAT CREE")
    print("=" * 60)

    print("ID :", chat.id)
    print("Question :", chat.question)
    print("Conversation :", chat.id_conversation)


    # =====================================================
    # 2. OBTENIR PAR ID
    # =====================================================

    chat_obtenu = repo.get_by_id(db, chat.id)

    print("\n" + "=" * 60)
    print("CHAT OBTENU")
    print("=" * 60)

    if chat_obtenu:
        print("ID :", chat_obtenu.id)
        print("Question :", chat_obtenu.question)
    else:
        print("Chat introuvable")


    # =====================================================
    # 3. LISTER LES CHATS
    # =====================================================

    chats = repo.get_all(db)

    print("\n" + "=" * 60)
    print("LISTE DES CHATS")
    print("=" * 60)

    for c in chats:
        print(
            "ID :", c.id,
            "| Question :", c.question,
            "| Conversation :", c.id_conversation
        )


    # =====================================================
    # 4. MODIFICATION
    # =====================================================

    nouveau_chat = Chat(
    question="Question modifiée",
    reponse="Réponse modifiée",
    id_utilisateur=5,
    id_conversation=10
)

    chat_modifie = repo.update(
        db,
        chat_obtenu.id,
        nouveau_chat
    )
    print("\n" + "=" * 60)
    print("CHAT MODIFIE")
    print("=" * 60)

    if chat_modifie:
        print("ID :", chat_modifie.id)
        print("Question :", chat_modifie.question)
        print("Réponse :", chat_modifie.reponse)
    # =====================================================
    # 5. SUPPRESSION
    # =====================================================

    resultat = repo.delete(db, chat_modifie.id)

    print("\n" + "=" * 60)
    print("SUPPRESSION")
    print("=" * 60)

    print("Résultat :", resultat)


finally:

    db.close()