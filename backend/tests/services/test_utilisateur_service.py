from app.core.database import SessionLocal
from app.models.utilisateur import Utilisateur
from app.services.utilisateur_service import UtilisateurService


db = SessionLocal()
service = UtilisateurService()


# Test de création
user = Utilisateur(
    nom="Test",
    prenom="Service",
    email="testservice@gmail.com",
    mot_de_passe="12345"
)

user = service.creer_utilisateur(db, user)

print("Utilisateur créé :")
# print(user.id_utilisateur, user.nom, user.prenom, user.email)


# Test de récupération par ID
user = service.obtenir_utilisateur(db, user.id_utilisateur)

print("\nUtilisateur récupéré :")
print(user.id_utilisateur, user.nom, user.prenom, user.email)


# Test de récupération de tous les utilisateurs
users = service.lister_utilisateurs(db)

print("\nListe des utilisateurs :")
for user in users:
    print(user.id_utilisateur, user.nom, user.prenom)


# Test de modification
new_user = Utilisateur(
    nom="Adil",
    prenom="Modifié",
    email="adilmodifie@gmail.com",
    mot_de_passe="123456"
)

user = service.modifier_utilisateur(
    db,
    user.id_utilisateur,
    new_user
)

print("\nUtilisateur modifié :")
print(user.id_utilisateur, user.nom, user.prenom, user.email)


# Test de suppression
resultat = service.supprimer_utilisateur(
    db,
    user.id_utilisateur
)

print("\nSuppression :")
print(resultat)


db.close()