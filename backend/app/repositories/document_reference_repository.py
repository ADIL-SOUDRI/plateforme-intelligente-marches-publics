from sqlalchemy.orm import Session
from app.models.document_reference import DocumentReference

class DocumentReferenceRepository:

    def create(self, db:Session,document:DocumentReference):
        db.add(document)
        db.commit()
        db.refresh(document)
        return document

    def get_all(self ,db:Session):
        return db.query(DocumentReference).all()

    def delete(self,db: Session,id:int):
        document = db.query(DocumentReference).filter(DocumentReference.id == id).first()

        if document:
            db.delete(document)
            db.commit()
            return document
    def update(self, db: Session, id: int, new_document: DocumentReference):
        doc = self.get_by_id(db, id)
        if doc:
                doc.titre=new_document.titre
                doc.type=new_document.type
                db.commit()
                db.refresh(doc)
                return doc 
        

    def get_by_id(self, db: Session, id: int):
        return db.query(DocumentReference).filter(
            DocumentReference.id == id
        ).first()