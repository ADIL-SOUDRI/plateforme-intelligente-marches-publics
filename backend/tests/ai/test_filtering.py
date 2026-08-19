from app.services.document.vector_search_service import (
    VectorSearchService
)


service = VectorSearchService()


question = """
Quelles sont les obligations concernant
la sécurité et l'hygiène du fournisseur ?
"""


# ==========================================
# RECHERCHE
# ==========================================

resultats = service.rechercher(
    question,
    # nombre_resultats=5
)


print("\n========== AVANT FILTRAGE ==========")


documents = resultats["documents"][0]
metadatas = resultats["metadatas"][0]
distances = resultats["distances"][0]


for i in range(len(documents)):

    print(
        f"\n{i + 1}. "
        f"Distance = {distances[i]}"
    )

    print(
        "Document :",
        metadatas[i]["nom_fichier"]
    )

    print(
        "Article :",
        metadatas[i]["article_numero"]
    )


# ==========================================
# FILTRAGE
# ==========================================

resultats_filtres = service.filtrer_resultats(
    resultats,
    distance_max=100.0
)


print("\n========== APRÈS FILTRAGE ==========")


for i, resultat in enumerate(
    resultats_filtres
):

    print(
        f"\n{i + 1}. "
        f"Distance = {resultat['distance']}"
    )

    print(
        "Document :",
        resultat["metadata"]["nom_fichier"]
    )

    print(
        "Type :",
        resultat["metadata"]["type_source"]
    )

    print(
        "Article :",
        resultat["metadata"]["article_numero"]
    )

    print(
        "Titre :",
        resultat["metadata"]["article_titre"]
    )