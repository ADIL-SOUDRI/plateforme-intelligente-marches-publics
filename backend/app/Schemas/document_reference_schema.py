from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.enums.type_document import TypeDocument

class DocumentReferenceCreate(BaseModel):


    titre: str
    type: TypeDocument
    

class DocumentReferenceResponse(BaseModel):
    id: int
    nom_fichier: str
    taille: float
    chemin_fichier: Optional[str] = None
    date_ajout: datetime
    id_admin:int
    
    class Config:
        from_attributes = True

class DocumentReferenceUpdate(BaseModel):
    titre: str
    type: TypeDocument
    id_admin:int