from sqlalchemy import Column,DateTime, String, func,Integer,ForeignKey
from datetime import datetime

from app.models.document import Document


class DocumentImporte(Document):
    __tablename__="documents_importes"

    date_importation =Column(DateTime , server_default=func.now())
    id_utilisateur=Column(Integer ,ForeignKey("utilisateurs.id_utilisateur"))
    chemin_fichier = Column(
    String,
    nullable=False
)