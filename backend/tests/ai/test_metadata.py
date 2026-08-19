from pathlib import Path

from app.services.document.document_extraction_service import (
    DocumentExtractionService
)

from app.services.document.document_cleaning_service import (
    DocumentCleaningService
)

from app.services.document.document_structure_service import (
    DocumentStructureService
)

from app.services.document.document_chunk_service import (
    DocumentChunkService
)

from app.services.document.embedding_service import (
    EmbeddingService
)


# ==================================================
# FICHIER
# ==================================================

chemin = Path(
    "uploads/documents_references/ccag_fournitures.pdf"
)


print("========== FICHIER ==========")

print("Fichier :", chemin.name)
print("Existe :", chemin.exists())


# ==================================================
# 1. EXTRACTION
# ==================================================

extraction_service = DocumentExtractionService()

texte = extraction_service.extraire_texte(
    str(chemin)
)


# ==================================================
# 2. NETTOYAGE
# ==================================================

cleaning_service = DocumentCleaningService()

texte_propre = cleaning_service.nettoyer(
    texte
)


# ==================================================
# 3. STRUCTURE
# ==================================================

structure_service = DocumentStructureService()

texte_document = structure_service.supprimer_sommaire(
    texte_propre
)


# ==================================================
# 4. ARTICLES
# ==================================================

articles = structure_service.trouver_articles(
    texte_document
)

print("\nNombre d'articles :", len(articles))


# ==================================================
# 5. CHUNKING
# ==================================================

chunk_service = DocumentChunkService(
    chunk_size=1500,
    chunk_overlap=200
)

chunks = chunk_service.decouper_articles(
    articles
)

print("Nombre de chunks :", len(chunks))


# ==================================================
# 6. EMBEDDINGS
# ==================================================

embedding_service = EmbeddingService()

textes = [
    chunk["contenu"]
    for chunk in chunks
]

embeddings = embedding_service.generer_embeddings(
    textes
)

print("Nombre d'embeddings :", len(embeddings))


# ==================================================
# 7. CONSTRUCTION DES METADONNEES
# ==================================================

documents_vectoriels = []

for i, chunk in enumerate(chunks):

    document_vectoriel = {

        "contenu": chunk["contenu"],

        "embedding": embeddings[i],

        "metadata": {

            "article_numero": chunk["article_numero"],

            "article_titre": chunk["article_titre"],

            "chunk_index": chunk["chunk_index"],

            "document": chemin.name
        }
    }

    documents_vectoriels.append(
        document_vectoriel
    )


# ==================================================
# 8. TEST DES METADONNEES
# ==================================================

print("\n========== TEST METADONNEES ==========")

print(
    "Nombre de documents vectoriels :",
    len(documents_vectoriels)
)


# ==================================================
# 9. TEST PREMIER CHUNK
# ==================================================

premier = documents_vectoriels[0]

print("\n========== PREMIER DOCUMENT VECTORIEL ==========")

print(
    "Document :",
    premier["metadata"]["document"]
)

print(
    "Article :",
    premier["metadata"]["article_numero"]
)

print(
    "Titre :",
    premier["metadata"]["article_titre"]
)

print(
    "Chunk :",
    premier["metadata"]["chunk_index"]
)

print(
    "Taille du contenu :",
    len(premier["contenu"])
)

print(
    "Dimension embedding :",
    len(premier["embedding"])
)


# ==================================================
# 10. VERIFICATION DE LA CORRESPONDANCE
# ==================================================

print("\n========== VERIFICATION CORRESPONDANCE ==========")

erreurs = 0


for i, document in enumerate(documents_vectoriels):

    contenu = document["contenu"]
    embedding = document["embedding"]
    metadata = document["metadata"]

    # Vérifier le contenu
    if not contenu or not contenu.strip():

        print(
            f"ERREUR chunk {i} : contenu vide"
        )

        erreurs += 1

    # Vérifier l'embedding
    if len(embedding) != 384:

        print(
            f"ERREUR chunk {i} : "
            f"dimension = {len(embedding)}"
        )

        erreurs += 1

    # Vérifier les métadonnées
    if "article_numero" not in metadata:

        print(
            f"ERREUR chunk {i} : article_numero manquant"
        )

        erreurs += 1

    if "article_titre" not in metadata:

        print(
            f"ERREUR chunk {i} : article_titre manquant"
        )

        erreurs += 1

    if "chunk_index" not in metadata:

        print(
            f"ERREUR chunk {i} : chunk_index manquant"
        )

        erreurs += 1

    if "document" not in metadata:

        print(
            f"ERREUR chunk {i} : document manquant"
        )

        erreurs += 1


# ==================================================
# 11. RESULTAT
# ==================================================

print("\n========================================")

print(
    "Documents testés :",
    len(documents_vectoriels)
)

print(
    "Erreurs :",
    erreurs
)

if erreurs == 0:

    print(
        "\n✅ METADATA QUALITY : PASS"
    )

else:

    print(
        "\n❌ METADATA QUALITY : FAIL"
    )