# import chromadb

# from app.services.document.embedding_service import EmbeddingService


# class VectorSearchService:

#     def __init__(self):

#         self.client = chromadb.PersistentClient(
#             path="chroma_db"
#         )

#         self.collection = self.client.get_collection(
#             name="documents_publics"
#         )

#         self.embedding_service = EmbeddingService()

#     def rechercher(
#         self,
#         question: str,
#         nombre_resultats: int = 5
#     ):

#         # 1. Générer l'embedding de la question
#         embedding_question = (
#             self.embedding_service.generer_embedding(
#                 question
#             )
#         )

#         resultats = self.collection.query(
#             query_embeddings=[embedding_question],
#             n_results=5,
#             where={
#                 "document_id": "9"
#             }
#         )

#         # 2. Rechercher dans ChromaDB
#         # resultats = self.collection.query(
#         #     query_embeddings=[embedding_question],
#         #     n_results=nombre_resultats
#         # )

#         return resultats


import chromadb

from app.services.document.embedding_service import (
    EmbeddingService
)


class VectorSearchService:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="chroma_db"
        )

        self.collection = self.client.get_collection(
            name="documents_publics"
        )

        self.embedding_service = EmbeddingService()

    def rechercher( self, question: str,top_k: int = 5,document_id: str | None = None ):

        

        embedding = (self.embedding_service.generer_embedding(question))

       

        where = None

        if document_id is not None:

            where = {
                "document_id": str(document_id)
            }

        
        resultats = self.collection.query( query_embeddings=[embedding],n_results=top_k,where=where)

        return resultats
   

    def filtrer_resultats(self,resultats, distance_max: float = 10.0 ):

        documents = resultats["documents"][0]
        metadatas = resultats["metadatas"][0]
        distances = resultats["distances"][0]

        resultats_filtres = []

        for document, metadata, distance in zip(documents,  metadatas, distances):

            if distance <= distance_max:

                resultats_filtres.append({

                    "contenu": document,

                    "metadata": metadata,

                    "distance": distance})

        return resultats_filtres