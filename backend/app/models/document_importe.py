from sqlalchemy import Column,DateTime, func,Integer,ForeignKey
from datetime import datetime

from app.models.document import Document


class DocumentImporte(Document):
    __tablename__="documents_importes"

    date_importation =Column(DateTime , server_default=func.now())
    utilisateur_id=Column(Integer ,ForeignKey("utilisateurs.id_utilisateur"))
