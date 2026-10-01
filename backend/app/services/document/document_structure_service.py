# import re

# class DocumentStructureService:

#     ARTICLE_PATTERN = re.compile(
#         r"(?im)^\s*(?:Article|ART\.?)\s+(premier|\d+)\s*(?::|\.|\s*-\s*)"
#     )

#     def supprimer_sommaire(self, texte: str) -> str:

#         matches = list( self.ARTICLE_PATTERN.finditer(texte))

#         if not matches:
#             return texte.strip()

#         for match in matches:

#             debut = match.start()

#             fin_ligne = texte.find(
#                 "\n",
#                 debut
#             )

#             if fin_ligne == -1:
#                 fin_ligne = len(texte)

#             ligne = texte[
#                 debut:fin_ligne
#             ].strip()

#             if re.search(
#                 r"\s\d{1,3}$",
#                 ligne
#             ):
#                 continue

#             texte_apres = texte[
#                 fin_ligne:
#             ].strip()

#             if len(texte_apres) > 100:

#                 return texte[
#                     debut:
#                 ].strip()

#         return texte.strip()


#     def trouver_articles(
#         self,
#         texte: str
#     ) -> list[dict]:

#         articles = []

#         matches = list(
#             self.ARTICLE_PATTERN.finditer(
#                 texte
#             )
#         )

#         for i, match in enumerate(matches):

#             debut = match.start()

#             if i + 1 < len(matches):

#                 fin = matches[
#                     i + 1
#                 ].start()

#             else:

#                 fin = len(texte)

#             contenu = texte[
#                 debut:fin
#             ].strip()

#             titre = match.group(
#                 0
#             ).strip()

#             numero = self._extraire_numero(
#                 titre
#             )

#             articles.append({

#                 "numero": numero,

#                 "titre": titre,

#                 "contenu": contenu

#             })

#         return articles


#     def _extraire_numero(
#         self,
#         titre: str
#     ) -> str:

#         match = re.search(
#             r"(?:Article|ART\.?)\s+(premier|\d+)",
#             titre,
#             re.IGNORECASE
#         )

#         if not match:

#             return ""

#         numero = match.group(1)

#         if numero.lower() == "premier":

#             return "1"

#         return numero

# import re


# class DocumentStructureService:

#     # Détection :
#     # Article 1 :
#     # Article 1.
#     # Article 1 -
#     # Article premier :
#     # ART. 1 :
#     # ART 1 :
#     ARTICLE_PATTERN = re.compile(
#         r"(?im)^\s*(?:Article|ART\.?)\s+"
#         r"(premier|\d+)"
#         r"\s*(?::|\.|-)?\s*(.*)$"
#     )

#     def supprimer_sommaire(self, texte: str) -> str:

#         matches = list(
#             self.ARTICLE_PATTERN.finditer(texte)
#         )

#         if not matches:
#             return texte.strip()

#         for match in matches:

#             debut = match.start()

#             fin_ligne = texte.find(
#                 "\n",
#                 debut
#             )

#             if fin_ligne == -1:
#                 fin_ligne = len(texte)

#             ligne = texte[
#                 debut:fin_ligne
#             ].strip()

#             # Évite de considérer les lignes de sommaire
#             if re.search(r"\s\d{1,3}$", ligne):
#                 continue

#             texte_apres = texte[
#                 fin_ligne:
#             ].strip()

#             if len(texte_apres) > 100:
#                 return texte[
#                     debut:
#                 ].strip()

#         return texte.strip()

#     # def trouver_articles(
#     #     self,
#     #     texte: str
#     # ) -> list[dict]:

#     #     articles = []

#     #     matches = list(
#     #         self.ARTICLE_PATTERN.finditer(
#     #             texte
#     #         )
#     #     )

#     #     for i, match in enumerate(matches):

#     #         debut = match.start()

#     #         if i + 1 < len(matches):

#     #             fin = matches[
#     #                 i + 1
#     #             ].start()

#     #         else:

#     #             fin = len(texte)

#     #         contenu = texte[
#     #             debut:fin
#     #         ].strip()

#     #         numero = self._extraire_numero(
#     #             match.group(1)
#     #         )

#     #         titre = self._extraire_titre(
#     #             match.group(2)
#     #         )

#     #         articles.append({

#     #             "numero": numero,

#     #             "titre": titre,

#     #             "contenu": contenu
#     #         })

#     #     return articles
#     def trouver_articles(self, texte: str):

#         articles = []

#         # for page_data in pages:

#             # page = page_data["page"]
#             # texte = page_data["texte"]

#         # matches = list(
#         #         self.ARTICLE_PATTERN.finditer(texte)
#         #     )
#         matches = list(
#             self.ARTICLE_PATTERN.finditer(
#                 texte
#             )
#         )

        

#             # for i, match in enumerate(matches):

#             #     debut = match.start()

