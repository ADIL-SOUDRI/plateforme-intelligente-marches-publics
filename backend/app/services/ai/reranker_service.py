from sentence_transformers import CrossEncoder


class RerankerService:

    def __init__(self):

        self.model = CrossEncoder(
            "BAAI/bge-reranker-v2-m3"
        )


    def reranker(
        self,
        question: str,
        resultats: list[dict],
        top_k: int = 5
    ):

        if not resultats:

            return []


        pairs = []

        for resultat in resultats:

            pairs.append(
                (
                    question,
                    resultat["contenu"]
                )
            )


        scores = self.model.predict(
            pairs
        )


        for resultat, score in zip(
            resultats,
            scores
        ):

            resultat["rerank_score"] = float(
                score
            )


        resultats.sort(
            key=lambda x: x["rerank_score"],
            reverse=True
        )


        return resultats[:top_k]