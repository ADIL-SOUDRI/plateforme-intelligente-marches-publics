from pathlib import Path

from app.services.document.document_extraction_service import (
    DocumentExtractionService
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

print("\nPremiers caractères :\n")

print(
    texte[:3000]
)