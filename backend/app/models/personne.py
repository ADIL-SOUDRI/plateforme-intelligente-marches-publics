from sqlalchemy import Column,Integer,String
from app.core.database import Base

class Personne(Base):
    __abstract__ = True

    nom = Column(String )
    prenom = Column(String )
    email = Column(String )
    mot_de_passe = Column(String )
