import chromadb


client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_collection(
    name="documents_publics"
)

resultat = collection.get(
    limit=5,
    include=[
        "documents",
        "metadatas"
    ]
)

print("\n========== TEST CHROMADB ==========\n")

print(
    "Nombre total :",
    collection.count()
)

for i in range(len(resultat["ids"])):

    print("\n--------------------------------")

    print(
        "ID :",
        resultat["ids"][i]
    )

    print(
        "Metadata :",
        resultat["metadatas"][i]
    )

    print(
        "Contenu :",
        resultat["documents"][i][:200]
    )