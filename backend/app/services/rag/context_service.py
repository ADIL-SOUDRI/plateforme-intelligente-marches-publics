class ContextService:

    def construire_contexte(  self,   resultats: list[dict] ) -> str:

        parties = []

        for i, resultat in enumerate( resultats,start=1):

            metadata = resultat["metadata"]

            contenu = resultat["contenu"]

            partie = f"""
--- SOURCE {i} ---

Document : {metadata.get("nom_fichier")}
Type : {metadata.get("type_source")}
Article : {metadata.get("article_numero")}
Titre : {metadata.get("article_titre")}
Distance : {resultat.get("distance")}

Contenu :
{contenu}
"""

            parties.append(partie)

        return "\n".join(parties)