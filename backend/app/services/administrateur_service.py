from sqlalchemy.orm import Session
from app.models.administrateur import Administrateur
from app.repositories.administrateur_repository import AdministrateurRepo
from app.exceptions.administrateur_exceptions import AdministrateurNotFoundException

class AdministrateurService:

    def __init__(self):
        self.repo=AdministrateurRepo()

    def creer_administrateur(self,db:Session,administrateur:Administrateur):
        return self.repo.create(db,administrateur)
    
    def obtenir_administrateur(self,db:Session, id:int):
        administrateur = self.repo.get_by_id(db,id)

        if not administrateur:
            raise AdministrateurNotFoundException()

        return administrateur
    
    def lister_administrateurs(self, db:Session):
        return self.repo.get_all(db)
        
    def  modifier_administrateur(self,db: Session,id:int, administrateur:Administrateur):
        administrateur_existant = self.repo.get_by_id(db,id)
        if not administrateur_existant:
            raise AdministrateurNotFoundException()

        return self.repo.update(db, id, administrateur)
    
    def supprimer_administrateur(self,db:Session, id:int):
        administrateur = self.repo.get_by_id(db,id)
        if not administrateur:
            raise AdministrateurNotFoundException()

        return self.repo.delete(db, id)