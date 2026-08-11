from app.core.database import SessionLocal
from app.models.administrateur import Administrateur
from app.repositories.administrateur_repository import AdministrateurRepo


db = SessionLocal()
repo = AdministrateurRepo()


admin1 = Administrateur(
    nom="Yasser",
    prenom="Yasser",
    email="yasser@gmail.com",
    mot_de_passe="12345"
)

admin2 = Administrateur(
    nom="Ali",
    prenom="Ali",
    email="ali@gmail.com",
    mot_de_passe="12345"
)

admin3 = Administrateur(
    nom="Adil",
    prenom="Adil",
    email="adil@gmail.com",
    mot_de_passe="123456"
)

admin4 = Administrateur(
    nom="Ahmed",
    prenom="Ahmed",
    email="ahmed@gmail.com",
    mot_de_passe="123456"
)

admin5 = Administrateur(
    nom="Omar",
    prenom="Omar",
    email="omar@gmail.com",
    mot_de_passe="123456"
)


repo.create(db, admin1)
repo.create(db, admin2)
repo.create(db, admin3)
repo.create(db, admin4)
repo.create(db, admin5)


# admins = repo.get_all(db)

# print("Liste des administrateurs :")

# for admin in admins:
#     print(
#         admin.id_admin,
#         admin.nom,
#         admin.prenom,
#         admin.email
#     )


# admin = repo.get_by_id(db, 3)

# print("Administrateur avec ID 3 :")

# if admin:
#     print(
#         admin.id_admin,
#         admin.nom,
#         admin.prenom,
#         admin.email
#     )


# admin_modifie = Administrateur(
#     nom="Adil_Modifie",
#     prenom="Adil_Modifie",
#     email="adil.modifie@gmail.com",
#     mot_de_passe="987654"
# )

# admin = repo.update(db, 3, admin_modifie)

# print("Administrateur modifié :")

# if admin:
#     print(
#         admin.id_admin,
#         admin.nom,
#         admin.prenom,
#         admin.email
#     )


# admin = repo.get_by_id(db, 3)

# print("Vérification après modification :")

# if admin:
#     print(
#         admin.id_admin,
#         admin.nom,
#         admin.prenom,
#         admin.email
#     )


# resultat = repo.delete(db, 5)

# print("Administrateur supprimé :")
# print(resultat)


admins = repo.get_all(db)

print("Liste finale :")

for admin in admins:
    print(
        admin.id_admin,
        admin.nom,
        admin.prenom,
        admin.email
    )


db.close()