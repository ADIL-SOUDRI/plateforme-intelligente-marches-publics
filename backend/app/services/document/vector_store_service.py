# import chromadb


# class VectorStoreService:

#     def __init__(self):

#         self.client = chromadb.PersistentClient( path="chroma_db")

#         self.collection = self.client.get_or_create_collection(name="documents_publics")

#     def ajouter_chunks( self, chunks: list[dict],   embeddings: list[list[float]],  document_id: int,  nom_fichier: str,type_source: str = "reference"):

#         ids = []
#         documents = []
#         metadatas = []

#         for i, chunk in enumerate(chunks):

#             ids.append(  f"document_{document_id}_chunk_{i}")

#             documents.append(chunk["contenu"] )

#         #     metadatas.append({

                
#         #         "document_id": str(document_id),
#         #         "nom_fichier": nom_fichier,
#         #         "type_source": type_source,

               
#         #         "article_numero": str( chunk["article_numero"]),

#         #         "article_titre": str(  chunk["article_titre"] ),

                
#         #         "chunk_index": int(  chunk["chunk_index"] )
#         #     })

#         # self.collection.add(ids=ids, documents=documents, embeddings=embeddings, metadatas=metadatas )
#             metadata = {
#                     "document_id": str(document_id),
#                     "nom_fichier": nom_fichier,
#                     "type_source": type_source,

#                     "article_numero": str(
#                         chunk.get("article_numero", "")
#                     ),

#                     "article_titre": str(
#                         chunk.get("article_titre", "")
#                     ),

#                     "chunk_index": int(
#                         chunk.get("chunk_index", i)
#                     )
#                 }


#             if chunk.get("page") is not None:
#                     metadata["page"] = int(chunk["page"])

#             metadatas.append(metadata)

#         self.collection.add(
#                 ids=ids,
#                 documents=documents,
#                 embeddings=embeddings,
#                 metadatas=metadatas
#         )
import chromadb


class VectorStoreService:

    def __init__(self):

        # self.client = chromadb.PersistentClient(
        #     path="chroma_db"
        # )
        self.client = chromadb.HttpClient(
            host="localhost",
            port=8002
        )

        self.collection = (
            self.client.get_or_create_collection(
                name="documents_publics"
            )
        )

    def ajouter_chunks(
        self,
        chunks: list[dict],
        embeddings: list[list[float]],
        document_id: int,
        nom_fichier: str,
        domaine: str,
        type_source: str = "reference"
    ):

        ids = []
        documents = []
        metadatas = []

        for i, chunk in enumerate(chunks):

            ids.append(
                f"document_{document_id}_chunk_{i}"
            )

            article_numero = str(
                chunk.get(
                    "article_numero",
                    ""
                )
            )

            article_titre = str(
                chunk.get(
                    "article_titre",
                    ""
                )
            )

            contenu = chunk.get(
                "contenu",
                ""
            )

            # Texte utilisé pour la recherche vectorielle
            embedding_text = f"""
            Document : {nom_fichier}

            Article : {article_numero}

            Titre de l'article : {article_titre}

            Contenu :
            {contenu}
            """.strip()

            documents.append(
                embedding_text
            )

            metadata = {

                "document_id": str(
                    document_id
                ),

                "nom_fichier": nom_fichier,

                "type_source": type_source,
                "domaine": domaine,

                "article_numero":
                    article_numero,

                "article_titre":
                    article_titre,

                "chunk_index":
                    int(
                        chunk.get(
                            "chunk_index",
                            i
                        )
                    )
            }

            if chunk.get("page") is not None:

                metadata["page"] = int(
                    chunk["page"]
                )

            metadatas.append(metadata)

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )
    def obtenir_tous_chunks(self):

        resultats = self.collection.get(
            include=[
                "documents",
                "metadatas"
            ]
        )

        return resultats