from app.core.database import SessionLocal
from app.models.utilisateur import Utilisateur
from app.repositories.utilisateur_repository import UtilisateurRepo


db = SessionLocal()
repo = UtilisateurRepo()


user1 = Utilisateur(
    nom="Yasser",
    prenom="Yasser",
    email="yasser@gmail.com",
    mot_de_passe="12345"
)

user2 = Utilisateur(
    nom="Ali",
    prenom="Ali",
    email="ali@gmail.com",
    mot_de_passe="12345"
)

user3 = Utilisateur(
    nom="Adil",
    prenom="Adil",
    email="adil@gmail.com",
    mot_de_passe="123456"
)

user4 = Utilisateur(
    nom="Ahmed",
    prenom="Ahmed",
    email="ahmed@gmail.com",
    mot_de_passe="123456"
)

user5 = Utilisateur(
    nom="Omar",
    prenom="Omar",
    email="omar@gmail.com",
    mot_de_passe="123456"
)

user6 = Utilisateur(
    nom="Walid",
    prenom="Walid",
    email="walid@gmail.com",
    mot_de_passe="123456"
)


repo.create(db, user1)
repo.create(db, user2)
repo.create(db, user3)
repo.create(db, user4)
repo.create(db, user5)
repo.create(db, user6)



users = repo.get_all(db)

print("Liste des utilisateurs :")

for user in users:
    print(
        user.id_utilisateur,
        user.nom,
        user.prenom,
        user.email
    )


user = repo.get_by_id(db, 3)

print("\nUtilisateur avec ID 3 :")

if user:
    print(
        user.id_utilisateur,
        user.nom,
        user.prenom,
        user.email
    )


user_modifie = Utilisateur(
    nom="Adil_Modifie",
    prenom="Adil_Modifie",
    email="adil.modifie@gmail.com",
    mot_de_passe="987654"
)

user = repo.update(db, 3, user_modifie)

print("\nUtilisateur modifié :")

if user:
    print(
        user.id_utilisateur,
        user.nom,
        user.prenom,
        user.email
    )


user = repo.get_by_id(db, 3)

print("\nVérification après modification :")

if user:
    print(
        user.id_utilisateur,
        user.nom,
        user.prenom,
        user.email
    )


resultat = repo.delete(db, 6)

print("\nUtilisateur supprimé :")
print(resultat)


user = repo.get_by_id(db, 6)

print("\nVérification après suppression :")

if user:
    print(
        user.id_utilisateur,
        user.nom,
        user.prenom,
        user.email
    )
else:
    print("Utilisateur introuvable")


users = repo.get_all(db)

print("\nListe finale :")

for user in users:
    print(
        user.id_utilisateur,
        user.nom,
        user.prenom,
        user.email
    )


db.close()