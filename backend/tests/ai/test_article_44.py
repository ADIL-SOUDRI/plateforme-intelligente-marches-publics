# from app.services.document.vector_store_service import VectorStoreService


# vector_store = VectorStoreService()

# resultats = vector_store.collection.get(
#     where={
#         "article_numero": "44"
#     },
#     include=[
#         "documents",
#         "metadatas"
#     ]
# )

# print("\n")
# print("=" * 80)
# print("TEST ARTICLE 44")
# print("=" * 80)

# documents = resultats.get("documents", [])
# metadatas = resultats.get("metadatas", [])
# ids = resultats.get("ids", [])

# for i, (doc, metadata, id_) in enumerate(
#     zip(documents, metadatas, ids)
# ):

#     print("\n")
#     print("-" * 80)

#     print("ID :", id_)

#     print(
#         "Document :",
#         metadata.get("nom_fichier")
#     )

#     print(
#         "Article :",
#         metadata.get("article_numero")
#     )

#     print(
#         "Titre :",
#         metadata.get("article_titre")
#     )

#     print(
#         "Page :",
#         metadata.get("page")
#     )

#     print("\nCONTENU :\n")

#     print(doc)

#     print("\n")


from app.services.document.vector_store_service import VectorStoreService


vector_store = VectorStoreService()

resultats = vector_store.collection.get(
    include=[
        "documents",
        "metadatas"
    ]
)

for i in range(
    min(10, len(resultats["ids"]))
):

    print("\n==============================")

    print(
        "ID :",
        resultats["ids"][i]
    )

    print(
        "Document :",
        resultats["metadatas"][i].get(
            "nom_fichier"
        )
    )

    print(
        "Article :",
        resultats["metadatas"][i].get(
            "article_numero"
        )
    )

    print(
        "Titre :",
        resultats["metadatas"][i].get(
            "article_titre"
        )
    )

    print(
        "Page :",
        resultats["metadatas"][i].get(
            "page"
        )
    )