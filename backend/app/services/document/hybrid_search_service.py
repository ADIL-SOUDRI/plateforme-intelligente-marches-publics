import re

from rank_bm25 import BM25Okapi

from app.services.document.vector_search_service import (
    VectorSearchService
)


class HybridSearchService:

    def __init__(self):

        self.vector_search_service = (
            VectorSearchService()
        )

        self.collection = (
            self.vector_search_service.collection
        )

    # ==================================================
    # TOKENISATION BM25
    # ==================================================

    def _tokeniser(self, texte: str):

        return re.findall(
            r"\b\w+\b",
            texte.lower()
        )

    # ==================================================
    # RECHERCHE BM25
    # ==================================================

    def recherche_bm25(
        self,
        question: str,
        top_k: int = 20
    ):

        data = self.collection.get()

        documents = data.get(
            "documents",
            []
        )

        metadatas = data.get(
            "metadatas",
            []
        )

        ids = data.get(
            "ids",
            []
        )

        if not documents:
            return []

        corpus = [
            self._tokeniser(document)
            for document in documents
        ]

        bm25 = BM25Okapi(
            corpus
        )

        query_tokens = self._tokeniser(
            question
        )

        scores = bm25.get_scores(
            query_tokens
        )

        indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )[:top_k]

        resultats = []

        for index in indices:

            if scores[index] <= 0:
                continue

            resultats.append({

                "id": ids[index],

                "contenu":
                    documents[index],

                "metadata":
                    metadatas[index],

                "bm25_score":
                    float(scores[index])
            })

        return resultats

    # ==================================================
    # RECHERCHE VECTORIELLE
    # ==================================================

    def recherche_vectorielle(
        self,
        question: str,
        top_k: int = 20,
        document_id: str | None = None
    ):

        resultats = (
            self.vector_search_service.rechercher(
                question=question,
                top_k=top_k,
                document_id=document_id
            )
        )

        return (
            self.vector_search_service
            .filtrer_resultats(resultats)
        )

    # ==================================================
    # RECHERCHE HYBRIDE
    # ==================================================

    def rechercher(
        self,
        question: str,
        top_k: int = 20,
        document_id: str | None = None
    ):

        # ------------------------------------------
        # 1. Recherche vectorielle
        # ------------------------------------------

        resultats_vectoriels = (
            self.recherche_vectorielle(
                question,
                top_k,
                document_id
            )
        )

        # ------------------------------------------
        # 2. Recherche BM25
        # ------------------------------------------

        resultats_bm25 = (
            self.recherche_bm25(
                question,
                top_k
            )
        )

        # ------------------------------------------
        # 3. Fusion
        # ------------------------------------------

        fusion = {}

        # ==========================================
        # VECTORIEL
        # ==========================================

        for rang, resultat in enumerate(
            resultats_vectoriels,
            start=1
        ):

            id_ = resultat["id"]

            score = 1 / rang

            if id_ not in fusion:

                fusion[id_] = {

                    "id": id_,

                    "contenu":
                        resultat["contenu"],

                    "metadata":
                        resultat["metadata"],

                    "score_vectoriel": 0.0,

                    "score_bm25": 0.0,

                    "score_final": 0.0
                }

            fusion[id_]["score_vectoriel"] = score

        # ==========================================
        # BM25
        # ==========================================

        for rang, resultat in enumerate(
            resultats_bm25,
            start=1
        ):

            id_ = resultat["id"]

            score = 1 / rang

            if id_ not in fusion:

                fusion[id_] = {

                    "id": id_,

                    "contenu":
                        resultat["contenu"],

                    "metadata":
                        resultat["metadata"],

                    "score_vectoriel": 0.0,

                    "score_bm25": 0.0,

                    "score_final": 0.0
                }

            fusion[id_]["score_bm25"] = score

        # ==========================================
        # SCORE FINAL
        # ==========================================

        for resultat in fusion.values():

            resultat["score_final"] = (

                0.6 *
                resultat["score_vectoriel"]

                +

                0.4 *
                resultat["score_bm25"]
            )

        # ==========================================
        # TRI
        # ==========================================

        resultats = sorted(
            fusion.values(),
            key=lambda x: x["score_final"],
            reverse=True
        )

        return resultats[:top_k]