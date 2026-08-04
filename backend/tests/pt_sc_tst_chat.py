from app.core.database import SessionLocal
from app.models.chat import Chat
from app.repositories.chat_repository import ChatRepo
from app.models.utilisateur import Utilisateur
from app.models.administrateur import Administrateur
from app.models.document_importe import DocumentImporte
db=SessionLocal()
repo=ChatRepo()

# chat1=Chat(question="Bonjour",reponse="je vais bien",id_utilisateur=14,id_admin=1)
# chat2=Chat(question="Bonjour",reponse="je vais bien",id_utilisateur=5,id_admin=2)
ch=Chat(question="Bonjour3",reponse="je vais bie3n",id_utilisateur=5,id_admin=2,id_document_importe=2)
repo.create(db,ch)
# repo.create(db,chat2)
# chats=repo.get_all(db)
# for c in chats:
#     print(c.question,c.reponse)

# ch=repo.get_by_id(db,2)
# print(ch.question,ch.reponse)
ch=Chat(question="Bonjour3",reponse="je vais bie3n",id_utilisateur=5,id_admin=2,id_document_importe=1)
repo.delete(db,3)