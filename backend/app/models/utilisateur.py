from sqlalchemy import Column,Integer
from app.core.database import Base
from app.models.personne import Personne

class Utilisateur(Personne):
    __tablename__="utilisateurs"
    id_utilisateur=Column(Integer,primary_key=True,index=True,autoincrement=True)