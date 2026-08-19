from app.services.document.vector_store_service import (
    VectorStoreService
)

vector_service = VectorStoreService()

vector_service.ajouter_chunks(
    chunks,
    embeddings
)

print("Chunks enregistrés dans ChromaDB :", len(chunks))