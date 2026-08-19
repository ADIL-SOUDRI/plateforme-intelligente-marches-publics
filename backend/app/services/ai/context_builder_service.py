class ContextBuilderService:

    def construire(self,resultats: dict) -> str:

        documents = resultats["documents"][0]
        metadatas = resultats["metadatas"][0]

        parties = []

        for document, metadata in zip(documents, metadatas):

            nom_fichier = metadata.get( "nom_fichier", "")

            article_numero = metadata.get( "article_numero","")

            article_titre = metadata.get("article_titre","")

            partie = f"""
[Document : {nom_fichier}]
[Article : {article_numero}]
[Titre : {article_titre}]

{document}
"""

            parties.append(partie.strip())

        return "\n\n".join(parties)