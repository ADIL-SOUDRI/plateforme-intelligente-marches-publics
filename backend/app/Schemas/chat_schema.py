from datetime import datetime
from pydantic import BaseModel

class ChatCreate(BaseModel):
    question:str

class ChatResponse(BaseModel):
    id:int 
    question:str
    response:str
    date_creation:datetime
    id_utilisateur:int
    id_administrateur:int
    id_document_importe:int
    class Config:
        from_attributes = True