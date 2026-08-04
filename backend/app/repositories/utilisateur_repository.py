from sqlalchemy.orm import Session
from app.models.utilisateur import Utilisateur

class UtilisateurRepo:

    def create(self , db:Session , user:Utilisateur):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_by_id(self , db:Session, id:int):
         return db.query(Utilisateur).filter(Utilisateur.id_utilisateur==id).first()
    
    def get_all(self,db:Session):
        return db.query(Utilisateur).all()
    
    def delete(self, db:Session,id:int):
        user = self.get_by_id(db, id)
        if user:
            db.delete(user)
            db.commit()
            return "La suppression bien effectuée"
        return "Utilisateur introuvable."
    
    def update(self,db:Session,id:int,new_utilisateur=Utilisateur):
        user = self.get_by_id(db, id)
        if user:
            user.nom=new_utilisateur.nom
            user.prenom=new_utilisateur.prenom
            user.email=new_utilisateur.email
            user.mot_de_passe=new_utilisateur.mot_de_passe
            db.commit()
            db.refresh(user)
            return user
        else:
            return"l'utilisateur n'existe pas"