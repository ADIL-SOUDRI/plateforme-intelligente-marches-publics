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


# ==================================================
# FICHIER
# ==================================================

chemin = Path(
    "uploads/documents_references/ccag_fournitures.pdf"
)

print("========== FICHIER ==========")

print(
    "Fichier existe :",
    chemin.exists()
)

if not chemin.exists():
    raise FileNotFoundError(
        f"Fichier introuvable : {chemin}"
    )

print(
    "Taille :",
    chemin.stat().st_size
)


# ==================================================
# 1. EXTRACTION
# ==================================================

extraction_service = DocumentExtractionService()

texte = extraction_service.extraire_texte(
    str(chemin)
)

print("\n========== EXTRACTION ==========")

print(
    "Nombre de caractères :",
    len(texte)
)


# ==================================================
# 2. NETTOYAGE
# ==================================================

cleaning_service = DocumentCleaningService()

texte_propre = cleaning_service.nettoyer(
    texte
)

print("\n========== NETTOYAGE ==========")

print(
    "Nombre de caractères :",
    len(texte_propre)
)


# ==================================================
# 3. STRUCTURE
# ==================================================

structure_service = DocumentStructureService()

texte_document = structure_service.supprimer_sommaire(
    texte_propre
)

print("\n========== STRUCTURE ==========")

print(
    "Nombre de caractères après suppression du sommaire :",
    len(texte_document)
)


# ==================================================
# 4. DETECTION DES ARTICLES
# ==================================================

articles = structure_service.trouver_articles(
    texte_document
)

print("\n========== DETECTION DES ARTICLES ==========")

print(
    "Nombre d'articles détectés :",
    len(articles)
)


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

print("\n========== CHUNKING ==========")

print(
    "Nombre total de chunks :",
    len(chunks)
)


# ==================================================
# 6. AFFICHER LES PREMIERS CHUNKS
# ==================================================

print("\n========== PREMIERS CHUNKS ==========")

for chunk in chunks[:5]:

    print("\n-----------------------------")

    print(
        "Article :",
        chunk["article_numero"]
    )

    print(
        "Titre :",
        chunk["article_titre"]
    )

    print(
        "Chunk :",
        chunk["chunk_index"]
    )

    print(
        "Nombre de caractères :",
        len(chunk["contenu"])
    )

    print("\nContenu :")

    print(
        chunk["contenu"]
    )