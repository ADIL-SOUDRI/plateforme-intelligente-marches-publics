import chromadb


class VectorStoreService:

    def __init__(self):

        self.client = chromadb.PersistentClient( path="chroma_db")

        self.collection = self.client.get_or_create_collection(name="documents_publics")

    def ajouter_chunks( self, chunks: list[dict],   embeddings: list[list[float]],  document_id: int,  nom_fichier: str,type_source: str = "reference"):

        ids = []
        documents = []
        metadatas = []

        for i, chunk in enumerate(chunks):

            ids.append(  f"document_{document_id}_chunk_{i}")

            documents.append(chunk["contenu"] )

            metadatas.append({

                
                "document_id": str(document_id),
                "nom_fichier": nom_fichier,
                "type_source": type_source,

               
                "article_numero": str( chunk["article_numero"]),

                "article_titre": str(  chunk["article_titre"] ),

                
                "chunk_index": int(  chunk["chunk_index"] )
            })

        self.collection.add(ids=ids, documents=documents, embeddings=embeddings, metadatas=metadatas )