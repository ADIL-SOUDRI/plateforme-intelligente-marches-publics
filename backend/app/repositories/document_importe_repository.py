from sqlalchemy.orm import Session
from app.models.document_importe import DocumentImporte

class DocumentImporteRepository:

    def create(self, db:Session,document:DocumentImporte):
        db.add(document)
        db.commit()
        db.refresh(document)
        return document

    def get_all(self ,db:Session):
        return db.query(DocumentImporte).all()
    def get_by_id(self,db:Session,id:int):
        return db.query(DocumentImporte).filter(DocumentImporte.id==id).first()

    def delete(self,db: Session,id:int):
        document = db.query(DocumentImporte).filter( DocumentImporte.id == id).first()

        if document:
            db.delete(document)
            db.commit()
            return document
        
    def update(self,db:Session,id:int,new_document:DocumentImporte):
        doc=self.get_by_id(db,id)
        if doc:
             doc.titre=new_document.titre
             doc.type=new_document.type
             db.commit()
             db.refresh(doc)
             return doc 
        
