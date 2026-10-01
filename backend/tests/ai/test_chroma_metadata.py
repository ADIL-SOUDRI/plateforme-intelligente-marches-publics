# import chromadb


# client = chromadb.PersistentClient(
#     path="chroma_db"
# )

# collection = client.get_collection(
#     name="documents_publics"
# )

# resultats = collection.get(
#     limit=10
# )

# for i in range(
#     len(resultats["ids"])
# ):

#     print("\n==============================")
#     print("ID :", resultats["ids"][i])
#     print(
#         "Document :",
#         resultats["metadatas"][i].get(
#             "nom_fichier"
#         )
#     )
#     print(
#         "Article :",
#         resultats["metadatas"][i].get(
#             "article_numero"
#         )
#     )
#     print(
#         "Titre :",
#         resultats["metadatas"][i].get(
#             "article_titre"
#         )
#     )
#     print(
#         "Page :",
#         resultats["metadatas"][i].get(
#             "page"
#         )
#     )

# from app.services.document.document_extraction_service import (
#     DocumentExtractionService
# )

# service = DocumentExtractionService()

# texte = service.extraire_texte(
#     "uploads/documents_references/ccag_travaux.pdf"
# )

# print(texte[:5000])
from app.services.document.document_extraction_service import (
    DocumentExtractionService
)

from app.services.document.document_cleaning_service import (
    DocumentCleaningService
)

from app.services.document.document_structure_service import (
    DocumentStructureService
)


fichier = "uploads/documents_references/ccag_fournitures.pdf"


# 1. Extraction
extraction = DocumentExtractionService()

texte = extraction.extraire_texte(
    fichier
)

print("=" * 70)
print("TEST EXTRACTION")
print("=" * 70)

print(texte[:3000])


# 2. Nettoyage
cleaning = DocumentCleaningService()

texte_propre = cleaning.nettoyer(
    texte
)


# 3. Structure
structure = DocumentStructureService()

texte_structure = structure.supprimer_sommaire(
    texte_propre
)

articles = structure.trouver_articles(
    texte_structure
)


print("\n")
print("=" * 70)
print("TEST STRUCTURATION")
print("=" * 70)

print(
    "Nombre articles :",
    len(articles)
)


for article in articles[:20]:

    print("\n------------------------------")

    print(
        "Article :",
        article.get("numero")
    )

    print(
        "Titre :",
        article.get("titre")
    )

    print(
        "Page :",
        article.get("page")
    )

    print(
        "Contenu :",
        article.get("contenu", "")[:200]
    )