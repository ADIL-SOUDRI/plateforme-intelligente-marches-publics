from pathlib import Path

from pypdf import PdfReader
from docx import Document


class DocumentExtractionService:

    def extraire_texte(self, chemin_fichier: str) -> str:

        chemin = Path(chemin_fichier)

        if not chemin.exists():
            raise FileNotFoundError(f"Fichier introuvable : {chemin}")

        extension = chemin.suffix.lower()

        if extension == ".pdf":
            return self._extraire_pdf(chemin)

        elif extension == ".docx":
            return self._extraire_docx(chemin)

        else:
            raise ValueError(f"Format non supporté : {extension}")

    def _extraire_pdf(self, chemin: Path) -> str:

        reader = PdfReader(str(chemin))

        textes = []

        for page in reader.pages:

            texte = page.extract_text()

            if texte:
                textes.append(texte)

        return "\n".join(textes)

    def _extraire_docx(self, chemin: Path) -> str:

        document = Document(str(chemin))

        textes = []

        for paragraphe in document.paragraphs:

            if paragraphe.text.strip():
                textes.append(paragraphe.text)

        return "\n".join(textes)