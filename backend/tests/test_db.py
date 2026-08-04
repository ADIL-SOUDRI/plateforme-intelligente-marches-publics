from app.core.database import SessionLocal

from app.models.administrateur import Administrateur
from app.models.utilisateur import Utilisateur
from app.models.document_reference import DocumentReference
from app.models.document_importe import DocumentImporte
from app.models.chat import Chat

from app.enums.type_document import TypeDocument

db = SessionLocal()

# ===========================
# Administrateur
# ===========================
admin = Administrateur(
  
    nom="Ahmed",
    prenom="Admin",
    email="admin@gmail.com",
    mot_de_passe="123456"
)
db.add(admin)
admin1 = Administrateur(
    
    nom="Iliass",
    prenom="Iliass",
    email="Iliass@gmail.com",
    mot_de_passe="123456"
)


db.add(admin1)

# ===========================
# Utilisateur
# ===========================
user = Utilisateur(
   
    nom="Adil",
    prenom="Soudri",
    email="adil@gmail.com",
    mot_de_passe="123456"
)

db.add(user)

db.commit()

# ===========================
# Document de référence
# ===========================
doc_ref = DocumentReference(
    
    titre="Décret 2.22.431",
    nom_fichier="decret.pdf",
    type=TypeDocument.DECRET,
    taille=2.5,
    admin_id=1
)

db.add(doc_ref)

# ===========================
# Document importé
# ===========================
doc_imp = DocumentImporte(
    
    titre="Mon CPS",
    nom_fichier="cps.pdf",
    type=TypeDocument.CPS,
    taille=1.8,
    utilisateur_id=1
)

db.add(doc_imp)

db.commit()

# ===========================
# Chat
# ===========================
chat = Chat(
  
    question="Quels sont les critères d'attribution ?",
    reponse="Les critères sont définis dans le CPS.",
    utilisateur_id=1,
    admin_id=1
)

db.add(chat)

db.commit()
db.close()

print("Toutes les données ont été insérées avec succès.")