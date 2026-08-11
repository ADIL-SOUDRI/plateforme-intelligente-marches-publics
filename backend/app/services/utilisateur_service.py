from sqlalchemy.orm import Session
from app.models.utilisateur import Utilisateur
from app.repositories.utilisateur_repository import UtilisateurRepo
from app.exceptions.utilisateur_exceptions import UtilisateurAlreadyExistsException, UtilisateurNotFoundException

class UtilisateurService:

    def __init__(self):
        self.repo=UtilisateurRepo()


    def creer_utilisateur(self,db:Session,utilisateur:Utilisateur):
        user_existe = self.repo.get_by_email(db,utilisateur.email)

        if user_existe:
            raise UtilisateurAlreadyExistsException()

        return self.repo.create(db, utilisateur)
    
    def obtenir_utilisateur(self,db:Session, id:int):
        utilisateur = self.repo.get_by_id(db, id)

        if not utilisateur:
            raise UtilisateurNotFoundException()

        return utilisateur

    
    def lister_utilisateurs(self, db: Session):
        return self.repo.get_all(db)
    
    def  modifier_utilisateur(self,db: Session,id:int, utilisateur:Utilisateur):
        user_existe = self.repo.get_by_id(db, id)

        if not user_existe:
            raise UtilisateurNotFoundException()

        return self.repo.update(db,id,utilisateur)
    
    def supprimer_utilisateur(self,db:Session, id:int):
        utilisateur = self.repo.get_by_id(db, id)

        if not utilisateur:
            raise UtilisateurNotFoundException()

        return self.repo.delete(db, id)