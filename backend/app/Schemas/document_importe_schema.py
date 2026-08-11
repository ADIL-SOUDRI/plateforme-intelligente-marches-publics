from datetime import datetime
from pydantic import BaseModel
from app.enums.type_document import TypeDocument

class DocumentImporteCreate(BaseModel):


    titre: str
    type: TypeDocument
    id_utilisateur: int

class DocumentImporteResponse(BaseModel):
    id: int
    nom_fichier: str
    taille: float
    date_importation: datetime
    id_utilisateur:int
    
    class Config:
        from_attributes = True

class DocumentImporteUpdate(BaseModel):
    titre: str
    type: TypeDocument
    id_utilisateur: int
