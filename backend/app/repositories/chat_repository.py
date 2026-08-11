from sqlalchemy.orm import Session
from app.models.chat import Chat

class ChatRepo:
    def get_all(self,db:Session):
        return db.query(Chat).all()

    def get_by_id(self ,db:Session,id:int):
        return db.query(Chat).filter(Chat.id==id).first()

    def create(self,db:Session,chat:Chat):
        db.add(chat)
        db.commit()
        db.refresh(chat)
        return chat
    def delete(self,db:Session,id:int):
        chat=self.get_by_id(db,id)
        if chat:
            db.delete(chat)
            db.commit()
           # db.refresh()
            return chat
        


    def update(self,db:Session,id:int,new_chat:Chat):
        chat=self.get_by_id(db,id)

        if chat:
            chat.question=new_chat.question
            db.commit()
            db.refresh(chat)
            return chat
        
    def get_by_user(self,db: Session,id_utilisateur: int):
        return db.query(Chat).filter(Chat.id_utilisateur == id_utilisateur).all()
    def get_by_admin(self,db: Session,id_admin: int):
        return db.query(Chat).filter(Chat.id_admin == id_admin).all()
