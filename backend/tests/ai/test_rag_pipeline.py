from app.services.document.vector_search_service import (
    VectorSearchService
)

from app.services.rag.context_service import (
    ContextService
)

from app.services.rag.generation_service import (
    GenerationService
)


# ==================================================
# SERVICES
# ==================================================

vector_search_service = VectorSearchService()

context_service = ContextService()

generation_service = GenerationService()


# ==================================================
# QUESTIONS
# ==================================================

questions = [

   
    " Quelles sont les rues concernées par les travaux de voirie dans la ville d'Assilah ?"
    
]


# ==================================================
# TEST
# ==================================================

for question in questions:

    print("\n")
    print("=" * 70)

    print("QUESTION")
    print(question)

    print("=" * 70)


    # ==================================================
    # 1. RECHERCHE
    # ==================================================

    resultats = vector_search_service.rechercher(
        question=question,
        top_k=10,
        document_id=23
    )

    print(
        "\nNombre de résultats bruts :",
        len(resultats["documents"][0])
    )


    # ==================================================
    # 2. FILTRAGE
    # ==================================================

    resultats_filtres = (
        vector_search_service.filtrer_resultats(
            resultats,
            # distance_max=120.0
        )
    )

    print(
        "Nombre de résultats après filtrage :",
        len(resultats_filtres)
    )


    # ==================================================
    # 3. AFFICHAGE DES SOURCES
    # ==================================================

    for i, resultat in enumerate(
        resultats_filtres,
        start=1
    ):

        metadata = resultat["metadata"]

        print(
            f"\n--- SOURCE {i} ---"
        )

        print(
            "Document :",
            metadata.get("nom_fichier")
        )

        print(
            "Type :",
            metadata.get("type_source")
        )

        print(
            "Article :",
            metadata.get("article_numero")
        )

        print(
            "Distance :",
            resultat["distance"]
        )


    # ==================================================
    # 4. CONSTRUCTION DU CONTEXTE
    # ==================================================

    contexte = (
        context_service.construire_contexte(
            resultats_filtres
        )
    )


    print("\n========== CONTEXTE RAG ==========")

    print(contexte)


    # ==================================================
    # 5. GENERATION
    # ==================================================

    reponse = generation_service.generer_reponse(
        question=question,
        contexte=contexte
    )


    print("\n========== RÉPONSE LLM ==========")

    print(reponse)

# from app.services.document.vector_search_service import (
#     VectorSearchService
# )

# from app.services.rag.context_service import (
#     ContextService
# )

# from app.services.rag.generation_service import (
#     GenerationService
# )


# # ==================================================
# # SERVICES
# # ==================================================

# vector_search_service = VectorSearchService()

# context_service = ContextService()

# generation_service = GenerationService()


# # ==================================================
# # QUESTION
# # ==================================================
# question = """
# Quelle est la procédure exacte de paiement
# du titulaire après réception des fournitures ?
# """
# # ==================================================
# # 1. RECHERCHE
# # ==================================================

# resultats = vector_search_service.rechercher(
#     question=question,
#     top_k=5,
#     # document_id="9"
# )
# print("\n========== Question ==========")
# print(question)

# print("\n========== RECHERCHE ==========")

# print(
#     "Nombre de résultats bruts :",
#     len(resultats["documents"][0])
# )


# # ==================================================
# # 2. FILTRAGE
# # ==================================================

# resultats_filtres = (
#     vector_search_service.filtrer_resultats(
#         resultats,
#         distance_max=12.0
#     )
# )


# print("\n========== FILTRAGE ==========")

# print(
#     "Nombre de résultats après filtrage :",
#     len(resultats_filtres)
# )


# # ==================================================
# # 3. AFFICHER LES RÉSULTATS
# # ==================================================

# for i, resultat in enumerate(
#     resultats_filtres,
#     start=1
# ):

#     print(
#         f"\n--- RESULTAT {i} ---"
#     )

#     print(
#         "Distance :",
#         resultat["distance"]
#     )

#     print(
#         "Metadata :",
#         resultat["metadata"]
#     )

#     print(
#         "Contenu :",
#         resultat["contenu"][:500]
#     )


# # ==================================================
# # 4. CONSTRUCTION DU CONTEXTE
# # ==================================================

# contexte = context_service.construire_contexte(
#     resultats_filtres
# )


# print("\n========== CONTEXTE RAG ==========")

# print(contexte)


# # ==================================================
# # 5. GÉNÉRATION
# # ==================================================

# reponse = generation_service.generer_reponse(
#     question=question,
#     contexte=contexte
# )


# print("\n========== RÉPONSE LLM ==========")

# print(reponse)