from app.core.database import SessionLocal
from app.models.chat import Chat
from app.models.administrateur import Administrateur
#from app.models.document import Document
from app.models.document_importe import DocumentImporte
from app.models.document_reference import DocumentReference
from app.models.utilisateur import Utilisateur
from app.repositories.administrateur_repository import AdministrateurRepo
from app.repositories.chat_repository import ChatRepo
from app.repositories.document_importe_repository import DocumentImporteRepository
from app.repositories.document_reference_repository import DocumentReferenceRepository
from app.repositories.utilisateur_repository import UtilisateurRepo

db=SessionLocal()
repo=UtilisateurRepo()
print("##############################")

#user1=Utilisateur(nom="yasser",prenom="yasser",email="yasser@gmail.com",mot_de_passe="12345")
#user2=Utilisateur(nom="ALi",prenom="ALi",email="ALi@gmail.com",mot_de_passe="12345")

#repo.create(db,user1)
#repo.create(db,user2)
print("##############################")

users = repo.get_all(db)

#print("\nGET ALL :")
#for u in users:
    #print(u.id_utilisateur, u.nom, u.prenom)
#print("##############################")

print("\n un seul element :")
user3=repo.get_by_id(db,16)
#print(user3.id_utilisateur,user3.nom,user3.prenom,user3.email)
print("##############################")

#print(repo.delete(db,20))
print("##############################")

user4=Utilisateur(nom="Adil12",prenom="Adil12",email="adil151@gmail.com",mot_de_passe="123456")
us=repo.update(db,21,user4)
print(us.id_utilisateur,us.nom,us.prenom,us.email)

print("OK")