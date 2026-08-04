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
repo=AdministrateurRepo()
print("##############################")

#admin1=Administrateur(nom="yasser",prenom="yasser",email="yasser@gmail.com",mot_de_passe="12345")
#admin2=Administrateur(nom="ALi",prenom="ALi",email="ALi@gmail.com",mot_de_passe="12345")

#ad1=repo.create(db,admin1)
#ad2=repo.create(db,admin2)
#print(ad1.id_admin,ad2.id_admin)
#print("##############################")

admins = repo.get_all(db)


#for admin in admins:
    #print(admin.id_admin, admin.nom, admin.prenom)


user3=repo.get_by_id(db,4)
#print(user3.id_admin,user3.nom,user3.prenom,user3.email)
#print("##############################")

print(repo.delete(db,4))
#print("##############################")

user4=Administrateur(nom="Adil12",prenom="Adil12",email="adil151@gmail.com",mot_de_passe="123456")
#us=repo.update(db,4,user4)
#print(us.id_admin,us.nom,us.prenom,us.email)

print("OK")