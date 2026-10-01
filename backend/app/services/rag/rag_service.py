# from app.services.document.vector_search_service import VectorSearchService
# from app.services.rag.context_service import ContextService
# from app.services.rag.generation_service import GenerationService


# class RAGService:

#     def __init__(self):
#         self.vector_search_service = VectorSearchService()
#         self.context_service = ContextService()
#         self.generation_service = GenerationService()

#     def repondre(self, question: str, document_id: str | None = None):

#         resultats = self.vector_search_service.rechercher(question=question,  top_k=20)#document_id=document_id 

#         resultats_filtres = (
#             self.vector_search_service.filtrer_resultats(resultats ) #,distance_max=12.0
#         )

#         contexte = self.context_service.construire_contexte( resultats_filtres)

#         reponse = self.generation_service.generer_reponse(question=question, contexte=contexte)

#         return {"question": question,"reponse": reponse,
#             "sources": [
#                 resultat["metadata"]
#                 for resultat in resultats_filtres
#             ]
#         }
from app.services.document.hybrid_search_service import (
    HybridSearchService
)

from app.services.rag.context_service import (
    ContextService
)

from app.services.rag.generation_service import (
    GenerationService
)
# from app.services.ai.reranker_service import (
#     RerankerService
# )

class RAGService:

    def __init__(self):

        self.hybrid_search_service = (
            HybridSearchService()
        )

        self.context_service = (
            ContextService()
        )

        self.generation_service = (
            GenerationService()
        )
        # self.reranker_service = (
        # RerankerService()
        # )

    def repondre(
        self,
        question: str
    ):

        # ==========================
        # 1. RECHERCHE HYBRIDE
        # ==========================

        resultats_hybrides = (
            self.hybrid_search_service.rechercher(
                question=question,
                top_k=5
                # top_k=20

            )
        )

        print(
            "\nRESULTATS RECHERCHE HYBRIDE :",
            len(resultats_hybrides)
        )

        for i, resultat in enumerate(
            resultats_hybrides,
            start=1
        ):

            metadata = resultat[
                "metadata"
            ]

            print(
                f"\n--- RESULTAT {i} ---"
            )

            print(
                "Document :",
                metadata.get(
                    "nom_fichier"
                )
            )

            print(
                "Article :",
                metadata.get(
                    "article_numero"
                )
            )

            print(
                "Titre :",
                metadata.get(
                    "article_titre"
                )
            )

            print(
                "Page :",
                metadata.get(
                    "page"
                )
            )

            print(
                "Score :",
                resultat.get(
                    "score"
                )
            )

        # resultats_rerankes = (
        #             self.reranker_service.reranker(
        #                 question=question,
        #                 resultats=resultats_hybrides,
        #                 top_k=5
        #             )
        #         )


        # print(
        #     "\n=============================="
        # )

        # print(
        #     "RESULTATS APRÈS RERANKING :",
        #     len(resultats_rerankes)
        # )
        # ==========================
        # 2. CONSTRUIRE CONTEXTE
        # ==========================

        contexte = (
            self.context_service
            .construire_contexte(
                resultats_hybrides
            )
        )

        # ==========================
        # 3. GENERATION LLM
        # ==========================

        reponse = (
            self.generation_service
            .generer_reponse(
                question=question,
                contexte=contexte
            )
        )

        return {

            "reponse": reponse,

            "sources": [
                {
                    "document":
                        r["metadata"].get(
                            "nom_fichier"
                        ),

                    "article":
                        r["metadata"].get(
                            "article_numero"
                        ),

                    "titre":
                        r["metadata"].get(
                            "article_titre"
                        ),

                    "page":
                        r["metadata"].get(
                            "page"
                        )
                }

                for r in resultats_hybrides
            ]
        }