#             #     if i + 1 < len(matches):

#             #         fin = matches[i + 1].start()

#             #     else:

#             #         fin = len(texte)

#             #     contenu = texte[
#             #         debut:fin
#             #     ].strip()

#             #     titre = match.group(0).strip()

#             #     numero = self._extraire_numero(
#             #         titre
#             #     )
#         for i, match in enumerate(matches):

#                 debut = match.start()

#                 if i + 1 < len(matches):
#                     fin = matches[i + 1].start()
#                 else:
#                     fin = len(texte)

#                 contenu = texte[debut:fin].strip()

#                 titre = match.group(0).strip()

#                 numero = self._extraire_numero(titre)

#                 # Chercher la dernière page avant l'article
#                 texte_avant = texte[:debut]

#                 pages = re.findall(
#                     r"\[PAGE:(\d+)\]",
#                     texte_avant
#                 )

#                 page = int(pages[-1]) if pages else None


#                 articles.append({

#                     "numero": numero,

#                     "titre": titre,

#                     "contenu": contenu,

#                     "page": page
#                 })

#         return articles

#     def _extraire_numero(
#         self,
#         numero: str
#     ) -> str:

#         if numero.lower() == "premier":

#             return "1"

#         return numero

#     def _extraire_titre(
#         self,
#         texte: str
#     ) -> str:

#         if not texte:
#             return ""

#         titre = texte.strip()

#         # Nettoyage éventuel
#         titre = re.sub(
#             r"\s+",
#             " ",
#             titre
#         )

#         return titre


import re


class DocumentStructureService:

    ARTICLE_PATTERN = re.compile(
        r"(?im)^\s*(?:Article|ART\.?)\s+"
        r"(premier|\d+)"
        r"\s*(?::|\.|-)?\s*(.*)$"
    )

    PAGE_PATTERN = re.compile(
        r"\[PAGE:(\d+)\]"
    )

    # ==========================================================
    # SUPPRIMER LE SOMMAIRE
    # ==========================================================

    def supprimer_sommaire(self, texte: str) -> str:

        matches = list(
            self.ARTICLE_PATTERN.finditer(texte)
        )

        if not matches:
            return texte.strip()

        for match in matches:

            debut = match.start()

            fin_ligne = texte.find(
                "\n",
                debut
            )

            if fin_ligne == -1:
                fin_ligne = len(texte)

            ligne = texte[
                debut:fin_ligne
            ].strip()

            # Exemple :
            # Article 44 : Prix de référence 30
            # => probablement une ligne du sommaire
            if re.search(
                r"\s\d{1,3}$",
                ligne
            ):
                continue

            texte_apres = texte[
                fin_ligne:
            ].strip()

            if len(texte_apres) > 100:

                return texte[
                    debut:
                ].strip()

        return texte.strip()

    # ==========================================================
    # TROUVER LES ARTICLES
    # ==========================================================

    def trouver_articles(
        self,
        texte: str
    ):

        articles = []

        matches = list(
            self.ARTICLE_PATTERN.finditer(
                texte
            )
        )

        print(
            "\nNombre de débuts d'articles détectés :",
            len(matches)
        )

        for i, match in enumerate(matches):

            debut = match.start()

            # --------------------------------------------------
            # FIN DE L'ARTICLE
            # --------------------------------------------------

            if i + 1 < len(matches):

                fin = matches[
                    i + 1
                ].start()

            else:

                fin = len(texte)

            contenu = texte[
                debut:fin
            ].strip()

            # --------------------------------------------------
            # NUMERO
            # --------------------------------------------------

            numero = self._extraire_numero(
                match.group(1)
            )

            # --------------------------------------------------
            # TITRE
            # --------------------------------------------------

            titre = match.group(2).strip()

            # Nettoyage
            titre = re.sub(
                r"\s+",
                " ",
                titre
            )

            # --------------------------------------------------
            # PAGE
            # --------------------------------------------------

            texte_avant = texte[:debut]

            pages = re.findall(
                self.PAGE_PATTERN,
                texte_avant
            )

            page = (
                int(pages[-1])
                if pages
                else None
            )

            # --------------------------------------------------
            # DEBUG
            # --------------------------------------------------

            print("\n-----------------------------")

            print(
                "Article :",
                numero
            )

            print(
                "Titre :",
                titre
            )

            print(
                "Page :",
                page
            )

            print(
                "Longueur contenu :",
                len(contenu)
            )

            print(
                "-----------------------------")

            # --------------------------------------------------
            # AJOUT
            # --------------------------------------------------

            articles.append({

                "numero": numero,

                "titre": titre,

                "contenu": contenu,

                "page": page

            })

        return articles

    # ==========================================================
    # EXTRAIRE NUMERO
    # ==========================================================

    def _extraire_numero(
        self,
        numero: str
    ) -> str:

        if numero.lower() == "premier":

            return "1"

        return numero