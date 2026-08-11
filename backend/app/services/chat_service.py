from sqlalchemy.orm import Session
from app.models.chat import Chat
from app.repositories.chat_repository import ChatRepo
from app.exceptions.chat_exceptions import ChatNotFoundException

class CHatService:

    def __init__(self):
        self.repo=ChatRepo()

    def creer_chat(self,db:Session,chat:Chat):
        return self.repo.create(db,chat)
    
    def obtenir_chat(self,db:Session, id:int):
        chat = self.repo.get_by_id(db, id)

        if not chat:
            raise ChatNotFoundException()

        return chat
    
    def lister_chats(self, db: Session):
        return self.repo.get_all(db)
            
    def  modifier_chat(self,db: Session,id:int,chat:ChatRepo):
        chat_existe = self.repo.get_by_id(db, id)

        if not chat_existe:
            raise ChatNotFoundException()

        return self.repo.update(db,id,chat)
    
    def supprimer_chat(self,db:Session, id:int):
        chat = self.repo.get_by_id(db, id)

        if not chat:
            raise ChatNotFoundException()

        return self.repo.delete(db, id)
    
    def consulter_historique_utilisateur(self,db:Session, id_utilisateur: int):
        return self.repo.get_by_user(db, id_utilisateur)
    
    def consulter_historique_admin(self, db:Session,id_admin: int):
        return self.repo.get_by_admin(db, id_admin)