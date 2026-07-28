from sqlalchemy import Column,Integer,String,Float,Enum
from app.core.database import Base
from app.enums.type_document import TypeDocument

class Document(Base):
    __abstract__=True

    id = Column(Integer , primary_key=True , index=True,autoincrement=True)
    titre = Column(String)
    nom_fichier=Column(String)
    type=Column(Enum(TypeDocument),nullable=False) #enum(TypeDocument ) ou TypeDocument direct ?
    taille=Column(Float)