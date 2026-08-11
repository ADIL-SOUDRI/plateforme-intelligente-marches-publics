from app.core.database import SessionLocal
from app.models.administrateur import Administrateur
from app.services.administrateur_service import AdministrateurService


db = SessionLocal()
service = AdministrateurService()


admin = Administrateur(
    nom="Admin",
    prenom="Test",
    email="admin_service@gmail.com",
    mot_de_passe="12345"
)

admin = service.creer_administrateur(db, admin)

# print("Administrateur créé :")
# print(admin.id_admin, admin.nom, admin.prenom, admin.email)


admin = service.obtenir_administrateur(db, admin.id_admin)

print("Administrateur récupéré :")
print(admin.id_admin, admin.nom, admin.prenom, admin.email)


admins = service.lister_administrateurs(db)

print("Liste des administrateurs :")
for admin in admins:
    print(admin.id_admin, admin.nom, admin.prenom)


new_admin = Administrateur(
    nom="AdminModifie",
    prenom="TestModifie",
    email="admin_modifie@gmail.com",
    mot_de_passe="123456"
)

admin = service.modifier_administrateur(
    db,
    admin.id_admin,
    new_admin
)

print("Administrateur modifié :")
print(admin.id_admin, admin.nom, admin.prenom, admin.email)


resultat = service.supprimer_administrateur(db, admin.id_admin)

print("Suppression :")
print(resultat)

db.close()