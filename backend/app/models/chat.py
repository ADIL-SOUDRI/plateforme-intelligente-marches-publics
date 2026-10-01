from sqlalchemy import Column, ForeignKey,Integer,DateTime,String,func
from app.core.database import Base

class Chat(Base):
    __tablename__="chats"

    id=Column(Integer,primary_key=True, index=True,autoincrement=True)
    date_creation=Column(DateTime,server_default=func.now())
    question=Column(String)
    reponse=Column(String)
    id_utilisateur=Column(Integer ,ForeignKey("utilisateurs.id_utilisateur"))
    id_admin=Column(Integer,ForeignKey("administrateurs.id_admin"),nullable=True)
    id_document_importe=Column(Integer,ForeignKey("documents_importes.id"),nullable=True)
    # id_conversation = Column(
    #     Integer,
    #     ForeignKey("conversations.id"),
    #     nullable=False
    # )
    id_conversation=Column(Integer,nullable=True)