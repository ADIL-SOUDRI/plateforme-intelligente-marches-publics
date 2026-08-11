from app.core.database import SessionLocal
from app.models.document_importe import DocumentImporte
from app.enums.type_document import TypeDocument
from app.services.document_importe_service import DocumentImporteService


db = SessionLocal()
service = DocumentImporteService()


# 1. Tester l'importation
document = DocumentImporte(
    titre="CPS test service",
    nom_fichier="cps_test_service.pdf",
    type=TypeDocument.CPS,
    taille=2.5,
    id_utilisateur=1
)

document = service.importer_document(db, document)

print("Document importé :")
print(document.id, document.titre, document.nom_fichier)


# 2. Tester l'obtention par ID
document = service.obtenir_document_importe(
    db,
    document.id
)

print("Document obtenu :")
if document:
    print(document.id, document.titre, document.nom_fichier)


# 3. Tester la liste
documents = service.lister_documents_importes(db)

print("Liste des documents :")
for doc in documents:
    print(doc.id, doc.titre, doc.nom_fichier)


# 4. Tester la modification
nouveau_document = DocumentImporte(
    titre="CPS modifié",
    nom_fichier="cps_modifie.pdf",
    type=TypeDocument.CPS,
    taille=3.5,
    id_utilisateur=1
)

document = service.modifier_document_importe(
    db,
    document.id,
    nouveau_document
)

print("Document modifié :")
if document:
    print(document.id, document.titre, document.nom_fichier)


# 5. Tester la suppression
resultat = service.supprimer_document_importe(
    db,
    document.id
)

print("Suppression :")
print(resultat)


db.close()