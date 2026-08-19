# # from google import genai
# from groq import Groq
# from app.core.config import settings


# class GenerationService:

#     def __init__(self):

#         # self.client = genai.Client(
#         #     api_key=settings.GEMINI_API_KEY
#         # )

#         # self.model = "gemini-2.5-flash"

#         self.client = Groq(
#             api_key=settings.GROQ_API_KEY
#         )

#         self.model = "llama-3.3-70b-versatile"
        
#     def generer_reponse(
#         self,
#         question: str,
#         contexte: str
#     ) -> str:

#         prompt = f"""
# Tu es un assistant intelligent spécialisé
# dans les marchés publics marocains.

# Tu dois répondre à la question de l'utilisateur
# uniquement à partir du contexte fourni.

# Règles :
# - Utilise uniquement les informations présentes dans le contexte.
# - Ne crée pas d'informations qui ne sont pas présentes.
# - Si le contexte ne permet pas de répondre,
#   indique clairement que l'information n'a pas été trouvée.
# - Donne une réponse claire et concise.
# - Lorsque c'est possible, indique l'article et le document
#   utilisés pour répondre.

# CONTEXTE :
# --------------------
# {contexte}
# --------------------

# QUESTION :
# {question}

# RÉPONSE :
# """

#         response = self.client.models.generate_content(
#             model=self.model,
#             contents=prompt
#         )

#         return response.text

from groq import Groq
from app.core.config import settings


class GenerationService:

    def __init__(self):

        self.client = Groq( api_key=settings.GROQ_API_KEY)

        self.model = "openai/gpt-oss-20b"
        

    def generer_reponse( self, question: str, contexte: str ) -> str:

#         prompt = f"""
# Tu es un assistant intelligent spécialisé
# dans les marchés publics marocains.

# Tu dois répondre à la question de l'utilisateur
# uniquement à partir du contexte fourni.

# Règles :
# - Utilise uniquement les informations présentes dans le contexte.
# - Ne crée aucune information qui n'est pas présente dans le contexte.
# - Si le contexte ne permet pas de répondre,
#   indique clairement que l'information n'a pas été trouvée
#   dans les documents fournis.
# - Donne une réponse claire et concise.
# - Lorsque c'est possible, indique le document et l'article
#   utilisés pour répondre.

# ========== CONTEXTE ==========

# {contexte}

# ========== QUESTION ==========

# {question}

# ========== RÉPONSE ==========
# """
        prompt = f"""
Tu es un assistant spécialisé dans les marchés publics marocains.

Ta tâche est de répondre à la question UNIQUEMENT à partir
des informations présentes dans le contexte fourni.

========== RÈGLES OBLIGATOIRES ==========

1. Utilise exclusivement les informations présentes dans le contexte.

2. N'utilise aucune connaissance externe ou connaissance générale
   pour compléter la réponse.

3. N'invente JAMAIS :
   - un numéro d'article ;
   - un numéro de paragraphe ;
   - un nom de document ;
   - une obligation ;
   - une règle juridique ;
   - une source.

4. Si le contexte indique un article, utilise exactement
   le numéro d'article indiqué dans le contexte.

5. Si le contexte ne permet pas de connaître le numéro du
   paragraphe, NE DONNE PAS de numéro de paragraphe.

6. Si plusieurs documents sont présents dans le contexte,
   distingue clairement les informations provenant de chaque
   document.

7. Lorsque tu cites une information, indique si possible :
   - le document ;
   - le numéro de l'article ;
   - le titre de l'article.

8. Si l'information demandée n'est pas présente dans le contexte,
   réponds exactement dans cet esprit :
   "L'information demandée n'a pas été trouvée dans les documents
   fournis."

9. Si le contexte contient seulement une partie de la réponse,
   indique clairement que les informations sont partielles.

10. Ne transforme jamais une supposition en fait.

11. Ne complète jamais une référence incomplète.
    Par exemple, si le contexte contient :
    "Article 152"
    mais ne précise pas le paragraphe,
    écris simplement "Article 152" et jamais "Article 152, § ?".

12. Réponds en français.

13. Donne une réponse claire, structurée et concise.

========== CONTEXTE ==========

{contexte}

========== QUESTION ==========

{question}

========== RÉPONSE ==========
"""

        # response = self.client.chat.completions.create(
        #     model=self.model,
        #     messages=[
        #         {
        #             "role": "system",
        #             "content": (
        #                 "Tu es un assistant spécialisé "
        #                 "dans les marchés publics marocains."
        #             )
        #         },
        #         {
        #             "role": "user",
        #             "content": prompt
        #         }
        #     ],
        #     temperature=0.1
        # )

        # return response.choices[0].message.content
        response = self.client.chat.completions.create(
        model=self.model,
        messages=[
            {
                "role": "system",
                "content": (
                    "Tu es un assistant spécialisé "
                    "dans les marchés publics marocains. "
                    "Tu dois respecter strictement le contexte fourni "
                    "et ne jamais inventer de références."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.1
    )

        return response.choices[0].message.content