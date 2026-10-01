from sqlalchemy.orm import Session
from app.models.document_importe import DocumentImporte
from app.repositories.document_importe_repository import DocumentImporteRepository

class DocumentImporteService:

    def __init__(self):
        self.repo=DocumentImporteRepository()

    def importer_document(self,db:Session,doc:DocumentImporte):
        return self.repo.create(db,doc)

    def lister_documents_importes(self,db:Session):
        return self.repo.get_all(db)
    
    def supprimer_document_importe(self,db:Session,id:int):
        return self.repo.delete(db,id)
    
    def obtenir_document_importe(self,db:Session,id:int):
        return self.repo.get_by_id(db,id)
    
    def modifier_document_importe(self,db:Session,id:int,doc:DocumentImporte):
        return self.repo.update(db,id,doc)

    from sqlalchemy.orm import Session
from app.models.document_importe import DocumentImporte
from app.repositories.document_importe_repository import DocumentImporteRepository
from app.exceptions.document_exceptions import DocumentImporteNotFoundException


class DocumentImporteService:

    def __init__(self):
        self.repo = DocumentImporteRepository()

    def importer_document(self, db: Session, doc: DocumentImporte):
        return self.repo.create(db, doc)

    def lister_documents_importes(self, db: Session):
        return self.repo.get_all(db)

    def get_all_documents_importes_by_utilisateur(self, db: Session,id_utilisateur: int):
            return self.repo.get_all_documents_importes_by_utilisateur(
                db,
                id_utilisateur
            )

    def supprimer_document_importe(self, db: Session, id: int):

        document = self.repo.get_by_id(db, id)

        if not document:
            raise DocumentImporteNotFoundException()

        return self.repo.delete(db, id)

    def obtenir_document_importe(self, db: Session, id: int):

        document = self.repo.get_by_id(db, id)

        if not document:
            raise DocumentImporteNotFoundException()

        return document

    def modifier_document_importe(self, db: Session, id: int, doc: DocumentImporte):

        document = self.repo.get_by_id(db, id)

        if not document:
            raise DocumentImporteNotFoundException()

        return self.repo.update(db, id, doc)