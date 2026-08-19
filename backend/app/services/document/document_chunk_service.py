from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentChunkService:

    def __init__(
        self,
        chunk_size: int = 1500,
        chunk_overlap: int = 200
    ):

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        # self.splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        self.splitter = RecursiveCharacterTextSplitter(

            # encoding_name="cl100k_base",
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                "; ",
                ": ",
                " ",
                ""
            ]
        )

    def decouper_article(self, article: dict) -> list[dict]:

        contenu = article["contenu"]
        numero = article["numero"]
        titre = article["titre"]

        if not contenu or not contenu.strip():
            return []

        # Article suffisamment petit :
        # on conserve l'article entier.
        # if len(contenu) <= self.chunk_size:

            # return [
            #     {
            #         "article_numero": numero,
            #         "article_titre": titre,
            #         "chunk_index": 0,
            #         "contenu": contenu.strip()
            #     }
            # ]

        # Article trop grand :
        # découpage avec LangChain.
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
                    "contenu": morceau.strip()
                }
            )

        return chunks

    def decouper_articles(self,articles: list[dict]) -> list[dict]:

        chunks = []

        for article in articles:

            chunks = self.decouper_article(article)

            chunks.extend(chunks)

        return chunks