# from sentence_transformers import SentenceTransformer


# class EmbeddingService:

#     def __init__(self):
#         self.model = SentenceTransformer(
#             "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
#         )

#     def generer_embedding(self, texte: str):

#         if not texte or not texte.strip():
#             return []

#         return self.model.encode(
#             texte,
#             convert_to_numpy=True
#         ).tolist()

#     def generer_embeddings(self, textes: list[str]):

#         if not textes:
#             return []

#         return self.model.encode(textes,convert_to_numpy=True).tolist()
from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self):

        self.model = SentenceTransformer(
            "BAAI/bge-m3"
        )


    def generer_embedding(
        self,
        texte: str
    ):

        if not texte or not texte.strip():

            return []

        return self.model.encode(
            texte,
            normalize_embeddings=True
        ).tolist()


    def generer_embeddings(
        self,
        textes: list[str]
    ):

        if not textes:

            return []

        return self.model.encode(
            textes,
            normalize_embeddings=True
        ).tolist()