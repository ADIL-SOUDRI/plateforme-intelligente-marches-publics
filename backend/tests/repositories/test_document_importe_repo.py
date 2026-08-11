from app.core.database import SessionLocal
from app.models.document_importe import DocumentImporte
from app.repositories.document_importe_repository import DocumentImporteRepository
from app.enums.type_document import TypeDocument
from app.models.utilisateur import Utilisateur


db = SessionLocal()
repo = DocumentImporteRepository()


doc1 = DocumentImporte(
    titre="CPS Travaux",
    type=TypeDocument.CPS,
    nom_fichier="CPS_Travaux.pdf",
    taille=2.5,
    id_utilisateur=1
)

doc2 = DocumentImporte(
    titre="Décret Marchés Publics",
    type=TypeDocument.DECRET,
    nom_fichier="Decret_Marches_Publics.pdf",
    taille=3.2,
    id_utilisateur=2
)

doc3 = DocumentImporte(
    titre="CPS Fournitures",
    type=TypeDocument.CPS,
    nom_fichier="CPS_Fournitures.pdf",
    taille=4.1,
    id_utilisateur=3
)

doc4 = DocumentImporte(
    titre="Guide Marchés Publics",
    type=TypeDocument.GUIDE,
    nom_fichier="Guide_Marches_Publics.pdf",
    taille=5.6,
    id_utilisateur=4
)

doc5 = DocumentImporte(
    titre="Circulaire Marchés Publics",
    type=TypeDocument.CIRCULAIRE,
    nom_fichier="Circulaire_Marches_Publics.pdf",
    taille=2.8,
    id_utilisateur=5
)

doc6 = DocumentImporte(
    titre="Autre Document",
    type=TypeDocument.AUTRE,
    nom_fichier="Autre_Document.pdf",
    taille=1.9,
    id_utilisateur=5
)


repo.create(db, doc1)
repo.create(db, doc2)
repo.create(db, doc3)
repo.create(db, doc4)
repo.create(db, doc5)
repo.create(db, doc6)


docs = repo.get_all(db)

print("Liste des documents importés :")

for doc in docs:
    print(
        doc.id,
        doc.titre,
        doc.type,
        doc.nom_fichier,
        doc.taille,
        doc.id_utilisateur
    )


doc = repo.get_by_id(db, 3)

print("\nDocument avec ID 3 :")

if doc:
    print(
        doc.id,
        doc.titre,
        doc.type,
        doc.nom_fichier,
        doc.taille,
        doc.id_utilisateur
    )


doc_modifie = DocumentImporte(
    titre="CPS Travaux Modifié",
    type=TypeDocument.CPS,
    nom_fichier="CPS_Travaux_Modifie.pdf",
    taille=6.5,
    id_utilisateur=3
)

doc = repo.update(db, 3, doc_modifie)

print("\nDocument modifié :")

if doc:
    print(
        doc.id,
        doc.titre,
        doc.type,
        doc.nom_fichier,
        doc.taille,
        doc.id_utilisateur
    )


doc = repo.get_by_id(db, 3)

print("\nVérification après modification :")

if doc:
    print(
        doc.id,
        doc.titre,
        doc.type,
        doc.nom_fichier,
        doc.taille,
        doc.id_utilisateur
    )


resultat = repo.delete(db, 6)

print("\nDocument supprimé :")
print(resultat)


doc = repo.get_by_id(db, 6)

print("\nVérification après suppression :")

if doc:
    print(
        doc.id,
        doc.titre,
        doc.type,
        doc.nom_fichier,
        doc.taille,
        doc.id_utilisateur
    )
else:
    print("Document introuvable")


docs = repo.get_all(db)

print("\nListe finale :")

for doc in docs:
    print(
        doc.id,
        doc.titre,
        doc.type,
        doc.nom_fichier,
        doc.taille,
        doc.id_utilisateur
    )


db.close()