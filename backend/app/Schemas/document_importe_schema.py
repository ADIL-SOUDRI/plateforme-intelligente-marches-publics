import datetime
from pydantic import BaseModel
from backend.app.enums.type_document import TypeDocument

class DocumentImporteCreate(BaseModel):


    titre: str
    type: TypeDocument
    

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
