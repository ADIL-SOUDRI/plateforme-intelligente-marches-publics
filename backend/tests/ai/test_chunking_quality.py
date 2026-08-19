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
# 6. TEST DES ARTICLES LONGS
# ==================================================

print("\n========== ARTICLES LONGS ==========")

for article in articles:

    longueur = len(article["contenu"])

    if longueur > 1500:

        print(
            f"Article {article['numero']} : "
            f"{longueur} caractères"
        )


# ==================================================
# 7. TEST DES CHUNKS PAR ARTICLE
# ==================================================

print("\n========== CHUNKS ARTICLES LONGS ==========")

for article in articles:

    longueur = len(article["contenu"])

    if longueur > 1500:

        chunks_article = chunk_service.decouper_article(
            article
        )

        print(
            f"\nArticle {article['numero']} "
            f"({longueur} caractères)"
        )

        print(
            "Nombre de chunks :",
            len(chunks_article)
        )

        for chunk in chunks_article:

            print(
                f"  Chunk {chunk['chunk_index']} : "
                f"{len(chunk['contenu'])} caractères"
            )


# ==================================================
# 8. TEST QUALITE DU CHUNKING
# ==================================================

print("\n========== TEST QUALITE DU CHUNKING ==========")

ERREURS = 0
ARTICLES_TESTES = 0
CHUNKS_TESTES = 0

for article in articles:

    chunks_article = chunk_service.decouper_article(article)

    ARTICLES_TESTES += 1
    CHUNKS_TESTES += len(chunks_article)

    # ----------------------------------------------
    # TEST 1 : METADONNEES
    # ----------------------------------------------

    for i, chunk in enumerate(chunks_article):

        if chunk["article_numero"] != article["numero"]:
            print(
                f"❌ Erreur métadonnée article "
                f"{article['numero']} - chunk {i}"
            )
            ERREURS += 1

        if chunk["article_titre"] != article["titre"]:
            print(
                f"❌ Erreur titre article "
                f"{article['numero']} - chunk {i}"
            )
            ERREURS += 1

        if chunk["chunk_index"] != i:
            print(
                f"❌ Mauvais index article "
                f"{article['numero']} - "
                f"attendu={i}, obtenu={chunk['chunk_index']}"
            )
            ERREURS += 1

    # ----------------------------------------------
    # TEST 2 : CHUNKS VIDES
    # ----------------------------------------------

    for chunk in chunks_article:

        contenu = chunk["contenu"].strip()

        if not contenu:
            print(
                f"❌ Chunk vide "
                f"article {article['numero']}"
            )
            ERREURS += 1

    # ----------------------------------------------
    # TEST 3 : OVERLAP
    # ----------------------------------------------

    for i in range(len(chunks_article) - 1):

        courant = chunks_article[i]["contenu"]
        suivant = chunks_article[i + 1]["contenu"]

        # On cherche une partie commune à la fin
        # du chunk courant et au début du suivant.

        overlap_trouve = False

        longueur_max = min(
            200,
            len(courant),
            len(suivant)
        )

        for taille in range(
            longueur_max,
            0,
            -1
        ):

            fin_courant = courant[-taille:]
            debut_suivant = suivant[:taille]

            if fin_courant == debut_suivant:

                overlap_trouve = True
                break

        if not overlap_trouve:

            print(
                f"⚠️ Overlap non détecté : "
                f"article {article['numero']} "
                f"chunk {i} → chunk {i + 1}"
            )

    # ----------------------------------------------
    # TEST 4 : AFFICHAGE RESUME
    # ----------------------------------------------

    if len(chunks_article) > 1:

        print(
            f"✓ Article {article['numero']} : "
            f"{len(chunks_article)} chunks"
        )


# ==================================================
# RESULTAT
# ==================================================

print("\n========================================")

print(
    "Articles testés :",
    ARTICLES_TESTES
)

print(
    "Chunks testés :",
    CHUNKS_TESTES
)

print(
    "Erreurs :",
    ERREURS
)

if ERREURS == 0:

    print(
        "\n✅ CHUNKING QUALITY : PASS"
    )

else:

    print(
        "\n❌ CHUNKING QUALITY : FAIL"
    )