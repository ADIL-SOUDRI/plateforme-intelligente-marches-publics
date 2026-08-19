class ContextBuilderService:

   def construire_contexte( self,resultats: list[dict]) -> str:

        if not resultats:
            return ""

        parties = []

        for i, resultat in enumerate(resultats,start=1):

            contenu = resultat["contenu"]

            metadata = resultat["metadata"]

            nom_fichier = metadata.get("nom_fichier","Inconnu" )

            type_source = metadata.get("type_source","Inconnu" )

            article_numero = metadata.get("article_numero","Inconnu")

            article_titre = metadata.get( "article_titre", "Inconnu")

            source = f"""
[Source {i}]

Document : {nom_fichier}
Type de source : {type_source}
Article : {article_numero}
Titre : {article_titre}

Contenu :
{contenu}
"""

            parties.append( source.strip())

        return "\n\n".join(parties)