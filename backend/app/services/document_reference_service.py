from sqlalchemy.orm import Session
from app.models.document_reference import DocumentReference
from app.repositories.document_reference_repository import DocumentReferenceRepository
from app.exceptions.document_exceptions import DocumentReferenceNotFoundException

class DocumentReferenceService:

    def __init__(self):
        self.repo=DocumentReferenceRepository()

    def creer_document_reference(self,db:Session,doc:DocumentReference):
        return self.repo.create(db,doc)
    
    def lister_documents_references(self,db:Session):
        return self.repo.get_all(db)
    
    def supprimer_document_reference(self,db:Session,id:int):
        document = self.repo.get_by_id(db, id)

        if not document:
            raise DocumentReferenceNotFoundException()

        return self.repo.delete(db, id)
    
    def obtenir_document_reference(self,db:Session,id:int):
        document = self.repo.get_by_id(db, id)

        if not document:
            raise DocumentReferenceNotFoundException()

        return document
    
    def modifier_document_reference(self,db:Session,id:int,doc:DocumentReference):
        document = self.repo.get_by_id(db, id)

        if not document:
            raise DocumentReferenceNotFoundException()

        return self.repo.update(db, id, doc)