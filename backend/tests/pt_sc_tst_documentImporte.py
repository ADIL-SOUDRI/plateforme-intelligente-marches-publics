from app.core.database import SessionLocal
from app.models.document_importe import DocumentImporte
from app.models.utilisateur import Utilisateur
from app.repositories.document_importe_repository import DocumentImporteRepository
from app.enums.type_document import TypeDocument

db=SessionLocal()
repo=DocumentImporteRepository()

# doc1=DocumentImporte(titre="docImporte1",type= TypeDocument.CPS , nom_fichier="docImprte.pdf",taille=2.5,id_utilisateur=1)
# doc2=DocumentImporte(titre="docImporte2",type= TypeDocument.AUTRE,nom_fichier="docImprte.pdf",taille=2.5,id_utilisateur=2)

# save_doc1=repo.create(db,doc1)
# save_doc2=repo.create(db,doc2)

# print(save_doc1.titre,save_doc1.type,save_doc1.date_importation,save_doc1.id_utilisateur,save_doc1.id,save_doc1.nom_fichier,save_doc1.taille)
# print(save_doc2.titre,save_doc2.type,save_doc2.date_importation,save_doc2.id_utilisateur,save_doc2.id,save_doc2.nom_fichier,save_doc2.taille)

# docs=repo.get_all(db)
# for d in docs:
#     print(d.nom_fichier,d.taille)
# d=repo.get_by_id(db,2)
# print(d.nom_fichier,d.taille)

# d=DocumentImporte(titre="docImporte22",type= TypeDocument.DECRET,nom_fichier="Imprte.pdf",taille=5,id_utilisateur=2)
# repo.update(db,3,d)
# repo.delete(db,3)
