from pydantic import BaseModel

class AdministrateurCreate(BaseModel):
    nom:str
    prenom:str
    email:str
    mot_de_passe:str

class AdministrateurResponse(BaseModel):
    id_admin:int
    nom:str
    prenom:str
    email:str
    class Config:
        from_attributes = True

class AdministrateurUpdate(BaseModel):
    nom:str
    prenom:str
    email:str
    mot_de_passe:str