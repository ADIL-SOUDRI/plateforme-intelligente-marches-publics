from app.services.document.vector_search_service import (
    VectorSearchService
)


service = VectorSearchService()


question = (
    "1. Quelles sont les mesures de sécurité et d'hygiène ?"
    "2. Comment sont gérés les déchets pendant l'exécution du marché ?"
    "3. Quelles sont les règles concernant la protection de l'environnement ?"
)


resultats = service.rechercher(
    question,
    nombre_resultats=5
)


print("\n========== RECHERCHE ==========\n")

for i in range(5):

    print(f"\n========== RESULTAT {i + 1} ==========")

    print(
        "Distance :",
        resultats["distances"][0][i]
    )

    print(
        "Métadonnées :",
        resultats["metadatas"][0][i]
    )

    print(
        "Contenu :"
    )

    print(
        resultats["documents"][0][i]
    )