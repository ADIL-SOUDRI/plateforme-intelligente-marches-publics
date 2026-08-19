from app.services.document.vector_search_service import VectorSearchService
from app.services.rag.context_service import ContextService
from app.services.rag.generation_service import GenerationService


class RAGService:

    def __init__(self):
        self.vector_search_service = VectorSearchService()
        self.context_service = ContextService()
        self.generation_service = GenerationService()

    def repondre(self, question: str, document_id: str | None = None):

        resultats = self.vector_search_service.rechercher(question=question,  top_k=5,document_id=document_id )

        resultats_filtres = (
            self.vector_search_service.filtrer_resultats(resultats,distance_max=12.0 )
        )

        contexte = self.context_service.construire_contexte( resultats_filtres)

        reponse = self.generation_service.generer_reponse(question=question, contexte=contexte)

        return {"question": question,"reponse": reponse,
            "sources": [
                resultat["metadata"]
                for resultat in resultats_filtres
            ]
        }