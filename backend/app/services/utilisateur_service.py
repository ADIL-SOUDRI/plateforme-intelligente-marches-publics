from sqlalchemy.orm import Session
from app.models.utilisateur import Utilisateur
from app.repositories.utilisateur_repository import UtilisateurRepo

class UtilisateurService:

    def __init__(self):
        self.repo=UtilisateurRepo()


    def creer_utilisateur(self,db:Session,utilisateur:Utilisateur):
        return self.repo.create(db,utilisateur)
    
    def obtenir_utilisateur(self,db:Session, id:int):
        return self.repo.get_by_id(db,id)

    
    def lister_utilisateurs(self, db: Session):
        return self.repo.get_all(db)
    
    def  modifier_utilisateur(self,db: Session,id:int, utilisateur:Utilisateur):
        return self.repo.update(db,id,utilisateur)
    
    def supprimer_utilisateur(self,db:Session, id:int):
        return self.repo.delete(db,id)