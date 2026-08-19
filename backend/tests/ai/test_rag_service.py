from app.services.rag.rag_service import RAGService


service = RAGService()

# question = """
# Quelles sont les mesures de sécurité et d'hygiène
# que doit prendre le fournisseur ?
# """
question="""Quels sont les principes généraux de la passation des marchés publics ?"""
resultat = service.repondre(
    question=question,
    # document_id="9"
)

print("========== QUESTION ==========")
print(resultat["question"])

print("\n========== REPONSE ==========")
print(resultat["reponse"])

print("\n========== SOURCES ==========")

for source in resultat["sources"]:
    print(source)