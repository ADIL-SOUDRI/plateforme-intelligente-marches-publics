from app.services.rag.generation_service import GenerationService


service = GenerationService()


question = """
Quelle est la procédure exacte de paiement
du titulaire après réception des fournitures ?
"""


contexte = """
Document : ccag_fournitures.pdf
Type : CCAG
Article : 30
Titre : Mesures de sécurité et d'hygiène

Le cahier des prescriptions communes ou le cahier
des prescriptions spéciales définit les mesures que
le fournisseur doit prendre pour assurer la sécurité
et l'hygiène dans les lieux d'exécution du marché.

Ces mesures concernent notamment :
- le service médical ;
- les conditions de sécurité et de protection
  du personnel et des tiers ;
- la protection de l'environnement.
"""


reponse = service.generer_reponse(
    question,
    contexte
)


print("\n========== QUESTION ==========")
print(question)

print("\n========== RÉPONSE ==========")
print(reponse)