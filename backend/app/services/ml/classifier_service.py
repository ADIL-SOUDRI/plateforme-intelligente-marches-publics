# 


# from transformers import pipeline


# class ClassifierService:

#     def __init__(self):

#         print("Chargement du modèle Zero-Shot...")

#         self.classifier_model = pipeline(
#             "zero-shot-classification",
#             model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli"
#         )

#         self.domaines = [
#             "Bâtiment",
#             "Génie civil",
#             "VRD",
#             "Électricité",
#             "Plomberie",
#             "Assainissement",
#             "Informatique",
#             "Maintenance",
#             "Nettoyage",
#             "Gardiennage",
#             "Transport",
#             "Mobilier",
#             "Matériel médical",
#             "Fournitures de bureau",
#             "Études techniques",
#             "Ingénierie",
#             "Architecture",
#             "Agriculture"
#         ]

#         print("Modèle Zero-Shot chargé.")


#     def classifier(self, texte: str):

#         resultat = self.classifier_model(
#             texte,
#             candidate_labels=self.domaines,
#             multi_label=False
#         )

#         domaine = resultat["labels"][0]
#         confiance = resultat["scores"][0]

#         return {
#             "domaine": domaine,
#             "confiance": float(confiance)
#         }
# from transformers import pipeline


# class ClassifierService:

#     def __init__(self):

#         print("Chargement du modèle Zero-Shot...")

#         self.classifier_model = pipeline(
#             "zero-shot-classification",
#             model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli"
#         )

#         self.domaines = [
#             "Bâtiment",
#             "Génie civil",
#             "VRD",
#             "Électricité",
#             "Plomberie",
#             "Assainissement",
#             "Informatique",
#             "Maintenance",
#             "Nettoyage",
#             "Gardiennage",
#             "Transport",
#             "Mobilier",
#             "Matériel médical",
#             "Fournitures de bureau",
#             "Études techniques",
#             "Ingénierie",
#             "Architecture",
#             "Agriculture"
#         ]

#         print("Modèle Zero-Shot chargé.")

#     def classifier(self, texte: str):

#         resultat = self.classifier_model(
#             texte,
#             candidate_labels=self.domaines,
#             multi_label=False
#         )

#         return {
#             "domaine": resultat["labels"][0],
#             "confiance": float(resultat["scores"][0])
#         }
# import json
# import re

# from google import genai
# from app.core.config import settings


# class ClassifierService:

#     def __init__(self):

#         self.client = genai.Client(
#             api_key=settings.GEMINI_API_KEY
#         )

#         self.model = "gemini-3.5-flash-lite"

#         self.domaines = [
#             "Bâtiment",
#             "Génie civil",
#             "VRD",
#             "Électricité",
#             "Plomberie",
#             "Assainissement",
#             "Informatique",
#             "Maintenance",
#             "Nettoyage",
#             "Gardiennage",
#             "Transport",
#             "Mobilier",
#             "Matériel médical",
#             "Fournitures de bureau",
#             "Études techniques",
#             "Ingénierie",
#             "Architecture",
#             "Agriculture"
#         ]

#     def classifier(self, texte: str):

#         prompt = f"""
# Tu es un expert en classification des marchés publics marocains.

# Analyse le texte du marché fourni ci-dessous et détermine
# le domaine principal de la prestation.

# DOMAINES POSSIBLES :

# {", ".join(self.domaines)}

# RÈGLES :

# 1. Choisis un seul domaine.

# 2. Analyse principalement l'objet du marché,
# les travaux, les fournitures, les équipements
# ou les prestations décrites.

# 3. Ignore les clauses juridiques générales,
# les conditions administratives et les informations
# qui ne permettent pas d'identifier le domaine.

# 4. Si plusieurs domaines apparaissent, choisis
# celui qui correspond à l'objet principal du marché.

# 5. "Maintenance des équipements électriques"
# doit être classé dans "Électricité".

# 6. "Développement d'une application", "réseau informatique",
# "serveurs informatiques", "logiciels" doivent être classés
# dans "Informatique".

# 7. "Construction d'une route", "pont", "tunnel",
# "ouvrage d'art" doivent être classés dans "Génie civil".

# 8. "Peinture", "rénovation", "construction",
# "façades", "bâtiment" doivent être classés dans "Bâtiment"
# lorsqu'ils concernent principalement un bâtiment.

# 9. "Fourniture de mobilier" doit être classée dans "Mobilier".

# 10. Retourne UNIQUEMENT un JSON valide.

# Format obligatoire :

# {{
#     "domaine": "nom exact du domaine",
#     "confiance": 0.95
# }}

# Texte du marché :

# {texte}
# """

#         response = self.client.models.generate_content(
#             model=self.model,
#             contents=prompt
#         )

#         contenu = response.text.strip()

#         contenu = re.sub(
#             r"```json|```",
#             "",
#             contenu
#         ).strip()

#         resultat = json.loads(contenu)

#         domaine = resultat["domaine"]
#         confiance = float(resultat["confiance"])

#         if domaine not in self.domaines:
#             raise ValueError(
#                 f"Domaine retourné par Gemini invalide : {domaine}"
#             )

#         return {
#             "domaine": domaine,
#             "confiance": confiance
#         }

import joblib


class ClassifierService:

    def __init__(self):

        self.model = joblib.load(
            "app/services/ml/model.pkl"
        )

    def classifier(self, texte: str):

        domaine = self.model.predict(
            [texte]
        )[0]

        probabilites = self.model.predict_proba(
            [texte]
        )[0]

        confiance = max(probabilites)

        return {
            "domaine": domaine,
            "confiance": float(confiance)
        }