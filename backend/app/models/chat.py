from sqlalchemy import Column, ForeignKey,Integer,DateTime,String,func
from app.core.database import Base

class Chat(Base):
    __tablename__="chats"

    id=Column(Integer,primary_key=True, index=True,autoincrement=True)
    date_creation=Column(DateTime,server_default=func.now())
    question=Column(String)
    reponse=Column(String)
    utilisateur_id=Column(Integer ,ForeignKey("utilisateurs.id_utilisateur"))
    admin_id=Column(Integer,ForeignKey("administrateurs.id_admin"))
