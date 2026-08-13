from fastapi import APIRouter, Depends, UploadFile, File, Form

from app.services.document_importe_service import DocumentImporteService
from app.core.database import SessionLocal
from app.models.document_importe import DocumentImporte

from app.schemas.document_importe_schema import DocumentImporteCreate,DocumentImporteResponse,DocumentImporteUpdate

from app.enums.type_document import TypeDocument
from app.core.dependencies import get_current_utilisateur


api = APIRouter()
service = DocumentImporteService()

@api.get("/documents-importes",response_model=list[DocumentImporteResponse])
def get_all(current_utilisateur=Depends(get_current_utilisateur)):
    db = SessionLocal()

    try:
        return service.lister_documents_importes(db)

    finally:
        db.close()

@api.get("/documents-importes/{id}",response_model=DocumentImporteResponse)
def get_by_id(id: int,current_utilisateur=Depends(get_current_utilisateur)):
    db = SessionLocal()

    try:
        return service.obtenir_document_importe(db, id)

    finally:
        db.close()

@api.post( "/documents-importes",response_model=DocumentImporteResponse)
def create( id_utilisateur: int = Form(...), titre: str = Form(...),
            type: TypeDocument = Form(...),fichier: UploadFile = File(...),
            current_utilisateur=Depends(get_current_utilisateur)):
    db = SessionLocal()

    try:
        contenu = fichier.file.read()

        
        doc_create = DocumentImporteCreate(
            titre=titre,
            type=type,
            id_utilisateur=id_utilisateur
        )

      
        document = DocumentImporte(
            titre=doc_create.titre,
            type=doc_create.type,
            nom_fichier=fichier.filename,
            taille=len(contenu),
            id_utilisateur=id_utilisateur)

        return service.importer_document(db, document)

    finally:
        db.close()


@api.put("/documents-importes/{id}",response_model=DocumentImporteResponse)
def update(id: int,doc: DocumentImporteUpdate,current_utilisateur=Depends(get_current_utilisateur)):
    db = SessionLocal()
    try:
        document = DocumentImporte(
            titre=doc.titre,
            type=doc.type,
            id_utilisateur=doc.id_utilisateur
        )

        return service.modifier_document_importe(db,id,document)

    finally:
        db.close()


@api.delete("/documents-importes/{id}")
def delete(id: int,current_utilisateur=Depends(get_current_utilisateur)):
    db = SessionLocal()

    try:
        return service.supprimer_document_importe(db, id)

    finally:
        db.close()