# par le 2


import re


class DocumentStructureService:

    ARTICLE_PATTERN = re.compile(
    r"(?im)^\s*(?:Article|ART\.?)\s+(premier|\d+)\s*(?::|\.|\s*-\s*)"
)

    def supprimer_sommaire(self, texte: str) -> str:

        matches = list(self.ARTICLE_PATTERN.finditer(texte) )

        if not matches:
            return texte.strip()

        for match in matches:

            debut = match.start()

            # Fin de la ligne du titre
            fin_ligne = texte.find("\n", debut)

            if fin_ligne == -1:
                fin_ligne = len(texte)

            ligne = texte[debut:fin_ligne].strip()

           

            if re.search(r"\s\d{1,3}$", ligne):
                continue

           

            texte_apres = texte[fin_ligne:].strip()

            if len(texte_apres) > 100:

                return texte[debut:].strip()

        return texte.strip()

    def trouver_articles(self,texte: str) -> list[dict]:

        articles = []

        matches = list(
            self.ARTICLE_PATTERN.finditer(texte)
        )

        for i, match in enumerate(matches):

            debut = match.start()

            if i + 1 < len(matches):

                fin = matches[i + 1].start()

            else:

                fin = len(texte)

            contenu = texte[
                debut:fin
            ].strip()

            titre = match.group(0).strip()

            numero = self._extraire_numero(
                titre
            )

            articles.append({
                "numero": numero,
                "titre": titre,
                "contenu": contenu
            })

        return articles

    def _extraire_numero(
    self,
    titre: str
) -> str:

        match = re.search(
            r"(?:Article|ART\.?)\s+(premier|\d+)",
            titre,
            re.IGNORECASE
        )

        if not match:
            return ""

        numero = match.group(1)

        if numero.lower() == "premier":
            return "1"

        return numero