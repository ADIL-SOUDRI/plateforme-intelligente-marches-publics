from app.core.database import SessionLocal
from app.models.document_reference import DocumentReference
from app.models.administrateur import Administrateur
from app.repositories.document_reference_repository import DocumentReferenceRepository
from app.enums.type_document import TypeDocument

db=SessionLocal()
repo=DocumentReferenceRepository()

# doc1=DocumentReference(titre="docImporte1",type= TypeDocument.CPS , nom_fichier="docImprte.pdf",taille=2.5,id_admin=1)
# doc2=DocumentReference(titre="docImporte2",type= TypeDocument.AUTRE,nom_fichier="docImprte.pdf",taille=2.5,id_admin=2)

# save_doc1=repo.create(db,doc1)
# save_doc2=repo.create(db,doc2)

# print(save_doc1.titre,save_doc1.type,save_doc1.date_ajout,save_doc1.id_admin,save_doc1.id,save_doc1.nom_fichier,save_doc1.taille)
# print(save_doc2.titre,save_doc2.type,save_doc2.date_ajout,save_doc2.id_admin,save_doc2.id,save_doc2.nom_fichier,save_doc2.taille)

# docs=repo.get_all(db)
# for d in docs:
#     print(d.nom_fichier,d.taille)
# d=repo.get_by_id(db,8)
# print(d.nom_fichier,d.taille)

# d=DocumentReference(titre="docImporte22",type= TypeDocument.DECRET,nom_fichier="Imprte.pdf",taille=5,id_admin=2)
# repo.update(db,9,d)
# repo.delete(db,9)
