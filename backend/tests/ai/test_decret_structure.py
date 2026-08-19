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


# ==================================================
# FICHIER
# ==================================================

chemin = Path(
    "uploads/documents_references/decret_marches_publics.pdf"
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

texte_document = (
    structure_service.supprimer_sommaire(
        texte_propre
    )
)

print("\n========== STRUCTURE ==========")

print(
    "Nombre de caractères après suppression du sommaire :",
    len(texte_document)
)


# ==================================================
# 4. DÉTECTION DES ARTICLES
# ==================================================

articles = structure_service.trouver_articles(
    texte_document
)

print("\n========== ARTICLES ==========")

print(
    "Nombre d'articles détectés :",
    len(articles)
)


# ==================================================
# 5. AFFICHER LES PREMIERS ARTICLES
# ==================================================

for article in articles[:10]:

    print("\n--------------------------------")

    print(
        "Numéro :",
        article["numero"]
    )

    print(
        "Titre :",
        article["titre"]
    )

    print(
        "Contenu :"
    )

    print(
        article["contenu"][:500]
    )


# ==================================================
# 6. AFFICHER LES DERNIERS ARTICLES
# ==================================================

print("\n========== DERNIERS ARTICLES ==========")

for article in articles[-5:]:

    print("\n--------------------------------")

    print(
        "Numéro :",
        article["numero"]
    )

    print(
        "Titre :",
        article["titre"]
    )
print("\n========== ARTICLES ==========")

print(
    "Nombre d'articles détectés :",
    len(articles)
)