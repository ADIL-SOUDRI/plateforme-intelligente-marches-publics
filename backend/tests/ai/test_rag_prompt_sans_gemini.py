from app.services.document.vector_search_service import (
    VectorSearchService
)

from app.services.document.context_builder_service import (
    ContextBuilderService
)

from app.services.ai.rag_prompt_service import (
    RagPromptService
)


# ==================================================
# QUESTION
# ==================================================

# question = """
# Quelles sont les mesures de sécurité et d'hygiène ?
# """

questions = [
    "Quelles sont les mesures de sécurité et d'hygiène ?",

    "Quelles sont les dispositions relatives aux documents constitutifs du marché ?",

    "Quelles sont les règles concernant la protection de l'environnement ?",

    "Comment sont définis les prix du marché ?",

    "Quels documents le fournisseur doit-il fournir en cas d'audit ?"
]
# ==================================================
# SERVICES
# ==================================================

vector_search_service = VectorSearchService()

context_builder = ContextBuilderService()

rag_prompt_service = RagPromptService()


# ==================================================
# 1. RECHERCHE VECTORIELLE
# ==================================================

resultats = vector_search_service.rechercher(
    question=questions,
    # nombre_resultats=5
)


# ==================================================
# 2. CONSTRUCTION DU CONTEXTE
# ==================================================

contexte = context_builder.construire_contexte(
    resultats
)


# ==================================================
# 3. CONSTRUCTION DU PROMPT
# ==================================================

prompt = rag_prompt_service.construire_prompt(
    question=questions,
    contexte=contexte
)


# ==================================================
# AFFICHAGE
# ==================================================

print("\n========== QUESTION ==========\n")

print(questions)

print("\n========== CONTEXTE ==========\n")

print(contexte)

print("\n========== PROMPT RAG ==========\n")

print(prompt)