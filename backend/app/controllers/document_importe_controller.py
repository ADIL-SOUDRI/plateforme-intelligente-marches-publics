from fastapi import APIRouter, Depends, UploadFile, File, Form
from app.services.document.document_indexation_service import (
    DocumentIndexationService
)
from pathlib import Path
import shutil
from app.services.document_importe_service import DocumentImporteService
from app.core.database import SessionLocal
from app.models.document_importe import DocumentImporte

from app.schemas.document_importe_schema import DocumentImporteCreate,DocumentImporteResponse,DocumentImporteUpdate

from app.enums.type_document import TypeDocument
from app.core.dependencies import get_current_utilisateur


api = APIRouter()
service = DocumentImporteService()
indexation_service = DocumentIndexationService()
UPLOAD_DIR = Path("uploads/documents_importes")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
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

# @api.post( "/documents-importes",response_model=DocumentImporteResponse)
# def create(  titre: str = Form(...),
#             type: TypeDocument = Form(...),fichier: UploadFile = File(...),
#             current_utilisateur=Depends(get_current_utilisateur)):
#     db = SessionLocal()

#     try:
#         contenu = fichier.file.read()
#         id_utilisateur = int(current_utilisateur["sub"])
        
#         doc_create = DocumentImporteCreate(
#             titre=titre,
#             type=type,
#             id_utilisateur=id_utilisateur
#         )

      
#         document = DocumentImporte(
#             titre=doc_create.titre,
#             type=doc_create.type,
#             nom_fichier=fichier.filename,
#             taille=len(contenu),
#             id_utilisateur=id_utilisateur)
#         # resultat_indexation = (
#         #     indexation_service.indexer_document(
#         #         chemin_fichier=document.chemin_fichier,
#         #         document_id=document.id,
#         #         type_source="importe",
#         #         nom_fichier=document.nom_fichier
#         #     )
#         # )

#         return service.importer_document(db, document)

#     finally:
#         db.close()


@api.post(
    "/documents-importes",
    response_model=DocumentImporteResponse
)
def create(
    titre: str = Form(...),
    type: TypeDocument = Form(...),
    fichier: UploadFile = File(...),
    current_utilisateur=Depends(get_current_utilisateur)
):
    db = SessionLocal()

    try:

        # ==========================================
        # 1. UTILISATEUR CONNECTÉ
        # ==========================================

        id_utilisateur = int(
            current_utilisateur["sub"]
        )


        # ==========================================
        # 2. SAUVEGARDE DU FICHIER
        # ==========================================

        chemin = UPLOAD_DIR / fichier.filename

        with open(chemin, "wb") as buffer:
            shutil.copyfileobj(
                fichier.file,
                buffer
            )


        # ==========================================
        # 3. TAILLE DU FICHIER
        # ==========================================

        taille = chemin.stat().st_size


        # ==========================================
        # 4. CREATION DU DOCUMENT
        # ==========================================

        document = DocumentImporte(

            titre=titre,

            type=type,

            nom_fichier=fichier.filename,

            taille=taille,

            chemin_fichier=str(chemin),

            id_utilisateur=id_utilisateur
        )


        # ==========================================
        # 5. ENREGISTREMENT EN BASE
        # ==========================================

        document = service.importer_document(
            db,
            document
        )


        # ==========================================
        # 6. INDEXATION
        # ==========================================

        resultat_indexation = (
            indexation_service.indexer_document(

                chemin_fichier=document.chemin_fichier,

                document_id=document.id,

                type_source="importe",

                nom_fichier=document.nom_fichier

            )
        )


        # ==========================================
        # 7. RETOUR
        # ==========================================

        return document


    finally:

        db.close()

@api.put("/documents-importes/{id}",response_model=DocumentImporteResponse)
def update(id: int,doc: DocumentImporteUpdate,current_utilisateur=Depends(get_current_utilisateur)):
    db = SessionLocal()
    try:
        id_utilisateur = int(current_utilisateur["sub"])
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

@api.get(
    "/documents-importes_by_utilisateur",
    response_model=list[DocumentImporteResponse]
)
def get_all_documents_importes_by_utilisateur(
    current_utilisateur=Depends(get_current_utilisateur)
):
    db = SessionLocal()

    try:
        id_utilisateur = int(current_utilisateur["sub"])

        return service.get_all_documents_importes_by_utilisateur(
            db,
            id_utilisateur
        )

    finally:
        db.close()