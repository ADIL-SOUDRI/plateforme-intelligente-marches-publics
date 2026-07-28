from sqlalchemy import Column,Integer
from app.core.database import Base
from app.models.personne import Personne

class Administrateur(Personne):
    __tablename__="administrateurs"
    id_admin=Column(Integer,primary_key=True,index=True,autoincrement=True)