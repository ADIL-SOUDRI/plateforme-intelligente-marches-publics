# cree pour le deux chat .
import re

class DocumentCleaningService:

    def nettoyer(self, texte: str) -> str:

        texte = texte.replace("\r\n", "\n")
        texte = texte.replace("\r", "\n")

        texte = re.sub(
            r"[ \t]+$",
            "",
            texte,
            flags=re.MULTILINE
        )

        texte = re.sub(
            r"\n{3,}",
            "\n\n",
            texte
        )

        texte = re.sub(
            r"[ \t]{2,}",
            " ",
            texte
        )

        texte = re.sub(
            r"(?m)^\s*\d{1,3}\s*$",
            "",
            texte
        )

        texte = re.sub(
            r"\n{3,}",
            "\n\n",
            texte
        )

        return texte.strip()