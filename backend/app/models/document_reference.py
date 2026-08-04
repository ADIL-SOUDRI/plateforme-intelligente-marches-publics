from sqlalchemy import Column,DateTime, func,Integer,ForeignKey
from app.models.document import Document


class DocumentReference(Document):
    __tablename__="documents_references"

    date_ajout =Column(DateTime , server_default=func.now())
    id_admin=Column(Integer,ForeignKey("administrateurs.id_admin"))