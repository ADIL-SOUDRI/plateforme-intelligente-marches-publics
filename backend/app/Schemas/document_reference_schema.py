import datetime
from pydantic import BaseModel
from backend.app.enums.type_document import TypeDocument

class DocumentReferenceCreate(BaseModel):


    titre: str
    type: TypeDocument
    

class DocumentReferenceResponse(BaseModel):
    id: int
    nom_fichier: str
    taille: float
    date_ajout: datetime
    id_utilisateur:int
    
    class Config:
        from_attributes = True

class DocumentReferenceUpdate(BaseModel):
    titre: str
    type: TypeDocument