# from sqlalchemy import Column, Integer, DateTime, ForeignKey, String, func
# from app.core.database import Base
# from app.models.utilisateur import Utilisateur

# class Conversation(Base):

#     __tablename__ = "conversations"

#     id = Column(
#         Integer,
#         primary_key=True,
#         index=True,
#         autoincrement=True
#     )

#     titre = Column(
#         String,
#         nullable=True
#     )

#     date_creation = Column(
#         DateTime,
#         server_default=func.now()
#     )

#     id_utilisateur = Column(
#         Integer,
#         ForeignKey("utilisateurs.id_utilisateur"),
#         nullable=False
#     )