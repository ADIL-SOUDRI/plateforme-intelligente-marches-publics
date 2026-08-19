from app.services.document.vector_search_service import (
    VectorSearchService
)

from app.services.document.context_builder_service import (
    ContextBuilderService
)


# ==========================================
# SERVICES
# ==========================================

search_service = VectorSearchService()

context_service = ContextBuilderService()


# ==========================================
# QUESTION
# ==========================================

question = """
Quelles sont les obligations du fournisseur
concernant la sécurité et l'hygiène ?
"""


# ==========================================
# RECHERCHE
# ==========================================

resultats = search_service.rechercher(
    question,
    # nombre_resultats=5
)


# ==========================================
# FILTRAGE
# ==========================================

resultats_filtres = search_service.filtrer_resultats(
    resultats,
    distance_max=12.0
)


# ==========================================
# CONTEXTE
# ==========================================

contexte = context_service.construire_contexte(
    resultats_filtres
)


# ==========================================
# AFFICHAGE
# ==========================================

print("\n========== QUESTION ==========")

print(question)


print("\n========== NOMBRE DE RESULTATS ==========")

print(
    len(resultats_filtres)
)


print("\n========== CONTEXTE RAG ==========")

print(contexte)




# from app.services.document.vector_search_service import (
#     VectorSearchService
# )

# from app.services.document.context_builder_service import (
#     ContextBuilderService
# )


# vector_search_service = VectorSearchService()
# context_builder = ContextBuilderService()


# questions = [

#     "Quelles sont les dispositions relatives aux documents constitutifs du marché ?",

#     "Quelles sont les mesures de sécurité et d'hygiène ?",

#     "Quelles sont les règles concernant la protection de l'environnement ?",

#     "Comment sont définis les prix du marché ?",

#     "Quels documents le fournisseur doit-il fournir en cas d'audit ?"
# ]


# for question in questions:

#     print("\n")
#     print("=" * 70)
#     print("QUESTION")
#     print("=" * 70)

#     print(question)

#     # Recherche
#     resultats = vector_search_service.rechercher(
#         question=question,
#         # nombre_resultats=5
#     )

#     # Construction du contexte
#     contexte = context_builder.construire_contexte(
#         resultats
#     )

#     print("\n")
#     print("=" * 70)
#     print("CONTEXTE RAG")
#     print("=" * 70)

#     print(contexte)