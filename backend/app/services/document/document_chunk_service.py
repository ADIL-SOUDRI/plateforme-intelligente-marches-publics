# # from langchain_text_splitters import RecursiveCharacterTextSplitter


# # class DocumentChunkService:

# #     def __init__(
# #         self,
# #         chunk_size: int = 1500,
# #         chunk_overlap: int = 250
# #     ):

# #         self.chunk_size = chunk_size
# #         self.chunk_overlap = chunk_overlap

# #         # self.splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
# #         self.splitter = RecursiveCharacterTextSplitter(

# #             # encoding_name="cl100k_base",
# #             chunk_size=chunk_size,
# #             chunk_overlap=chunk_overlap,
# #             separators=[
# #                 "\n\n",
# #                 "\n",
# #                 ". ",
# #                 "; ",
# #                 ": ",
# #                 " ",
# #                 ""
# #             ]
# #         )

# #     def decouper_article(self, article: dict) -> list[dict]:

# #         contenu = article["contenu"]
# #         numero = article["numero"]
# #         titre = article["titre"]

# #         if not contenu or not contenu.strip():
# #             return []

# #         # Article suffisamment petit :
# #         # on conserve l'article entier.
# #         # if len(contenu) <= self.chunk_size:

# #             # return [
# #             #     {
# #             #         "article_numero": numero,
# #             #         "article_titre": titre,
# #             #         "chunk_index": 0,
# #             #         "contenu": contenu.strip()
# #             #     }
# #             # ]

# #         # Article trop grand :
# #         # découpage avec LangChain.
# #         morceaux = self.splitter.split_text(
# #             contenu
# #         )

# #         chunks = []

# #         for index, morceau in enumerate(morceaux):

# #             chunks.append(
# #                 {
# #                     "article_numero": numero,
# #                     "article_titre": titre,
# #                     "chunk_index": index,
# #                     "contenu": morceau.strip()
# #                 }
# #             )

# #         return chunks

# #     def decouper_articles(
# #     self,
# #     articles: list[dict]
# #     ) -> list[dict]:

# #         chunks = []

# #         for article in articles:

# #             chunks_article = self.decouper_article(
# #                 article
# #             )

# #             chunks.extend(chunks_article)

# #         return chunks
# import re
# from langchain_text_splitters import RecursiveCharacterTextSplitter


# class DocumentChunkService:

#     def __init__(
#         self,
#         chunk_size: int = 1500,
#         chunk_overlap: int = 200
#     ):
#         self.chunk_size = chunk_size
#         self.chunk_overlap = chunk_overlap

#         self.splitter = RecursiveCharacterTextSplitter(
#             chunk_size=chunk_size,
#             chunk_overlap=chunk_overlap,
#             separators=[
#                 "\n\nART.",
#                 "\n\nArticle",
#                 "\n\n",
#                 "\n",
#                 ". ",
#                 "; ",
#                 " ",
#                 ""
#             ]
#         )

#     def _extraire_vrai_numero_article(self, texte: str, fallback_numero: str) -> str:
#         """
#         Détecte si un en-tête d'article spécifique est présent dans le texte du chunk
#         pour corriger les incohérences transmises en amont.
#         """
#         match = re.search(r'(?i)\bART(?:ICLE)?\b[\s\.\-]+?(\d+)', texte)
#         if match:
#             return match.group(1)
#         return fallback_numero

#     def decouper_article(self, article: dict) -> list[dict]:
#         contenu = article.get("contenu", "")
#         numero = str(article.get("numero", "Inconnu"))
#         titre = article.get("titre", "")

#         if not contenu or not contenu.strip():
#             return []

#         morceaux = self.splitter.split_text(contenu.strip())
#         chunks = []

#         for index, morceau in enumerate(morceaux):
#             morceau_clean = morceau.strip()
            
#             real_numero = self._extraire_vrai_numero_article(morceau_clean, fallback_numero=numero)
#             real_titre = f"Article {real_numero}:" if real_numero != numero else titre

#             chunks.append(
#                 {
#                     "article_numero": real_numero,
#                     "article_titre": real_titre,
#                     "chunk_index": index,
#                     "contenu": morceau_clean
#                 }
#             )

#         return chunks

#     def decouper_articles(self, articles: list[dict]) -> list[dict]:
#         chunks = []
#         for article in articles:
#             chunks.extend(self.decouper_article(article))
#         return chunks
from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentChunkService:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=2500,
            chunk_overlap=300,
            separators=[
                "\n\n",
                "\n",
                ". ",
                "; ",
                " ",
                ""
            ]
        )

    def decouper_article(
        self,
        article: dict
    ) -> list[dict]:

        contenu = article.get("contenu", "").strip()

        if not contenu:
            return []

        numero = str(
            article.get("numero", "Inconnu")
        )

        titre = article.get(
            "titre",
            ""
        )

        page = article.get("page")

        # Article court :
        # on garde tout l'article
        if len(contenu) <= 2500:

            return [
                {
                    "article_numero": numero,
                    "article_titre": titre,
                    "chunk_index": 0,
                    "page": page,
                    "contenu": contenu
                }
            ]

        # Article long
        morceaux = self.splitter.split_text(
            contenu
        )

        chunks = []

        for index, morceau in enumerate(morceaux):

            chunks.append(
                {
                    "article_numero": numero,
                    "article_titre": titre,
                    "chunk_index": index,
                    "page": page,
                    "contenu": morceau.strip()
                }
            )

        return chunks

    def decouper_articles(
        self,
        articles: list[dict]
    ) -> list[dict]:

        chunks = []

        for article in articles:

            chunks.extend(
                self.decouper_article(article)
            )

        return chunks