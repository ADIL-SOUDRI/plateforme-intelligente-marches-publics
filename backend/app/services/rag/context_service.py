# # class ContextService:

# #     def construire_contexte(  self,   resultats: list[dict] ) -> str:

# #         parties = []

# #         for i, resultat in enumerate( resultats,start=1):

# #             metadata = resultat["metadata"]

# #             contenu = resultat["contenu"]

# #             partie = f"""
# # --- SOURCE {i} ---

# # Document : {metadata.get("nom_fichier")}
# # Type : {metadata.get("type_source")}
# # Article : {metadata.get("article_numero")}
# # Titre : {metadata.get("article_titre")}
# # Page : {metadata.get("page")}
# # if page is not None:
# #     source += f"Page : {Page}\n"
# # Distance : {resultat.get("distance")}

# # Contenu :
# # {contenu}
# # """

# #             parties.append(partie)

# #         return "\n".join(parties)

# class ContextService:

#     def construire_contexte(
#         self,
#         resultats: list[dict]
#     ) -> str:

#         parties = []

#         for i, resultat in enumerate(resultats, start=1):

#             metadata = resultat["metadata"]
#             contenu = resultat["contenu"]

#             nom_fichier = metadata.get(
#                 "nom_fichier",
#                 "Inconnu"
#             )

#             type_source = metadata.get(
#                 "type_source",
#                 "Inconnu"
#             )

#             article_numero = metadata.get(
#                 "article_numero",
#                 "Inconnu"
#             )

#             article_titre = metadata.get(
#                 "article_titre"
#             )

#             page = metadata.get("page")

#             distance = resultat.get("distance")

#             partie = f"""
# --- SOURCE {i} ---

# Document : {nom_fichier}
# Type : {type_source}
# Article : {article_numero}
# """

           
#             if article_titre:
#                 partie += f"""Titre de l'article : {article_titre}
# """

            
#             if page is not None:
#                 partie += f"""Page : {page}
# """

#             partie += f"""Distance : {distance}

# Contenu :
# {contenu}
# """

#             parties.append(partie.strip())

#         return "\n\n".join(parties)

class ContextService:

    def construire_contexte(
        self,
        resultats: list[dict]
    ) -> str:

        parties = []


        for i, resultat in enumerate(
            resultats,
            start=1
        ):

            metadata = resultat["metadata"]

            contenu = resultat["contenu"]


            partie = f"""
========== SOURCE {i} ==========

Document :
{metadata.get("nom_fichier", "Inconnu")}

Type de source :
{metadata.get("type_source", "Inconnu")}

Chapitre :
{metadata.get("chapitre", "Non précisé")}

Section :
{metadata.get("section", "Non précisée")}

Article :
{metadata.get("article_numero", "Non précisé")}

Titre de l'article :
{metadata.get("article_titre", "Non précisé")}

Page :
{metadata.get("page", "Non précisée")}

Score de pertinence :
{resultat.get("rerank_score", resultat.get("distance", ""))}

Contenu :
{contenu}

========== FIN SOURCE {i} ==========
"""

            parties.append(
                partie.strip()
            )


        return "\n\n".join(
            parties
        )