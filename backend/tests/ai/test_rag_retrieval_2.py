from app.services.document.vector_search_service import (
    VectorSearchService
)

from app.services.document.context_builder_service import (
    ContextBuilderService
)


vector_search_service = VectorSearchService()
context_builder = ContextBuilderService()


questions = [

    "Quelles sont les dispositions relatives aux documents constitutifs du marché ?",

    "Quelles sont les mesures de sécurité et d'hygiène ?",

    "Quelles sont les règles concernant la protection de l'environnement ?",

    "Comment sont définis les prix du marché ?",

    "Quels documents le fournisseur doit-il fournir en cas d'audit ?"
]

for question in questions:

    print("\n" + "=" * 70)
    print("QUESTION :", question)
    print("=" * 70)

    resultats = vector_search_service.rechercher(
        question=question,
        # nombre_resultats=5
    )

    documents = resultats["documents"][0]
    metadatas = resultats["metadatas"][0]
    distances = resultats["distances"][0]

    for i in range(len(documents)):

        metadata = metadatas[i]

        print(
            f"\nRésultat {i + 1}"
        )

        print(
            "Distance :",
            distances[i]
        )

        print(
            "Article :",
            metadata.get("article_numero")
        )

        print(
            "Titre :",
            metadata.get("article_titre")
        )