from fastapi import APIRouter, Depends, UploadFile, File, Form

from app.services.document_reference_service import DocumentReferenceService
from app.core.database import SessionLocal
from app.models.document_reference import DocumentReference
from app.schemas.document_reference_schema import DocumentReferenceResponse,DocumentReferenceUpdate,DocumentReferenceCreate
from app.enums.type_document import TypeDocument
from app.core.dependencies import get_current_admin


api = APIRouter()
service = DocumentReferenceService()

@api.get("/documents-references",response_model=list[DocumentReferenceResponse])
def get_all(current_admin=Depends(get_current_admin)):
    db = SessionLocal()

    try:
        return service.lister_documents_references(db)

    finally:
        db.close()



@api.get("/documents-references/{id}",response_model=DocumentReferenceResponse)
def get_by_id(id: int,current_admin=Depends(get_current_admin)):
    db = SessionLocal()

    try:
        return service.obtenir_document_reference(db, id)

    finally:
        db.close()


@api.post("/documents-references",response_model=DocumentReferenceResponse)
def create(titre: str = Form(...),type: TypeDocument = Form(...),
           id_admin: int = Form(...),fichier: UploadFile = File(...),
           current_admin=Depends(get_current_admin)):
    db = SessionLocal()

    try:
        contenu = fichier.file.read()
        doc_create = DocumentReferenceCreate(
            titre=titre,
            type=type)

        document = DocumentReference(
            titre=doc_create.titre,
            type=doc_create.type,
            nom_fichier=fichier.filename,
            taille=len(contenu),
            id_admin=id_admin)

        return service.creer_document_reference(db, document)

    finally:
        db.close()

@api.put("/documents-references/{id}",response_model=DocumentReferenceResponse)
def update(id: int,doc: DocumentReferenceUpdate,current_admin=Depends(get_current_admin)):
    db = SessionLocal()

    try:
        document = DocumentReference(
            titre=doc.titre,
            type=doc.type)

        return service.modifier_document_reference(db,id,document)

    finally:
        db.close()


@api.delete( "/documents-references/{id}")
def delete(id: int,current_admin=Depends(get_current_admin)):
    db = SessionLocal()

    try:
        return service.supprimer_document_reference(db, id)

    finally:
        db.close()