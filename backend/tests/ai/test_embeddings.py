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
from app.services.document.vector_store_service import (
    VectorStoreService
)

chemin = Path(
    "uploads/documents_references/ccag_fournitures.pdf"
)


# ==============================
# 1. EXTRACTION
# ==============================

extraction_service = DocumentExtractionService()

texte = extraction_service.extraire_texte(
    str(chemin)
)


# ==============================
# 2. NETTOYAGE
# ==============================

cleaning_service = DocumentCleaningService()

texte_propre = cleaning_service.nettoyer(
    texte
)


# ==============================
# 3. STRUCTURE
# ==============================

structure_service = DocumentStructureService()

texte_document = structure_service.supprimer_sommaire(
    texte_propre
)


# ==============================
# 4. ARTICLES
# ==============================

articles = structure_service.trouver_articles(
    texte_document
)


# ==============================
# 5. CHUNKS
# ==============================

chunk_service = DocumentChunkService(
    chunk_size=1500,
    chunk_overlap=200
)

chunks = chunk_service.decouper_articles(
    articles
)

print("Nombre de chunks :", len(chunks))


# ==============================
# 6. EMBEDDINGS
# ==============================

embedding_service = EmbeddingService()

textes = [
    chunk["contenu"]
    for chunk in chunks
]

embeddings = embedding_service.generer_embeddings(
    textes
)


print("\n========== EMBEDDINGS ==========")

print("Nombre d'embeddings :", len(embeddings))

if embeddings:

    print(
        "Dimension :",
        len(embeddings[0])
    )

    print(
        "Premier embedding :",
        embeddings[0][:5]
    )


vector_service = VectorStoreService()

vector_service.ajouter_chunks(
    chunks=chunks,
    embeddings=embeddings,
    document_id=9,
    nom_fichier="ccag_fournitures.pdf",
    type_source="CCAG"
)

print("Chunks enregistrés dans ChromaDB :", len(chunks))
print(
    "Nombre dans ChromaDB :",
    vector_service.collection.count()
)