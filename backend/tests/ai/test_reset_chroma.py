import chromadb


client = chromadb.PersistentClient(
    path="chroma_db"
)

try:
    client.delete_collection(
        name="documents_publics"
    )

    print("Collection supprimée.")

except Exception:
    print("Collection inexistante.")


collection = client.get_or_create_collection(
    name="documents_publics"
)

print("Collection recréée.")