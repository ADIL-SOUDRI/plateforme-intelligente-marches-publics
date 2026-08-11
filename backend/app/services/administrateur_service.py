from sqlalchemy.orm import Session
from app.models.administrateur import Administrateur
from app.repositories.administrateur_repository import AdministrateurRepo

class AdministrateurService:

    def __init__(self):
        self.repo=AdministrateurRepo()

    def creer_administrateur(self,db:Session,administrateur:Administrateur):
        return self.repo.create(db,administrateur)
    
    def obtenir_administrateur(self,db:Session, id:int):
        return self.repo.get_by_id(db,id)
    
    def lister_administrateurs(self, db:Session):
        return self.repo.get_all(db)
        
    def  modifier_administrateur(self,db: Session,id:int, administrateur:Administrateur):
        return self.repo.update(db,id,administrateur)
    
    def supprimer_administrateur(self,db:Session, id:int):
        return self.repo.delete(db,id)