from app.services.document.document_extraction_service import (DocumentExtractionService)
from app.services.document.document_cleaning_service import (DocumentCleaningService)
from app.services.document.document_structure_service import ( DocumentStructureService)
from app.services.document.document_chunk_service import ( DocumentChunkService)
from app.services.document.embedding_service import (EmbeddingService)
from app.services.document.vector_store_service import ( VectorStoreService)
from app.services.ml.classifier_service import (
    ClassifierService
)

class DocumentIndexationService:

    def __init__(self):
        self.extraction_service = DocumentExtractionService()
        self.cleaning_service = DocumentCleaningService()
        self.structure_service = DocumentStructureService()
        self.chunk_service = DocumentChunkService()
        self.embedding_service = EmbeddingService()
        self.classifier_service = ClassifierService()
        self.vector_store_service = VectorStoreService()


    # ==================================================
    # INDEXATION COMPLETE D'UN DOCUMENT
    # ==================================================

    def indexer_document(
        self,
        chemin_fichier: str,
        document_id: int,
        type_source: str,
        nom_fichier: str
    ):

        print("\n")
        print("=" * 60)
        print("DEBUT INDEXATION DOCUMENT")
        print("=" * 60)

        print("Fichier :", nom_fichier)
        print("Document ID :", document_id)
        print("Type source :", type_source)


        # ==================================================
        # 1. EXTRACTION
        # ==================================================

        print("\n[1/6] EXTRACTION")

        texte = self.extraction_service.extraire_texte(
            chemin_fichier
        )

        if not texte or not texte.strip():

            raise ValueError(
                "Aucun texte n'a été extrait du document."
            )

        print(
            "Nombre caractères :",
            len(texte)
        )


        # ==================================================
        # 2. NETTOYAGE
        # ==================================================

        print("\n[2/6] NETTOYAGE")

        texte_propre = (
            self.cleaning_service.nettoyer(
                texte
            )
        )

        print(
            "Nombre caractères après nettoyage :",
            len(texte_propre)
        )


        # ==================================================
        # 3. STRUCTURATION
        # ==================================================

        print("\n[3/6] STRUCTURATION")

        texte_structure = (
            self.structure_service.supprimer_sommaire(
                texte_propre
            )
        )

        articles = (
            self.structure_service.trouver_articles(
                texte_structure
            )
        )

        print(
            "Nombre articles :",
            len(articles)
        )

        if not articles:

            raise ValueError(
                "Aucun article détecté dans le document."
            )
        # texte_classification = texte_structure[:5000]
        classification = self.classifier_service.classifier(
            texte_structure
        )

        domaine = classification["domaine"]
        confiance = classification["confiance"]

        print("\n========== CLASSIFICATION ML ==========")

        print(
            "Domaine :",
            domaine
        )

        print(
            "Confiance :",
            confiance
        )

        # ==================================================
        # 4. CHUNKING
        # ==================================================

        print("\n[4/6] CHUNKING")

        chunks = (
            self.chunk_service.decouper_articles(
                articles
            )
        )

        # print(
        #     "Nombre chunks :",
        #     len(chunks)
        # )
        print("\n" + "=" * 70)
        print("CHUNKS")
        print("=" * 70)

        for i, chunk in enumerate(chunks, start=1):

            print(
                f"Chunk {i} | "
                f"Article {chunk.get('article_numero')} | "
                f"Page {chunk.get('page')} | "
                f"Taille {len(chunk.get('contenu', ''))}"
            )

        if not chunks:

            raise ValueError(
                "Aucun chunk généré."
            )


        # ==================================================
        # 5. EMBEDDINGS
        # ==================================================

        print("\n[5/6] EMBEDDINGS")

        # textes_chunks = [
        #     chunk["contenu"]
        #     for chunk in chunks
        # ]
        textes_chunks = []

        for chunk in chunks:

            embedding_text = f"""
        Document : {nom_fichier}

        Chapitre : {chunk.get("chapitre", "")}

        Section : {chunk.get("section", "")}

        Article : {chunk.get("article_numero", "")}

        Titre de l'article : {chunk.get("article_titre", "")}

        Contenu :
        {chunk.get("contenu", "")}
        """.strip()

            # conserver le texte utilisé pour l'embedding
            chunk["embedding_text"] = embedding_text

            textes_chunks.append(
                embedding_text
            )

        embeddings = (
            self.embedding_service.generer_embeddings(
                textes_chunks
            )
        )

        print(
            "Nombre embeddings :",
            len(embeddings)
        )

        if len(embeddings) != len(chunks):

            raise ValueError(
                "Le nombre d'embeddings est différent "
                "du nombre de chunks."
            )


        # ==================================================
        # 6. CHROMADB
        # ==================================================

        print("\n[6/6] CHROMADB")

        self.vector_store_service.ajouter_chunks(

            chunks=chunks,

            embeddings=embeddings,

            document_id=document_id,
            domaine=domaine,
            nom_fichier=nom_fichier,

            type_source=type_source
        )


        # ==================================================
        # FIN
        # ==================================================

        print("\n")
        print("=" * 60)
        print("DOCUMENT INDEXE AVEC SUCCES")
        print("=" * 60)

        # return {

        #     "document_id": document_id,

        #     "nom_fichier": nom_fichier,

        #     "type_source": type_source,

        #     "nombre_articles": len(articles),

        #     "nombre_chunks": len(chunks),

        #     "nombre_embeddings": len(embeddings)

        # }
        return {
            "document_id": document_id,
            "nom_fichier": nom_fichier,
            "type_source": type_source,
            "domaine": domaine,
            "confiance": confiance,
            "nombre_articles": len(articles),
            "nombre_chunks": len(chunks),
            "nombre_embeddings": len(embeddings)
        }