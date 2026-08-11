from app.core.database import SessionLocal
from app.models.document_reference import DocumentReference
from app.enums.type_document import TypeDocument
from app.services.document_reference_service import DocumentReferenceService
from app.models.administrateur import Administrateur


db = SessionLocal()
service = DocumentReferenceService()


document = DocumentReference(
    titre="Décret test",
    nom_fichier="decret_test.pdf",
    type=TypeDocument.DECRET,
    taille=2.5,
    id_admin=5
)

document = service.creer_document_reference(db, document)

print("Document créé :")
print(document.id, document.titre, document.nom_fichier)


document = service.obtenir_document_reference(db, document.id)

print("Document récupéré :")
print(document.id, document.titre, document.nom_fichier)


documents = service.lister_documents_references(db)

print("Liste des documents :")
for doc in documents:
    print(doc.id, doc.titre, doc.nom_fichier)


new_document = DocumentReference(
    titre="Décret modifié",
    nom_fichier="decret_modifie.pdf",
    type=TypeDocument.DECRET,
    taille=3.5,
    id_admin=5
)

document = service.modifier_document_reference(
    db,
    document.id,
    new_document
)

print("Document modifié :")
print(document.id, document.titre, document.nom_fichier)


resultat = service.supprimer_document_reference(
    db,
    document.id
)

print("Suppression :")
print(resultat)

db.close()