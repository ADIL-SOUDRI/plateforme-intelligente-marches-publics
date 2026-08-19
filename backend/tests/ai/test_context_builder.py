from app.services.document.vector_search_service import (
    VectorSearchService
)

from app.services.document.context_builder_service import (
    ContextBuilderService
)


# ==================================================
# QUESTION
# ==================================================

question = """
Quelles sont les dispositions relatives
aux documents constitutifs du marché ?
"""


# ==================================================
# RECHERCHE VECTORIELLE
# ==================================================

vector_search_service = VectorSearchService()

resultats = vector_search_service.rechercher(
    question=question,
    # nombre_resultats=5
)


# ==================================================
# CONSTRUCTION DU CONTEXTE
# ==================================================

context_builder = ContextBuilderService()

contexte = context_builder.construire_contexte(
    resultats
)


# ==================================================
# AFFICHAGE
# ==================================================

print("\n========== QUESTION ==========\n")

print(question)

print("\n========== CONTEXTE RAG ==========\n")

print(contexte)