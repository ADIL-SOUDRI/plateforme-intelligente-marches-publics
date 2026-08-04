from pydantic import BaseModel

class UtilisateurCreate(BaseModel):
    nom:str
    prenom:str
    email:str
    mot_de_passe:str

class UtilisateurResponse(BaseModel):
    id_utilisateur:int
    nom:str
    prenom:str
    email:str
    class Config:
        from_attributes = True

class UtilisateurUpdate(BaseModel):
    nom:str
    prenom:str
    email:str
    mot_de_passe:str
    

