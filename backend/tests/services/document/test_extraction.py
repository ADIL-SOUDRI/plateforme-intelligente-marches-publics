from pathlib import Path

from app.services.document.document_extraction_service import (
    DocumentExtractionService
)

chemin = Path("uploads/documents_references/ccag_fournitures.pdf")


def test_extraction():

    assert chemin.exists(), f"Fichier introuvable : {chemin}"

    service = DocumentExtractionService()

    texte = service.extraire_texte(str(chemin))

    assert texte is not None
    assert len(texte) > 0

    print("\n========== EXTRACTION ==========")
    print("Nombre de caractères :", len(texte))
    print("\nPremiers 3000 caractères :\n")
    print(texte[:3000])