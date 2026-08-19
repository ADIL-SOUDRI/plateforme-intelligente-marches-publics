from app.services.document.vector_search_service import (
    VectorSearchService
)


service = VectorSearchService()


question = (
    "Quelles sont les mesures de sécurité et d'hygiène ?"
)


resultats = service.rechercher(
    question=question,
    top_k=5,
    document_id="9"
)


print("\n========== TOP-K ==========\n")


documents = resultats["documents"][0]

metadatas = resultats["metadatas"][0]

distances = resultats["distances"][0]


for i in range(len(documents)):

    print(f"\n========== RESULTAT {i + 1} ==========")

    print(
        "Distance :",
        distances[i]
    )

    print(
        "Métadonnées :",
        metadatas[i]
    )

    print(
        "Contenu :"
    )

    print(
        documents[i]
    )