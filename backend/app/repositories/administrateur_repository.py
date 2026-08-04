from sqlalchemy.orm import Session
from app.models.administrateur import Administrateur

class AdministrateurRepo:

    def create(self , db:Session , admin:Administrateur):
        db.add(admin)
        db.commit()
        db.refresh(admin)
        return admin

    def get_by_id(self , db:Session, id:int):
         return db.query(Administrateur).filter(Administrateur.id_admin==id).first()
    
    def get_all(self,db:Session):
        return db.query(Administrateur).all()
    
    def delete(self, db:Session,id:int):
        admin = self.get_by_id(db, id)
        if admin:
            db.delete(admin)
            db.commit()
            return "La suppression bien effectuée"
        return "Administrateur introuvable"
    
    def update(self,db:Session,id:int,new_administrateur=Administrateur):
            user = self.get_by_id(db, id)
            if user:
                user.nom=new_administrateur.nom
                user.prenom=new_administrateur.prenom
                user.email=new_administrateur.email
                user.mot_de_passe=new_administrateur.mot_de_passe
                db.commit()
                db.refresh(user)
                return user
            else:
                return"l'administrateur n'existe pas"