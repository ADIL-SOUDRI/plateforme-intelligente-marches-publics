from app.services.document.embedding_service import EmbeddingService


service = EmbeddingService()

texte = """
Article 30 : Mesures de sécurité et d'hygiène.
Le titulaire doit prendre les mesures nécessaires
pour assurer la sécurité et l'hygiène.
"""

embedding = service.generer_embedding(texte)

print("Type :", type(embedding))
print("Dimension :", len(embedding))
print("Premiers éléments :", embedding[:5])
